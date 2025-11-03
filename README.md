## HunterProgressSystem

**HunterProgressSystem** is a gamified habit management system inspired by *Solo Leveling*.  
It represents personal growth as a leveling and experience (XP) mechanic, applying software engineering principles to self-improvement and personal analytics.

---

## Overview

The goal of this project is to build an application capable of recording, calculating, and displaying a user’s progress across multiple areas (Strength, Intelligence, Domain, Faith, etc.) through a system of XP, levels, and progression thresholds.

The system draws inspiration from RPG mechanics and the *Solo Leveling* universe, combining backend development practices and data design to create a scalable engine that will later serve as the foundation for a **full web application** focused on gamified habit tracking.

---

## Tech Stack

- **Language:** Python 3.13.1  
- **Dependencies:** None (uses only standard libraries such as `os` and `json`)  
- **Architecture:** Modular — separation between entities, repositories, utilities, and data

---

## Project Structure

```
HunterProgressSystem/
│
├── data/ # Persistent data and configuration files
├── entities/ # Core entities and domain models (Player, Mission, Stats, etc.)
├── repositories/ # Data management and persistence layer
├── services / # Entities to perform leveling information
├── utils/ # Constants, helpers, and utility modules
│ └── level_constants.py
│ └── valid_stats.py
│
├── test_*.py # Temporary sprint test scripts
└── README.md
```


---

## Core Concepts

- **Gamified Habits:** Daily actions are transformed into XP and levels.  
- **XP Thresholds:** Scalable XP progression system up to level 50.  
- **Modular Architecture:** Clear separation between domain logic (`entities`), data access (`repositories`), and helpers (`utils`).  
- **Scalability:** Designed to evolve into a REST API or full-featured web application.

---

## Current Usage

At this stage, the system can be executed directly with Python to test the core logic of progression and XP calculation.

python test_progress_system.py

⚙️ Current test scripts validate core entities and progression behavior before building the user-facing interface.

| Stage | Description                             | Status           |
| ----- | --------------------------------------- | ---------------- |
| 1️⃣   | Core progression and level system       | ✅ In development |
| 2️⃣   | Persistent repositories (JSON / SQLite) | 🧩 Upcoming      |
| 3️⃣   | REST API or CLI implementation          | ⏳ Planned        |
| 4️⃣   | Web application interface               | 🔮 Future        |


Author

Daniel Amado
High School Teacher, Systems Engineer, Data Analyst and Backend Developer
Passionate about self-improvement, analytics, and building systems that mirror real-life progression.

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project with proper attribution.
