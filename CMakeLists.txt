cmake_minimum_required(VERSION 2.8.3s)
project(drive_car)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  #Jetson.GPIO
  geometry_msgs
  joy
  sensor_msgs
)

catkin_python_setup()

catkin_package(
 CATKIN_DEPENDS roscpp rospy std_msgs
)

catkin_install_python(PROGRAMS src/drive_car.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
catkin_install_python(PROGRAMS src/initialize.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

# add_executable(drive_car src/drive_car.py)
add_executable(joystick src/joystick.cpp)

# target_link_libraries(drive_car ${catkin_LIBRARIES})
target_link_libraries(joystick ${catkin_LIBRARIES})