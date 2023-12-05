cmake_minimum_required(VERSION 3.8)
project(vicon_driver)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

include_directories(
  include
  ${Boost_INCLUDE_DIRS}
)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(interfaces REQUIRED)
find_package(Boost REQUIRED COMPONENTS thread)

add_executable(vicon_client src/communicator.cpp src/publisher.cpp)
target_link_libraries(vicon_client ViconDataStreamSDK_CPP ${Boost_LIBRARIES})
ament_target_dependencies(vicon_client "rclcpp" interfaces)

install(TARGETS vicon_client DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME})

ament_package()
