from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1) hand_hz_node（例：hand_hz パッケージに console_scripts 登録してある前提）
        Node(
            package='hand_hz',
            executable='hand_hz_node',
            name='hand_hz_node',
            output='screen',
        ),

        # 2) hand_music_node
        Node(
            package='hand_music',
            executable='hand_music_node',
            name='hand_music_node',
            output='screen',
            parameters=[
                {'topic_in': '/hand_norm'},
                {'freq_min': 50.0},
                {'freq_max': 600.0},
                {'wave_type': 'square'},
                {'volume': 0.5},
                {'chunk_dur': 0.04},
            ],
        ),

        # 3) EPOS 制御ノード
        Node(
            package='epos_control',
            executable='epos_control_node',
            name='epos_control_node',
            output='screen',
        ),

        # 4) Arduino スライダノード
        Node(
            package='arduino_slider',
            executable='slider_node',
            name='slider_node',
            output='screen',
            parameters=[
                {'use_binary': False},
                {'port': '/dev/ttyACM0'},
                {'publish_rate_hz': 100.0},
                {'smoothing_alpha': 1.0},
            ],
        ),
    ])
