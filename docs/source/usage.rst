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
(including the start and the end) will be collected and the exposure
time at each point is ``5`` second. The metadata we would like to record
is ``{"task": "calibration"}`` (optional).

.. code:: ipython3

    plan = multi_calib_scan([pe1c], ns.motor1, 0, 5, ns.motor2, 0, 0.5, num=6, exposure=5, md={"task": "calibration"})
    xrun({}, plan)


.. parsed-literal::

    No calib_map. This is a calibration run.
    INFO: requested exposure time = 5 - > computed exposure time= 5.0
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
    |         1 | 16:25:33.8 |
    +-----------+------------+
    generator count ['76be1c55'] (scan num: 1)


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
    |         1 | 16:25:34.6 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['aac0a589'] (scan num: 2)


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
    |         1 | 16:25:35.4 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['da7b2dcd'] (scan num: 3)


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
    |         1 | 16:25:36.2 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['5e4ac917'] (scan num: 4)


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
    |         1 | 16:25:36.9 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['14fb7c85'] (scan num: 5)


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
    |         1 | 16:25:37.6 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['fda5f4d8'] (scan num: 6)


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
    |         1 | 16:25:38.4 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['b215aed6'] (scan num: 7)






.. parsed-literal::

    ('76be1c55-5747-4937-8787-4389ec1458a8',
     'aac0a589-6bc4-48db-a5c2-1c89f509a5bb',
     'da7b2dcd-bb00-4936-8c80-3496587483e6',
     '5e4ac917-8e74-4c7f-b515-752a6cb66d70',
     '14fb7c85-310c-4e78-9ec2-517a9f2ed06a',
     'fda5f4d8-38b8-41e5-943a-dafeaf920090',
     'b215aed6-3aed-49d8-9bd0-40143bd3a9ac')



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
    ├── calib_5.poni
    └── calib_6.poni

    0 directories, 7 files


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
(including the start and the end) will be collected and the exposure
time at each point is ``5`` second. The metadata we would like to record
is ``{"task": "day time scan"}`` (optional). At each point ``i``, the
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
    |         1 | 16:06:24.6 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['d3c31d01'] (scan num: 27)


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
    |         1 | 16:06:25.4 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['fccd113a'] (scan num: 28)


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
    |         1 | 16:06:26.1 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['f7ad28cb'] (scan num: 29)


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
    |         1 | 16:06:26.9 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['d793caea'] (scan num: 30)


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
    |         1 | 16:06:27.7 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['5df9fa0f'] (scan num: 31)


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
    |         1 | 16:06:28.5 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['e973d11b'] (scan num: 32)


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
    |         1 | 16:06:29.2 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['462ff175'] (scan num: 33)


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
    |         1 | 16:06:30.0 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['3d117a51'] (scan num: 34)


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
    |         1 | 16:06:30.8 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['8cfc1bd4'] (scan num: 35)


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
    |         1 | 16:06:31.6 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['3ba5cfe0'] (scan num: 36)


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
    |         1 | 16:06:32.3 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['9895f1fd'] (scan num: 37)


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
    |         1 | 16:06:33.1 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['03eebeea'] (scan num: 38)


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
    |         1 | 16:06:33.9 |      0.000 |           0.000 |      0.000 |           0.000 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['b76a9a95'] (scan num: 39)


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
    |         1 | 16:06:34.7 |      1.000 |           1.000 |      0.100 |           0.100 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['bf648a83'] (scan num: 40)


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
    |         1 | 16:06:35.5 |      2.000 |           2.000 |      0.200 |           0.200 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['992e33a5'] (scan num: 41)


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
    |         1 | 16:06:36.3 |      3.000 |           3.000 |      0.300 |           0.300 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['98fdc7d1'] (scan num: 42)


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
    |         1 | 16:06:37.0 |      4.000 |           4.000 |      0.400 |           0.400 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['4f066e6d'] (scan num: 43)


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
    |         1 | 16:06:37.8 |      5.000 |           5.000 |      0.500 |           0.500 |
    +-----------+------------+------------+-----------------+------------+-----------------+
    generator count ['3df41ca3'] (scan num: 44)






.. parsed-literal::

    ('d3c31d01-d844-4b38-b28d-37873770f924',
     'fccd113a-0500-42ca-82c6-67d355d763e4',
     'f7ad28cb-0384-4924-be6c-779974fbb54b',
     'd793caea-efdd-45c1-a9af-f42b663cb936',
     '5df9fa0f-a466-4846-982a-f6c6d3d7a127',
     'e973d11b-1951-4f1e-9e4d-a17b9d67ca1d',
     '462ff175-884d-43b4-82be-b7159e976636',
     '3d117a51-9b9b-46c8-9efb-38b833c378ac',
     '8cfc1bd4-f98b-45d3-af0d-755900c3bbe1',
     '3ba5cfe0-0388-4d55-a242-3d9c1f0e017f',
     '9895f1fd-7560-479f-b9c9-ef0e38fcc8ad',
     '03eebeea-e84a-48a8-8baa-1e59f6b865d5',
     'b76a9a95-e36b-4067-b1aa-120f1b364c04',
     'bf648a83-b636-4df9-a3c3-68145cb8de2b',
     '992e33a5-27ae-4ed1-bff1-a53c7345403b',
     '98fdc7d1-610a-47d6-9866-ef5c30a52c1c',
     '4f066e6d-8bef-436a-a49d-11d026dfd662',
     '3df41ca3-3ad0-4067-bf2e-530da87bf530')



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
