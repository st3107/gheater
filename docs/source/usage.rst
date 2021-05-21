.. code:: ipython3

    %run -i 999-load.py


.. parsed-literal::

    /Users/sst/anaconda3/envs/test_xpdstack/lib/python3.8/site-packages/databroker/v1.py:1602: UserWarning: Failed to load config. Falling back to v0.Exception was: Unable to handle metadatastore.module 'databroker.headersource.sqlite'
      warnings.warn(


.. parsed-literal::

    No config file could be found in the following locations:
    /Users/sst/.config/acq
    /Users/sst/anaconda3/envs/test_xpdstack/etc/acq
    /etc/acq
    Loading from packaged simulation configuration
    INFO: Initializing the XPD data acquisition environment ...
    INFO: area detector has been configured to new acquisition time (time per frame)  = 0.1s
    INFO: Reload beamtime objects:
    
    ScanPlans:
    0: ct_5
    1: ct_0.1
    2: ct_1
    3: ct_10
    4: ct_30
    5: ct_60
    
    Samples:
    0: poop
    1: SrTiO3
    
    {'Verification time': '2021-05-20 13:54:39', 'Verified by': 'st'}


.. parsed-literal::

    
    Is this configuration correct? y/n:  y
    Please input your initials:  st


.. parsed-literal::

    INFO: beamtime object has been linked
    
    INFO: beamtime object has been linked
    
    INFO: Initialized glbl, bt, xrun.
    INFO: Publish data to localhost port 5567 with prefix 'raw'.
    INFO: Changed home to /Users/sst/acqsim/xpdUser
    OK, ready to go.  To continue, follow the steps in the xpdAcqdocumentation at http://xpdacq.github.io/xpdacq


How to use the scripts during the beamtime?
===========================================

Preparation
-----------

Load the functions into the namespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to load the functions into the namespace from the file
``plans.py``. Use the following command and remember to change the path
to the file on your machine:

.. code:: ipython3

    %run -i "~/PycharmProjects/gheater/gheater/plans.py"

Start save server
~~~~~~~~~~~~~~~~~

In your terminal, start the save server. The save server is used to save
the data on a hard disk in files.

``python save_server.py``

Calibration
-----------

Now, we will run the calibration of the gradient heater. Here, we
compose the plan using ``multi_calib_scan``. In this plan, the
diffraction image on the detector ``pe1c`` will be collected in a line.
The ``ns.motor1`` will move from ``0`` to ``5`` and the ``ns.motor2``
will move from ``0`` to ``0.5``. In total, ``6`` evenly spaced points
(including the start and the end) will be collected. Before the
collection, wait for ``2`` seconds for the detector to “cool” down and
then open the shutter to collect the image. The exposure time at each
point is ``5`` second. The metadata we would like to record is
``{"task": "calibration"}`` (optional).

.. code:: ipython3

    from bluesky.simulators import summarize_plan
    
    
    plan = multi_calib_scan([pe1c], ns.motor1, 0, 5, ns.motor2, 0, 0.5, num=6, wait_per_step=2., exposure=5., md={"task": "calibration"})
    xrun({}, plan)


.. parsed-literal::

    No calib_map. This is a calibration run.
    INFO: requested exposure time = 5.0 - > computed exposure time= 5.0
    INFO: closing shutter...
    INFO: taking dark frame....
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out


.. parsed-literal::

    /Users/sst/anaconda3/envs/test_xpdstack/lib/python3.8/site-packages/bluesky/callbacks/core.py:332: UserWarning: The key pe1_image will be skipped because LiveTable does not know how to display the dtype array
      warnings.warn("The key {} will be skipped because LiveTable "


.. parsed-literal::

    
    
    +-----------+------------+
    |   seq_num |       time |
    +-----------+------------+
    |         1 | 13:52:15.7 |
    +-----------+------------+
    generator count ['45fb097d'] (scan num: 1)
    
    
    dark frame complete, update dark dict
    opening shutter...
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:16.8 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['983c1be4'] (scan num: 2)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:19.9 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['c282db3a'] (scan num: 3)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:23.2 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['57150d0a'] (scan num: 4)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:26.4 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['f818a935'] (scan num: 5)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:29.5 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['12564b24'] (scan num: 6)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:32.7 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['efa6cd06'] (scan num: 7)
    
    




.. parsed-literal::

    ('45fb097d-f659-44cf-99da-fa75c498770b',
     '983c1be4-2f37-4c65-ad85-58ec8ce66cdf',
     'c282db3a-e722-46ca-b942-9ae7c9990017',
     '57150d0a-b856-42e9-86ff-07a880f06be5',
     'f818a935-3679-4087-a41d-fabf6ee340e4',
     '12564b24-b178-49db-a8bf-38d142108c5c',
     'efa6cd06-1150-4185-883b-e2179aa845bb')



After this scan is finished, the dark subtracted images will be saved in
the ``tiff_base`` folder. Now, we need to use ``pyFAI-calib2`` to
calibrate the tiff images and save the resulting poni file in a folder.
Here, an example of the command is shown. It means “calibrate the
image.tiff where the wavelength is 0.1675 A, the detector is
perkin_elmer and the D-spacing of the calibrant is record in ‘Ni24.D
file’.”

``pyFAI-calib2 -w 0.1675 -D perkin_elmer -C ./Ni24.D image.tiff``

Here, in this tutorial, we save the results in the ``poni_files``
folder. Below shows what files are inside this folder. The requirement
for the filename is that it can be sorted in the same order as the
diffraction is measured. For example, ``calib_0.poni`` is first file and
it is also the file generated from the calibration of the first image
from the scan.

.. code:: ipython3

    !tree "/Users/sst/PycharmProjects/gheater/notebooks/poni_files"


.. parsed-literal::

    /Users/sst/PycharmProjects/gheater/notebooks/poni_files
    ├── calib_0.poni
    ├── calib_1.poni
    ├── calib_2.poni
    ├── calib_3.poni
    ├── calib_4.poni
    └── calib_5.poni
    
    0 directories, 6 files


Now, we can load the calibration results from files to the namespace
using ``calib_map_gen``.

.. code:: ipython3

    calib_map = calib_map_gen("/Users/sst/PycharmProjects/gheater/notebooks/poni_files")


.. parsed-literal::

    0 --> /Users/sst/PycharmProjects/gheater/notebooks/poni_files/calib_0.poni
    1 --> /Users/sst/PycharmProjects/gheater/notebooks/poni_files/calib_1.poni
    2 --> /Users/sst/PycharmProjects/gheater/notebooks/poni_files/calib_2.poni
    3 --> /Users/sst/PycharmProjects/gheater/notebooks/poni_files/calib_3.poni
    4 --> /Users/sst/PycharmProjects/gheater/notebooks/poni_files/calib_4.poni
    5 --> /Users/sst/PycharmProjects/gheater/notebooks/poni_files/calib_5.poni


Start the measurement
---------------------

Now, we can heat the gradient heater and wait for the equilibrium. Then,
we start the measurement plan using ``gen_beautiful_plan``.

In this example, we start measurement by running a line scan. The
diffraction image on the detector ``pe1c`` will be collected in a line.
The ``ns.motor1`` will move from ``0`` to ``5`` and the ``ns.motor2``
will move from ``0`` to ``0.5``. In total, ``6`` evenly spaced points
(including the start and the end) will be collected. Before the
collection, wait for ``2`` seconds for the detector to “cool” down and
then open the shutter to collect the image. The exposure time at each
point is ``5`` second. The metadata we would like to record is
``{"task": "day time scan"}`` (optional). At each point ``i``, the
calibration data from ``calib_map[i]`` will be used for the data
processing.

We run the line scan for ``num_loop=2`` times. Then, we will let the
heater ``cs700`` to cool the temperature down to ``final_temp=300`` and
wait there for the ``sleep_time=5`` seconds. Then, we conduct a final
line scan just like that in the beginning.

.. code:: ipython3

    plan = gen_beautiful_plan([pe1c], ns.motor1, 0, 5, ns.motor2, 0, 0.5, num=6, calib_map=calib_map, exposure=5, num_loop=2, heater=cs700, final_temp=300, sleep_time=5, md={"task": "day time scan"})
    xrun({}, plan)


.. parsed-literal::

    INFO: requested exposure time = 5 - > computed exposure time= 5.0
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:44.6 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['51c1c1bb'] (scan num: 8)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:45.8 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['aa2a209c'] (scan num: 9)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:46.9 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['b7f64dc5'] (scan num: 10)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:48.1 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['33f68b9f'] (scan num: 11)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:49.5 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['cf90d1ec'] (scan num: 12)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:50.6 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['d7be71e4'] (scan num: 13)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:51.7 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['f9be9ece'] (scan num: 14)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:52.7 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['8e291a80'] (scan num: 15)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:53.9 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['39c42625'] (scan num: 16)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:55.0 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['52c9537e'] (scan num: 17)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:56.2 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['e5da38bb'] (scan num: 18)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:52:57.4 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['7d3a6e6a'] (scan num: 19)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:53:03.8 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['33e09bf5'] (scan num: 20)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:53:05.4 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['459c4976'] (scan num: 21)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:53:07.4 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['a6575ab3'] (scan num: 22)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:53:08.8 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['da1207ff'] (scan num: 23)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:53:10.0 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['8ecefcd3'] (scan num: 24)
    
    
    INFO: No calibration file found in config_base.
    Scan will still keep going on....
    INFO: Current filter status
    INFO: flt1 : In
    INFO: flt2 : Out
    INFO: flt3 : Out
    INFO: flt4 : Out
    
    
    +-----------+------------+------------+-----------------+------------+-----------------+
    |   seq_num |       time |     motor1 | motor1_setpoint |     motor2 | motor2_setpoint |
    +-----------+------------+------------+-----------------+------------+-----------------+
    |         1 | 13:53:11.1 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['0b7ef4f3'] (scan num: 25)
    
    




.. parsed-literal::

    ('51c1c1bb-7207-4b60-96a5-0112c1a39757',
     'aa2a209c-e459-4b44-b6e1-1472c83419eb',
     'b7f64dc5-1bd1-4e5c-a5cd-661ae3009bc2',
     '33f68b9f-09f3-4b80-a7bb-2cf08198eb95',
     'cf90d1ec-4c23-4f22-b6e9-019cb3c0de15',
     'd7be71e4-f954-472e-ad53-104dc34d3e5c',
     'f9be9ece-85a7-48c1-a1e8-4275c1bc46aa',
     '8e291a80-f987-44d5-9ffd-4c694daa37ea',
     '39c42625-e7bb-4e86-865e-2f1165705ef1',
     '52c9537e-ed8d-445a-bf97-237209f77885',
     'e5da38bb-190a-4ab5-8804-ebc0e5bbd50e',
     '7d3a6e6a-20f2-4bd5-9fc1-0f869253d054',
     '33e09bf5-fde9-4191-a6b9-dc4ea5344495',
     '459c4976-b5f6-48ce-b2a1-c0d4d2802d78',
     'a6575ab3-43f0-4773-9896-bbde2caed104',
     'da1207ff-174c-49d2-a116-ca8af75728dd',
     '8ecefcd3-4004-4543-9381-572dd3d4ad26',
     '0b7ef4f3-ee74-499d-a557-0a2a6af9d542')



Trouble shooting: Save server doesn’t save images
-------------------------------------------------

If the save server cannot save images, we can still get them using the
helper function ``process_and_save``. In the following examples, we save
the latest run (``-1``) in the database ``db`` in the file
``./my_image.tiff``. The data key of the image is ``pe1_image``. Before
the data is saved, the dark subtraction is automatically done.

.. code:: ipython3

    process_and_save(db, -1, tiff_path="./my_image.tiff", data_key="pe1_image")

We can also use the uid to specify which run we would like to save.

.. code:: ipython3

    process_and_save(db, "b215aed6-3aed-49d8-9bd0-40143bd3a9ac", tiff_path="./my_image.tiff", data_key="pe1_image")
