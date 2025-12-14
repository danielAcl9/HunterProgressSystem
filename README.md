# HunterProgressSystem

**HunterProgressSystem** is a gamified habit management system inspired by *Solo Leveling*.  
It represents personal growth as a leveling and experience (XP) mechanic, applying software engineering principles to self-improvement and personal analytics.

---

## Overview

The goal of this project is to build an application capable of recording, calculating, and displaying a user's progress across multiple areas (Strength, Agility, Intelligence, Spirit, Domain) through a system of XP, levels, and progression thresholds.

The system draws inspiration from RPG mechanics and the *Solo Leveling* universe, combining backend development practices and data design to create a scalable engine that serves as the foundation for a **full web application** focused on gamified habit tracking.

---

## Tech Stack

- **Language:** Python 3.13.1  
- **Framework:** FastAPI
- **Database:** PostgreSQL 15 + SQLAlchemy ORM
- **Migrations:** Alembic
- **Containerization:** Docker + Docker Compose
- **Architecture:** Modular — separation between entities, repositories, services, API, and database

---

## Project Structure
```
HunterProgressSystem/
│
├── api/                  # FastAPI REST API endpoints
│   ├── routes/           # API route handlers
│   └── schemas/          # Pydantic validation schemas
│
├── data/                 # JSON data files (legacy/backup)
│
├── database/             # PostgreSQL + SQLAlchemy
│   ├── models/           # ORM models (Hunter, Stat, Quest, QuestLog)
│   ├── migrations/       # Alembic migrations
│   ├── base.py           # Base model and mixins
│   ├── config.py         # Database configuration
│   └── connection.py     # Session management
│
├── entities/             # Core domain entities
│
├── repositories/         # Data persistence layer
│
├── services/             # Business logic
│
├── ui/                   # User interface (CLI)
│
├── utils/                # Constants and helpers
│
├── docker-compose.yml    # Docker services configuration
├── Dockerfile            # API container definition
├── requirements.txt      # Python dependencies
├── alembic.ini          # Alembic configuration
├── main.py              # CLI entry point
└── README.md
```

---

## Core Concepts

- **Gamified Habits:** Daily actions are transformed into XP and levels  
- **5 Core Stats:** Strength, Agility, Intelligence, Spirit, Domain  
- **6 Difficulty Levels:** Daily, Easy, Normal, Hard, Epic, Legendary  
- **XP Progression System:** Dynamic leveling with formula-based thresholds  
- **Modular Architecture:** Clean separation of concerns (domain, data, API)  
- **RESTful API:** Complete CRUD operations with FastAPI  
- **Database Persistence:** PostgreSQL with SQLAlchemy ORM

---

## Quick Start

### Prerequisites

- Docker Desktop installed and running
- Git

### Running the Application
```bash
# Clone the repository
git clone https://github.com/danielAcl9/HunterProgressSystem.git
cd HunterProgressSystem

# Start all services (API + PostgreSQL)
docker-compose up -d

# Apply database migrations
docker-compose exec api alembic upgrade head

# Access the API documentation
# Open in browser: http://localhost:8000/docs
```

### API Endpoints

- `GET /hunter/profile` - View hunter profile
- `PUT /hunter/profile` - Update hunter profile
- `GET /quests` - List all quests (filter by stat)
- `POST /quests` - Create new quest
- `PUT /quests/{id}` - Update quest
- `DELETE /quests/{id}` - Delete quest
- `POST /quests/{id}/complete` - Complete a quest

---

## Development Progress

| Stage | Description                                  | Status |
| ----- | -------------------------------------------- | ------ |
| 1️⃣   | Core progression and level system            | ✅ Done |
| 2️⃣   | FastAPI REST API + Dockerization             | ✅ Done |
| 3️⃣   | PostgreSQL + SQLAlchemy ORM + Alembic        | ✅ Done |
| 4️⃣   | Database repositories migration              | 🚧 In Progress |
| 5️⃣   | Testing & optimization                       | ⏳ Planned |
| 6️⃣   | Web application interface                    | 🔮 Future |

---

## Database Schema

### Tables

- **hunters** - Player profiles with global level and stats
- **stats** - Individual statistics (Strength, Agility, etc.)
- **quests** - Mission catalog with rewards
- **quest_logs** - Completion history

See [database/MIGRATION_PLAN.md](database/MIGRATION_PLAN.md) for detailed schema.

---

## Environment Variables

Create a `.env` file:
```env
DB_USER=hunter_user
DB_PASSWORD=hunter_password
DB_HOST=postgres
DB_PORT=5432
DB_NAME=hunter_system
```

---

## Commands Reference
```bash
# Docker
docker-compose up -d              # Start services
docker-compose down               # Stop services
docker-compose logs -f api        # View API logs
docker-compose exec api bash      # Access API container

# Database
docker-compose exec postgres psql -U hunter_user -d hunter_system

# Migrations
docker-compose exec api alembic revision --autogenerate -m "message"
docker-compose exec api alembic upgrade head
docker-compose exec api alembic downgrade -1
```

---

## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project with proper attribution.