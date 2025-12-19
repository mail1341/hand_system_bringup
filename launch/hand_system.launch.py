from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess   # ★これを追加



def generate_launch_description():
    return LaunchDescription([
        # 1) 手の角度ノード（Python スクリプトを直接実行）
        ExecuteProcess(
            cmd=[
                'python3',
                '/home/robot/ros2_ws/src/hand_hz/hand_hz/hand_hz_node.py'
            ],
            output='screen',
        ),


         # 2) 周波数ノード（Python スクリプトを直接実行）
        ExecuteProcess(
            cmd=[
                'python3',
                '/home/robot/ros2_ws/src/hand_music/hand_music/hand_music_node.py'
            ],
            output='screen',
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
                {'use_binary': False},          # Arduino は Serial.println(…) なので ASCII
                {'port': '/dev/ttyACM0'},      # 必要なら /dev/ttyUSB0 などに変更
                {'publish_rate_hz': 100.0},
                {'smoothing_alpha': 1.0},
            ],
        ),


    ])
