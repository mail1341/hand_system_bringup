from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hand_angle_node',
            executable='hand_angle_node',
            name='hand_angle_node',
            output='screen',
        ),

        #Node(
         #   package='hand_music',
          ## name='hand_music_node',
            #output='screen',
            #parameters=[
            #    {'topic_in': '/hand_norm'},
            #    {'freq_min': 50.0},
            #    {'freq_max': 600.0},
            #    {'wave_type': 'square'},
            #    {'volume': 0.5},
            #    {'chunk_dur': 0.04},
            #],
        #),

        Node(
            package='epos_control',
            executable='epos_control_node',
            name='epos_control_node',
            output='screen',
        ),

        Node(
            package='arduino_slider',
            executable='slider_node',
            name='slider_node',
            output='screen',
            parameters=[
                {'use_binary': False},
                {'port': '/dev/ttyACM0'},
                {'publish_rate_hz': 100.0},
                {'smoothing_alpha': 0.1},
            ],
        ),
    ])