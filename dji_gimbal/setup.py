## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
  packages=['dji_gimbal'],
  package_dir={'': 'src'},
  requires=['std_msgs', 'rospy', 'sensor_msgs', 'dji_sdk']
)

setup(**setup_args)