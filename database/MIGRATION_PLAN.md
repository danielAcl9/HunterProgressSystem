# Migration Plan: JSON → PostgreSQL

## 📊 Current State

### Data Storage
- **Format:** JSON files in `data/` directory
- **Files:**
  - `data/hunter_profile.json` - Single hunter profile
  - `data/quests.json` - Quest catalog
  - `data/quest_logs.json` - Completion history

### Repositories
- `HunterRepository` - CRUD for hunter profile
- `QuestRepository` - CRUD for quests
- `QuestLogRepository` - CRUD for quest completions

### Limitations
- No relational integrity
- Manual ID management
- No concurrent access control
- Limited query capabilities
- No transaction support

---

## 🎯 Target State

### Database
- **RDBMS:** PostgreSQL 15+
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic

### Benefits
- Relational integrity with foreign keys
- Automatic ID generation (UUID)
- ACID transactions
- Complex queries with joins
- Better performance at scale
- Data validation at DB level

---

## 🗺️ Migration Steps

### Phase 1: Database Models (Sprint 1, Day 1-2)
- [ ] Create `database/models/hunter_model.py`
  - Hunter entity with relationships
  - Stats as separate related table
- [ ] Create `database/models/stat_model.py`
  - Individual stat tracking
  - Foreign key to Hunter
- [ ] Create `database/models/quest_model.py`
  - Quest catalog
  - Enum for difficulties
- [ ] Create `database/models/quest_log_model.py`
  - Quest completion records
  - Foreign keys to Quest and Hunter
- [ ] Create `database/models/__init__.py`
  - Export all models

### Phase 2: Database Connection (Sprint 1, Day 2)
- [ ] Implement `database/connection.py`
  - Create SQLAlchemy engine
  - Session factory
  - Context manager for sessions
  - Connection pooling
- [ ] Implement `database/base.py`
  - Declarative base
  - Common mixins (Timestamps, UUID)
  - Base query methods

### Phase 3: Migrations Setup (Sprint 1, Day 3)
- [ ] Initialize Alembic
```bash
  alembic init database/migrations
```
- [ ] Configure `alembic.ini`
  - Set sqlalchemy.url from config
  - Configure migration path
- [ ] Create initial migration
```bash
  alembic revision --autogenerate -m "Initial schema"
```
- [ ] Test migration
```bash
  alembic upgrade head
  alembic downgrade base
```

### Phase 4: Repository Refactor (Sprint 2, Day 1-2)
- [ ] Create `repositories/db/` folder for new repositories
- [ ] Implement `HunterRepositoryDB`
  - Migrate from JSON to SQLAlchemy queries
  - Keep same interface as `HunterRepository`
  - Add transaction support
- [ ] Implement `QuestRepositoryDB`
  - Migrate CRUD operations
  - Add filtering and pagination
- [ ] Implement `QuestLogRepositoryDB`
  - Migrate logging operations
  - Add analytics queries
- [ ] Keep old JSON repositories as `repositories/json/`
  - For backward compatibility
  - For data export/backup

### Phase 5: Service Layer Updates (Sprint 2, Day 3)
- [ ] Update `QuestService`
  - Use new DB repositories
  - Add transaction handling
- [ ] Update `ProgressionService`
  - Wrap quest completion in transaction
  - Rollback on errors

### Phase 6: Data Migration Script (Sprint 2, Day 3)
- [ ] Create `database/migrate_data.py`
  - Read existing JSON files
  - Transform to SQLAlchemy models
  - Insert into PostgreSQL
  - Validate data integrity
  - Generate migration report

### Phase 7: Testing (Sprint 3, Day 1-2)
- [ ] Unit tests for models
- [ ] Integration tests for repositories
- [ ] End-to-end tests with real DB
- [ ] Performance benchmarks

### Phase 8: Docker Update (Sprint 3, Day 2)
- [ ] Add PostgreSQL service to `docker-compose.yml`
- [ ] Add environment variables
- [ ] Add volume for data persistence
- [ ] Update Dockerfile if needed