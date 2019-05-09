from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            node_name='rplidarNode',
            package='rplidar_ros',
            node_executable='rplidarNode',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 115200,
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
            }],
        ),
        Node(
            node_name='rplidarNodeClient',
            package='rplidar_ros',
            node_executable='rplidarNodeClient',
            output='screen',
        ),
    ])
