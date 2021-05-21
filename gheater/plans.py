import pathlib
import uuid

import bluesky.plan_stubs as bps
import bluesky.plans as bp
import bluesky.preprocessors as bpp
import numpy as np
import pyFAI
from bluesky.callbacks import LiveTable
from databroker.v0 import Broker
from tifffile import TiffWriter
from xpdacq.beamtime import (
    open_shutter_stub,
    close_shutter_stub,
    _check_mini_expo
)
from xpdacq.glbl import glbl
from xpdacq.xpdacq_conf import xpd_configuration


def configure_area_det_expo(exposure):
    """Configure the exposure time of the detector in `xpd_configuration`.

    Parameters
    ----------
    exposure : float
        The exposure time in seconds.
    """
    det = xpd_configuration["area_det"]
    yield from bps.abs_set(
        det.cam.acquire_time, glbl["frame_acq_time"], wait=True
    )
    acq_time = det.cam.acquire_time.get()
    _check_mini_expo(exposure, acq_time)
    # compute number of frames
    num_frame = np.ceil(exposure / acq_time)
    yield from bps.abs_set(det.images_per_set, num_frame, wait=True)
    computed_exposure = num_frame * acq_time
    # print exposure time
    print(
        "INFO: requested exposure time = {} - > computed exposure time"
        "= {}".format(exposure, computed_exposure)
    )
    return num_frame, acq_time, computed_exposure


def gradient_heating_plan(dets, expo_time, calib_map,
                          x_motor, x_pos_interval,
                          y_motor, y_pos_interval,
                          num_pos,
                          num_loops=1):
    """
    gradient heating scan; setting calibration info at each location

    The x/y-movement is used to compensate the small tilting of the
    sample (so that beam will hit the center of capillary). If it
    is not needed, please pass argument `x_pos_interval` or
    `y_post_interval` as 0 and the scan will only go through one
    dimension.

    Example:
    --------
    gradient heating scan over 15 points along sample,
    with 1 unit (depends on motor) between points for 2 loops;
    exposure time = 5s for each point and recording

       1. area detector image

       2. x- and y-motor position

       3. thermal coupler readback
    at each position

    Example syntax of this scan plan
    >>> plan = gradient_heating_plan([pe1c, eurotherm],
                                     5, {},
                                     ss_stg_x, 1.25,
                                     ss_stg_y, 1.75,
                                     17, 1
                                     )
    >>> xrun(<sample_ind>, plan)
    """
    _dets = list(dets) + [x_motor, y_motor]
    print("This scan will collect data with interval = {} along"
          " x-direction and interval = {} along y-direction"
          " with total {} points".format(x_pos_interval,
                                         y_pos_interval,
                                         num_pos)
          )
    rv = yield from configure_area_det_expo(expo_time)
    num_frame, acq_time, computed_exposure = rv
    # scan md
    _md = {"sp_time_per_frame": acq_time,
           "sp_num_frames": num_frame,
           "sp_requested_exposure": expo_time,
           "sp_computed_exposure": computed_exposure,
           "sp_type": "gradient_heating",
           "sp_plan_name": "gradient_heating",
           "sp_uid": str(uuid.uuid4()),
           }
    # motor hints
    x_fields = []
    for motor in (x_motor, y_motor):
        x_fields.extend(getattr(motor, 'hints', {}).get('fields', []))
    default_dimensions = [(x_fields, 'primary')]
    default_hints = {}
    if len(x_fields) > 0:
        default_hints.update(dimensions=default_dimensions)
    _md['hints'] = default_hints

    if calib_map is None:
        print('WARNING: no calib info is found')
        print("Ignore if this is a calibration run")
    print("INFO: this plan is going to be run {} times".format(num_loops))
    # FIXME: check this at beamline
    x_pos_0 = x_motor.position
    y_pos_0 = y_motor.position
    for i in range(num_loops):
        for j in range(num_pos):
            yield from bps.mvr(x_motor, x_pos_interval,
                               y_motor, y_pos_interval)
            yield from bps.checkpoint()  # check point for revert
            calib_md = calib_map.get(j, None)
            if calib_md:
                _md["calibration_md"] = calib_md
            elif not calib_md and calib_map:
                e = "No calibration info at {}-th position".format(j)
                raise RuntimeError(e)
            plan = bp.count(_dets, num=1, md=_md)
            plan = bpp.subs_wrapper(plan, LiveTable(_dets))
            yield from open_shutter_stub()
            yield from plan
            yield from close_shutter_stub()
        yield from bps.mv(x_motor, x_pos_0,
                          y_motor, y_pos_0)  # move back to origin
        yield from bps.checkpoint()
    print("END of gradient heating scan")


def multi_calib_scan(detectors: list, *args, num: int, exposure: float = None, wait_per_step: float = 0.,
                     calib_map: list = None, md: dict = None):
    """Run the line scan using one calibration at one point.

    Parameters
    ----------
    detectors :
        The detectors.
    args :
        A sequence of `motor1, start1, end1, motor2, start2, end2`.
    num :
        The number of points to collect on the line.
    exposure :
        The exposure time at each point in seconds.
    wait_per_step :
        The time to wait before open the shutter at each step in seconds.
    calib_map :
        The list of calibration data. It should be in the same order of the exposure and the number should be equal to the number of points.
    md :
        The metadata of the run.
    """
    if not md:
        md = {}
    if not calib_map:
        print("No calib_map. This is a calibration run.")
    elif len(calib_map) != num:
        raise ValueError("The length of calib_map must be equal to num: {} != {}".format(len(calib_map), num))
    if exposure:
        yield from configure_area_det_expo(exposure)
    # get the motors and points
    if len(args) < 3:
        raise ValueError("There must be at least 3 arguments: motor, start, end.")
    motors = list(args[::3])
    # add hints
    x_fields = []
    for motor in motors:
        x_fields.extend(getattr(motor, 'hints', {}).get('fields', []))
    default_dimensions = [(x_fields, 'primary')]
    default_hints = {}
    if len(x_fields) > 0:
        default_hints.update(dimensions=default_dimensions)
    md['hints'] = default_hints
    # calculate the positions
    if num <= 0:
        raise ValueError("Number of points must be positive.")
    starts, ends = args[1::3], args[2::3]
    lines = [np.linspace(start, end, num).tolist() for start, end in zip(starts, ends)]

    # start run

    def get_positions(j):
        lst = []
        for m, l in zip(motors, lines):
            lst.append(m)
            lst.append(l[j])
        return lst

    all_detectors = detectors + motors
    for i in range(num):
        yield from bps.mv(*get_positions(i))
        yield from bps.checkpoint()
        if calib_map:
            calib_md = calib_map[i]
            md["calibration_md"] = calib_md
        plan = bp.count(all_detectors, md=md)
        plan = bpp.subs_wrapper(plan, LiveTable(all_detectors))
        yield from bps.sleep(wait_per_step)
        yield from open_shutter_stub()
        yield from plan
        yield from close_shutter_stub()
    yield from bps.mv(*get_positions(0))
    yield from bps.checkpoint()


def gen_beautiful_plan(detectors: list, *args, num: int, calib_map: list = None, exposure: float = None,
                       wait_per_step: float = 0., num_loop: int = 1, heater, final_temp: float,
                       sleep_time: float = 0., md: dict = None):
    """Generate the plan for the whole measurement.

    Run the line scan for x times.
    Cool down to x K.
    Wait for x seconds.
    Run the line scan for the last time.

    Parameters
    ----------
    detectors :
        The detectors.
    args :
        A sequence of `motor1, start1, end1, motor2, start2, end2`.
    num :
        The number of points to collect on the line.
    exposure :
        The exposure time at each point in seconds.
    wait_per_step :
        The time to wait before open the shutter at each step in seconds.
    calib_map :
        The list of calibration data. It should be in the same order of the exposure and the number should be equal to the number of points.
    num_loop :
        The number of loops to run.
    heater :
        The heater to cool down the system.
    final_temp :
        The temperature for the final scan.
    sleep_time :
        The time to wait before the final scan.
    md :
        The metadata of the plan.
    """
    if not md:
        md = {}
    if exposure:
        yield from configure_area_det_expo(exposure)
    # start run
    for _ in range(num_loop):
        yield from multi_calib_scan(detectors, *args, num=num, calib_map=calib_map, md=md)
    # cool down
    yield from bps.mv(heater, final_temp)
    yield from bps.sleep(sleep_time)
    # final scan
    yield from multi_calib_scan(detectors, *args, num=num, calib_map=calib_map, md=md)


def calib_map_gen(calib_file_dir: str, pattern='*.poni') -> list:
    """Get a list of calibration data from the poni files in a folder.

    Parameters
    ----------
    calib_file_dir :
        The directory of the poni files.
    pattern :
        The pattern of the poni file names.
    """
    fns = sorted([str(x) for x in pathlib.Path(calib_file_dir).glob(pattern)])
    rv = []
    for i, fn in enumerate(fns):
        print('{} --> {}'.format(i, fn))
        calib_md = dict(pyFAI.load(fn).getPyFAI())
        rv.append(calib_md)
    return rv


def process_and_save(db: Broker, uid, tiff_path: str, data_key: str) -> None:
    """Process the image data in the last run and save ther result.

    Parameters
    ----------
    db :
        The databroker object.
    uid :
        The uid or the index of the run.
    tiff_path :
        The path to the tiff file to save.
    data_key :
        The data key of the image.
    """
    run = db[uid]
    dk_uid = run.start.get("sc_dk_field_uid", "")
    dk_run = db[dk_uid] if dk_uid else None
    dk_image = _mean(dk_run.data(data_key)) if dk_run else None
    image = _mean(run.data(data_key))
    image -= dk_image
    tw = TiffWriter(tiff_path)
    tw.write(image)
    return


def _mean(images):
    """Calculate the mean of a image generator."""
    try:
        total = next(images)
    except StopIteration:
        print("No images found. Use 0.")
        return 0.
    num = 1
    for image in images:
        total += image
    mean = total / num
    if np.ndim(mean) == 3:
        mean = np.mean(mean, axis=0)
    return mean
