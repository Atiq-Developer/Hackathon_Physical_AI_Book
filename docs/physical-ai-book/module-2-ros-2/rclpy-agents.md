# Python Agents with rclpy

`rclpy` is the Python client library for ROS 2, enabling developers to write ROS 2 nodes, publishers, subscribers, services, and actions using familiar Python syntax. This chapter will guide you through creating basic ROS 2 components with `rclpy`.

## Setting up Your Python Environment

Before writing any `rclpy` code, ensure your ROS 2 environment is sourced. This typically involves:

```bash
source /opt/ros/humble/setup.bash
```

It's highly recommended to use a Python virtual environment to manage dependencies for your ROS 2 packages.

```bash
python3 -m venv ~/ros2_ws/src/my_package/venv
source ~/ros2_ws/src/my_package/venv/bin/activate
pip install -U pip setuptools
pip install ros-humble-rclpy ros-humble-std-msgs # Install necessary ROS 2 Python packages
```

## Creating a Publisher Node

A publisher node sends messages to a topic. Let's create a simple "talker" node that publishes "Hello, ROS 2!" messages.

```python
# my_package/my_package/talker_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher') # Node name
        self.publisher_ = self.create_publisher(String, 'chatter', 10) # Topic name, QoS history depth
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS 2! {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args) # Initialize rclpy
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher) # Keep node alive until Ctrl+C
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## Creating a Subscriber Node

A subscriber node receives messages from a topic. Let's create a "listener" node that prints received messages.

```python
# my_package/my_package/listener_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):

    def __init__(self):
        super().__init__('simple_subscriber') # Node name
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10) # Topic name, QoS history depth
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## Creating a ROS 2 Package

To run these nodes within ROS 2, you need to create a package.

1.  **Create a workspace and package**:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ros2 pkg create --build-type ament_python my_package
    ```
2.  **Copy Python files**: Place `talker_node.py` and `listener_node.py` into `~/ros2_ws/src/my_package/my_package/`.
3.  **Update `setup.py`**: Add entry points to make your Python scripts executable as ROS 2 nodes.
    ```python
    # ~/ros2_ws/src/my_package/setup.py
    from setuptools import find_packages, setup

    package_name = 'my_package'

    setup(
        name=package_name,
        version='0.0.0',
        packages=find_packages(exclude=['test']),
        data_files=[
            ('share/' + package_name, ['package.xml']),
            ('share/' + package_name + '/launch', ['launch/simple_nodes.launch.py']), # Example launch file
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer='your_name',
        maintainer_email='you@example.com',
        description='TODO: Package description',
        license='TODO: License declaration',
        tests_require=['pytest'],
        entry_points={
            'console_scripts': [
                'talker = my_package.talker_node:main',
                'listener = my_package.listener_node:main',
            ],
        },
    )
    ```
4.  **Build your package**:
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select my_package
    ```
5.  **Source the workspace**:
    ```bash
    source install/setup.bash
    ```
6.  **Run the nodes**:
    ```bash
    ros2 run my_package talker
    ros2 run my_package listener # In a separate terminal
    ```

## Conclusion

`rclpy` provides a powerful and intuitive way to develop ROS 2 applications using Python. By creating nodes, topics, and packages, you can build complex robotic behaviors. The next chapter will explore how to describe your robot's physical structure using URDF.

## Further Reading

-   [Writing a Simple Publisher and Subscriber (Python)](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Writing-A-Simple-Publisher-And-Subscriber--Python.html)
-   [Creating a ROS 2 Package (Python)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)
