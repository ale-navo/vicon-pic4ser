import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('tf2_vicon'),
        'config',
        'params.yaml'
    )
    print(config)

    return LaunchDescription([
        Node(
            package='tf2_vicon',
            executable='vicon_tf_broadcaster',
            name='vicon_tf_broadcaster',
            parameters=[config],
            output="screen"
        )
    ])