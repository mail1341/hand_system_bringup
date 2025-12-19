from setuptools import setup

package_name = 'hand_system_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        # launch ファイルをインストール
        (
            'share/' + package_name + '/launch',
            ['launch/hand_system.launch.py']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='staff@syblab.org',
    description='Bringup launch for hand angle + EPOS + slider system',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # このパッケージは launch 専用なので何もなしでOK
        ],
    },
)

