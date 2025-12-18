# Data Model (Glossary of Terms)

This document defines the core entities and concepts for the "Physical AI & Humanoid Robotics" textbook. It serves as a canonical glossary to ensure consistency throughout the book.

## Content Entities

- **Textbook**: The complete collection of all modules, forming the final instructional book.
  - **Attributes**: Title, Target Audience, Primary Focus.

- **Module**: A top-level division of the book, dedicated to a major subject area. There are 6 core modules.
  - **Attributes**: Title, Learning Objectives.
  - **Relationships**: Contains one or more Chapters.

- **Chapter**: A self-contained instructional unit within a Module.
  - **Attributes**: Title, Key Concepts, Summary.
  - **Relationships**: Belongs to one Module. Contains Code Examples and Diagrams.

- **Learning Outcome**: A specific, measurable skill or piece of knowledge a reader will gain.
  - **Attributes**: Description, Verifiable Action.
  - **Relationships**: Associated with a Module and the Textbook as a whole.

- **Code Example**: A runnable snippet of code (Python/`rclpy` or YAML) that demonstrates a concept.
  - **Attributes**: Description, Language, Associated Concept.

- **Diagram**: A textual representation (ASCII or Mermaid) of an architecture, workflow, or concept.
  - **Attributes**: Title, Format, Description.

## Robotics & AI Concepts

- **Physical AI**: The study and development of intelligent agents that can perceive, reason about, and act upon a physical environment, subject to its constraints (e.g., physics, latency).

- **Embodied Intelligence**: A principle of Physical AI stating that intelligence is shaped by and inseparable from the physical form (body) in which it exists.

- **Digital Twin**: A high-fidelity simulation of a physical robot and its environment, used for development, testing, and training AI models before deploying to the real world.

- **Robotic Nervous System (RNS)**: An analogy for the middleware (ROS 2) that connects a robot's sensors, actuators, and computational components, enabling communication and data flow.

- **Vision-Language-Action (VLA)**: A model or system that can process visual and language inputs to generate a sequence of actions for a robot to execute.

- **Sim-to-Real**: The process of transferring AI models, control policies, or entire systems developed in a simulation to a physical robot.

## Technology Stack Entities

- **ROS 2 (Robot Operating System 2)**: The middleware used as the core "nervous system" of the robot, consisting of nodes, topics, services, and actions.

- **Gazebo**: The physics simulator used for core robotics simulation, including dynamics, collisions, and basic sensor models.

- **NVIDIA Isaac Sim**: The advanced simulator used for photorealistic rendering, synthetic data generation, and running GPU-accelerated AI models.

- **NVIDIA Isaac ROS**: A collection of GPU-accelerated ROS 2 packages for common robotics tasks, such as Visual SLAM (VSLAM) and navigation.
