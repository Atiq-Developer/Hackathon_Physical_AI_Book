# Code Example Validation Strategy

This document describes the strategy for validating all code examples within the "Physical AI & Humanoid Robotics" textbook to ensure they are runnable, correct, and produce the expected output.

## Objectives

-   All code examples, configurations (URDF, launch files), and scripts are syntactically correct and execute without errors.
-   The output of each code example matches the description and figures provided in the book.
-   The setup instructions (e.g., Docker environment) are sufficient to reproduce the results.

## Methodology

1.  **Automated Testing Environment**:
    -   A dedicated CI/CD pipeline will be established for the book's companion code repository.
    -   This pipeline will use the Docker environment specified in `quickstart.md` to ensure a consistent testing environment.
2.  **Per-Chapter / Per-Module Validation**:
    -   Each chapter's code examples will be organized into a separate directory within the companion repository.
    -   A simple script (e.g., Python `pytest` for `rclpy` nodes, `ros2 launch` commands for simulations) will be provided for each chapter to automatically run its examples.
3.  **Expected Output Verification**:
    -   For code examples with deterministic output (e.g., ROS 2 `info` messages, numerical results), a script will compare the actual output against a predefined expected output (e.g., `golden_output.txt`).
    -   For simulation-based examples, visual inspection (e.g., checking RViz 2 or Isaac Sim screenshots/recordings) will be part of the validation, alongside checking ROS 2 topic data.
4.  **Manual Spot Checks**:
    -   Beyond automated checks, a human reviewer will periodically run a subset of examples from different chapters to catch subtle issues or unexpected behaviors that automated tests might miss.

## Companion Code Repository Structure

The companion code repository will mirror the book's module and chapter structure, making it easy for readers to find and run relevant examples.

```text
/companion-code/
├── module-1-intro-physical-ai/
│   └── foundations_examples/
│       └── ...
├── module-2-ros-2/
│   ├── rclpy_agents_examples/
│   │   ├── talker_node.py
│   │   └── listener_node.py
│   └── urdf_examples/
│       └── ...
├── Dockerfile          # For the reproducible environment
├── README.md           # Instructions for using the code
└── validation_scripts/ # Scripts for automated checks
```

## Checklist for Code Validation (per chapter)

-   [ ] All Python scripts are runnable.
-   [ ] All ROS 2 launch files execute correctly.
-   [ ] All URDF/Xacro models load without errors in simulation.
-   [ ] Code examples produce the expected console output or behavior.
-   [ ] Simulation environments load correctly with robot models.
-   [ ] ROS 2 topics and services are correctly advertised/subscribed to as expected.
