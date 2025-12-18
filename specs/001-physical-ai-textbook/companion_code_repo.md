# Companion Code Repository Structure

This document outlines the planned structure and contents of the companion code repository that will accompany the "Physical AI & Humanoid Robotics" textbook. This repository will host all code examples, launch files, URDF models, and necessary configurations to enable readers to reproduce the book's content.

## Objectives

-   Provide all necessary code examples in a runnable and well-organized manner.
-   Ensure reproducibility by including environment setup (e.g., Dockerfile).
-   Facilitate easy navigation for readers, mirroring the book's module and chapter structure.
-   Include validation scripts for automated testing of code examples.

## Repository Root (`companion-code/`)

-   `Dockerfile`: Defines the Docker image for the reproducible development environment (Ubuntu 22.04, ROS 2 Humble, Gazebo Fortress, NVIDIA Isaac Sim dependencies, Python packages).
-   `docker-compose.yml`: (Optional) For orchestrating multiple containers if needed (e.g., for different ROS 2 nodes).
-   `README.md`: Comprehensive instructions on how to set up the environment, build the workspace, and run all examples.
-   `ros2_ws/`: The ROS 2 workspace containing all custom packages developed for the book.

## ROS 2 Workspace (`companion-code/ros2_ws/src/`)

Each chapter that introduces new ROS 2 code or configurations will have its own package within the ROS 2 workspace.

```text
/companion-code/ros2_ws/src/
├── my_book_common/        # Package for common messages, utilities, custom URDFs/models
│   ├── package.xml
│   ├── CMakeLists.txt
│   └── urdf/
│       └── my_humanoid.urdf
├── module-1-examples/
│   ├── package.xml
│   └── ...
├── module-2-ros-2-examples/
│   ├── package.xml
│   └── my_ros_chapter_package/
│       ├── package.xml
│       ├── setup.py        # Entry points for Python nodes
│       ├── launch/         # ROS 2 launch files
│       │   └── example.launch.py
│       └── my_ros_chapter_package/
│           ├── __init__.py
│           └── talker_node.py
│           └── listener_node.py
├── module-3-digital-twin-examples/
│   ├── package.xml
│   └── my_gazebo_chapter_package/
│       ├── package.xml
│       ├── worlds/
│       │   └── empty_world.world
│       └── models/
│           └── ...
├── module-4-nvidia-isaac-examples/
│   ├── package.xml
│   └── my_isaac_chapter_package/
│       ├── package.xml
│       ├── scripts/      # Python scripts for Isaac Sim Replicator
│       │   └── synthetic_data_gen.py
│       └── launch/
│           └── ...
├── module-5-vla-examples/
│   ├── package.xml
│   └── my_vla_chapter_package/
│       ├── package.xml
│       ├── scripts/
│       │   └── llm_interface_node.py
│       └── ...
└── module-6-capstone-project/
    ├── package.xml
    └── capstone_robot_pkg/
        ├── package.xml
        ├── launch/
        │   └── capstone_launch.py
        ├── scripts/
        │   └── llm_planner.py
        └── ...
```

## Validation & Testing (`companion-code/validation/`)

-   `validation_scripts/`: Python scripts or shell scripts to automatically run all examples and compare outputs against expected results.
-   `expected_outputs/`: Directory containing expected console outputs, log messages, or visual checksums for comparison.

## Conclusion

The companion code repository is designed to be a living resource that provides readers with a robust and reproducible environment to engage with the book's practical content. Its structured organization will facilitate easy learning and experimentation.
