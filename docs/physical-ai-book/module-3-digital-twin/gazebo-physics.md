# Physics Simulation with Gazebo

Once a robot's physical structure is defined using URDF, the next step in developing Physical AI is to bring it to life in a simulated environment. **Gazebo** is a powerful 3D robotics simulator widely used in the ROS ecosystem. It allows engineers to accurately test algorithms, design robots, and perform training in a safe, repeatable virtual world without needing physical hardware.

## Why Use Gazebo?

-   **High-Fidelity Physics**: Gazebo integrates with physics engines like ODE, Bullet, Simbody, and DART to provide realistic simulations of gravity, friction, collisions, and joint dynamics.
-   **Extensive Sensor Support**: It can simulate a wide range of sensors, including cameras, LiDAR, IMUs, force sensors, and GPS, providing realistic data streams to ROS nodes.
-   **ROS Integration**: Deep integration with ROS (both ROS 1 and ROS 2) means you can use the same ROS interfaces (topics, services) to control simulated robots as you would with real hardware.
-   **Visualisation**: A rich graphical user interface (GUI) allows for real-time visualization of the robot and its environment.
-   **Large Community & Resources**: A vast library of robot models, environments, and tutorials.

## Gazebo Architecture

Gazebo operates with a client-server architecture:

1.  **Gazebo Server (`gzserver`)**: The core physics engine and world simulation. It runs headless (without GUI) and computes all physics, sensor data, and robot movements.
2.  **Gazebo Client (`gzclient`)**: The graphical user interface that connects to `gzserver` to visualize the simulation.
3.  **ROS 2 Gazebo Bridge (`ros_gz_bridge`)**: A crucial component that translates ROS 2 messages to Gazebo messages and vice-versa, allowing ROS 2 nodes to interact with the simulated environment.

## Launching a Robot in Gazebo

To load a URDF-defined robot into Gazebo and connect it to ROS 2, you typically use ROS 2 launch files.

### 1. World File

Gazebo worlds are defined in `.world` files (XML format). These specify the environment (e.g., ground plane, lighting, static objects) and can include robot models.

```xml
<?xml version="1.0" ?>
<sdf version="1.7">
  <world name="empty_world">
    <light name="sun" type="directional">
      <cast_shadows>1</cast_shadows>
      <pose>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 -0.5 -1</direction>
    </light>
    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1.0</mu>
                <mu2>1.0</mu2>
              </ode>
            </friction>
          </surface>
        </collision>
        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.8 0.8 0.8 1</ambient>
            <diffuse>0.8 0.8 0.8 1</diffuse>
            <specular>0.8 0.8 0.8 1</specular>
          </material>
        </visual>
      </link>
    </model>
    <!-- Robot model would be included here or spawned by a ROS node -->
  </world>
</sdf>
```

### 2. ROS 2 Launch File

A Python-based ROS 2 launch file can orchestrate starting `gzserver`, `gzclient`, loading the robot model, and running controller nodes.

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Include the Gazebo launch file
    gazebo_ros_dir = get_package_share_directory('gazebo_ros')
    gazebo_launch_path = os.path.join(gazebo_ros_dir, 'launch', 'gazebo.launch.py')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_path),
        launch_arguments={'gazebo_model_path': os.path.join(get_package_share_directory('my_robot_description'), 'models')}.items(),
    )

    # Spawn the robot entity
    entity_name = "my_humanoid_robot"
    robot_description_path = os.path.join(
        get_package_share_directory('my_robot_description'),
        'urdf',
        'my_humanoid.urdf'
    )

    with open(robot_description_path, 'r') as file:
        robot_description = file.read()

    spawn_entity = Node(package='ros_gz_sim', executable='create',
                        arguments=['-name', entity_name,
                                   '-topic', 'robot_description',
                                   '-x', '0', '-y', '0', '-z', '1'],
                        output='screen')

    # Optionally, run a robot state publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}],
    )

    # Bridge for ROS 2 and Gazebo communication
    ros_gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='ros_gz_bridge',
        arguments=[
            '--ros-args', '-p', 'topic_name:=/cmd_vel',
            '-p', 'topic_type:=geometry_msgs/msg/Twist',
            '-p', 'gz_topic_name:=/model/my_humanoid_robot/cmd_vel',
            '-p', 'gz_topic_type:=ignition.msgs.Twist',
            '-p', 'direction:=ros_to_gz'
        ],
        output='screen'
    )


    return LaunchDescription([
        gazebo,
        robot_state_publisher_node,
        spawn_entity,
        ros_gz_bridge_node
    ])

```

To run this launch file:

```bash
ros2 launch my_robot_bringup my_robot_launch.py
```

## Conclusion

Gazebo provides a critical link between URDF robot descriptions and functional ROS 2 applications. By simulating complex physics and sensors, it enables iterative development and testing of Physical AI algorithms before deployment to real hardware. The next chapter will delve deeper into simulating specific sensors within Gazebo.

## Further Reading

-   [Gazebo ROS Documentation](https://gazebosim.org/docs/harmonic/ros_install)
-   [ROS 2 Tutorials: Launching with Gazebo](https://docs.ros.org/en/humble/Tutorials/Intermediate-CLI-Tools/Launching-Arguments.html)
-   [ROS 2 Gazebo Bridge](https://github.com/ros-simulation/ros_gz_bridge)
