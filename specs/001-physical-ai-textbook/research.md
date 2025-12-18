# Research & Decisions

This document records the key technology decisions for the "Physical AI & Humanoid Robotics" textbook, based on the feature specification and project goals.

## Decision: Simulation Environment (Gazebo & NVIDIA Isaac Sim)

**Decision**: The primary simulation environment will be **Gazebo** for foundational physics and ROS 2 integration, supplemented by **NVIDIA Isaac Sim** for advanced perception, synthetic data generation, and sim-to-real workflows. Unity will be mentioned as an alternative but not used for the core curriculum.

**Rationale**:
- **Gazebo**: It is the de-facto standard simulator in the ROS ecosystem, offering tight integration and a massive community. Its focus on robotics-specific sensors and physics makes it ideal for teaching the core principles of the Robotic Nervous System (Module 2) and Digital Twin (Module 3).
- **NVIDIA Isaac Sim**: This tool is critical for teaching modern, AI-driven robotics (Module 4). Its strengths in synthetic data generation, photorealistic rendering, and direct integration with Isaac ROS for perception and navigation are unmatched for the book's learning outcomes. The focus on sim-to-real is a key part of the book's promise.
- **Unity**: While a powerful physics engine, its ROS integration is less mature than Gazebo's. It will be noted as a viable alternative for readers with existing Unity expertise, but teaching two separate simulation workflows would dilute the book's focus.

**Alternatives considered**:
- **Unity**: A popular game engine with strong physics simulation capabilities. Rejected as the primary tool due to weaker out-of-the-box ROS integration compared to Gazebo.
- **Webots**: An open-source robotics simulator. Rejected because it lacks the industry-specific tooling and AI ecosystem provided by the combination of Gazebo and Isaac Sim.

## Decision: Robotics Middleware (ROS 2)

**Decision**: The exclusive robotics middleware used will be **ROS 2 (Robot Operating System 2)**.

**Rationale**:
- **Industry Standard**: ROS 2 is the most widely adopted framework for robotics development in both academia and industry. Teaching ROS 2 provides readers with a skill that is directly transferable to real-world jobs.
- **Ecosystem**: The ROS 2 ecosystem is vast, with pre-existing tools for navigation, manipulation, perception, and simulation that are essential for the book's curriculum (e.g., Nav2).
- **Language Support**: `rclpy` (the ROS 2 Python client library) allows for seamless integration with the Python-based AI/ML ecosystem (e.g., PyTorch, TensorFlow), which is central to the book's later modules.

**Alternatives considered**:
- **Custom Middleware**: Building a custom middleware is out of scope and would not provide readers with a marketable skill.
- **Other Frameworks (e.g., LCM)**: While other frameworks exist, they lack the broad community support and extensive tooling of ROS 2.

## Decision: Robotics AI Stack (NVIDIA Isaac)

**Decision**: The primary robotics AI stack will be **NVIDIA Isaac**.

**Rationale**:
- **Performance**: NVIDIA's stack is GPU-accelerated, providing the performance needed for real-time perception and navigation tasks.
- **Integration**: Isaac Sim and Isaac ROS are designed to work together seamlessly, providing a powerful, integrated toolchain for developing AI-powered robots. This aligns with the book's goal of teaching an end-to-end workflow.
- **State-of-the-Art**: Isaac includes state-of-the-art algorithms for VSLAM (Visual SLAM) and navigation (Nav2 integration), which are key learning outcomes for the book.

**Alternatives considered**:
- **Building from scratch**: Implementing perception and navigation algorithms from scratch is a monumental task and would detract from the book's primary focus on integrating existing AI systems.
- **Other AI Libraries**: While libraries like OpenCV are powerful, they do not offer the same level of simulation integration and end-to-end robotics focus as the NVIDIA Isaac platform. They will be used where appropriate as components within the larger Isaac/ROS 2 architecture.
