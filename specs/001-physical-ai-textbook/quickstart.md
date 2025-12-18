# Quick Start Guide

Welcome to "Physical AI & Humanoid Robotics"! This guide provides the necessary steps to set up your environment and get the most out of this book.

## Who This Book Is For

This book is aimed at three core audiences:
1.  **AI/ML Engineers** looking to apply their skills to robotics.
2.  **Robotics Students** who want to integrate modern AI techniques into their work.
3.  **Graduate-level CS Students** seeking a comprehensive guide for a capstone project.

## Prerequisites

To successfully follow this book, you should have:
- **Intermediate Python Proficiency**: You are comfortable with classes, functions, and basic data structures.
- **Familiarity with Linear Algebra & Probability**: You understand core concepts like vectors, matrices, and basic probability distributions.
- **Linux Fundamentals**: You are comfortable working in a Linux environment and using the command line.

## Environment Setup

All code and simulations in this book are designed to run on **Ubuntu 22.04**. To ensure a consistent and reproducible environment, we strongly recommend using a containerized setup.

**Recommended Setup (Docker):**

1.  **Install Docker**: Follow the official instructions to install Docker on your operating system.
2.  **Provided Dockerfile**: A `Dockerfile` will be provided with the book's companion code repository. This will configure an environment with all the necessary dependencies installed, including:
    - ROS 2 Humble
    - Gazebo Fortress
    - NVIDIA Isaac Sim (requires an NVIDIA GPU and drivers)
    - All necessary Python libraries
3.  **Build and Run**: Instructions will be provided on how to build the Docker image and run the container to launch the development environment.

**Manual Installation (Advanced):**

For users who prefer not to use Docker, detailed installation guides for each core technology can be found at their respective official websites. Be aware that version mismatches can cause significant issues.

## How to Use This Book

Each module builds upon the last. We recommend progressing through the book linearly.

- **Read the Theory**: Start each chapter by reading the theoretical concepts.
- **Run the Examples**: Execute the provided code examples to see the concepts in action.
- **Experiment**: Don't be afraid to modify the code and simulations to deepen your understanding.
- **Complete the Capstone**: The final module will guide you through building a complete project. This is where all the concepts come together.
