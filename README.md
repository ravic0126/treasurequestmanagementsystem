# TreasureQuest-Scheduling-Using-Priority-Queues

## Introduction
The **TreasureQuest-Scheduling-Using-Priority-Queues** project is a sophisticated, high-performance scheduling and priority management system inspired by the legendary Straw Hat pirates’ adventures. This Python-based system is designed to organize, schedule, and process treasures using an advanced priority queue mechanism, ensuring optimal treasure handling and efficient resource allocation among crew members.

This repository is tailored for complex, time-sensitive tasks, utilizing heap-based priority queues and a custom scheduling algorithm. It represents a refined solution for handling prioritized jobs with varying arrival times, sizes, and dynamic allocations, serving as a robust foundation for advanced scheduling and load-balancing applications.

## Features
- **Custom Heap Implementation**: Efficient min-heap constructed from scratch to handle scheduling with custom comparison functions.
- **Dynamic Scheduling Policy**: Supports dynamic allocation of treasures to the crewmate with the lowest load, adhering to pre-defined priority rules.
- **Advanced Priority Queue Management**: Efficiently prioritizes tasks based on wait time, processing time, and treasure size.
- **Scalable Design**: Capable of managing extensive sets of tasks with a time complexity optimized for competitive performance.

## System Model
In this system, each crewmate has a **priority queue** for handling assigned treasure. Treasures are processed based on:
1. **Arrival Time**: Treasures have a designated arrival time, after which they become eligible for processing.
2. **Processing Priority**: Calculated as `(Wait Time - Remaining Size)`, where treasures with higher values receive precedence. 
3. **Load Balancing**: New treasures are assigned to the crewmate with the least load to balance processing duties across the team.

The system's core revolves around the `Heap` and `StrawHatTreasury` classes, ensuring optimal task handling and processing order.

## Class Structure

### 1. `Heap` (located in `heap.py`)
   - A custom heap implementation supporting efficient insertion, extraction, and prioritization of treasures based on configurable criteria.
   - **Methods**:
     - `__init__(self, items)`: Initializes the heap with given items, maintaining the min-heap property.
     - `insert(self, item)`: Inserts an item while preserving the heap structure.
     - `extract(self)`: Removes and returns the top item from the heap.
     - `top(self)`: Returns the top item without extraction.

### 2. `StrawHatTreasury` (located in `straw_hat.py`)
   - Core class for managing treasure scheduling and processing.
   - **Methods**:
     - `__init__(self, num_crewmates)`: Initializes the treasure management system with a defined number of crewmates.
     - `add_treasure(self, treasure)`: Adds a new treasure to the system and schedules it for processing.
     - `get_completion_time(self)`: Returns the list of treasures based on their completion times in ascending order of IDs.

