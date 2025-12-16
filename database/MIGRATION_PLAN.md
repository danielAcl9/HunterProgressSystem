## 🗺️ Migration Steps

### Phase 1: Database Models (Sprint 1, Day 1-2) ✅ COMPLETED
- [x] Create `database/models/hunter_model.py`
  - Hunter entity with relationships
  - Stats as separate related table
- [x] Create `database/models/stat_model.py`
  - Individual stat tracking
  - Foreign key to Hunter
- [x] Create `database/models/quest_model.py`
  - Quest catalog
  - Enum for difficulties
- [x] Create `database/models/quest_log_model.py`
  - Quest completion records
  - Foreign keys to Quest and Hunter
- [x] Create `database/models/__init__.py`
  - Export all models

### Phase 2: Database Connection (Sprint 1, Day 2) ✅ COMPLETED
- [x] Implement `database/connection.py`
  - Create SQLAlchemy engine
  - Session factory
  - Context manager for sessions
  - Connection pooling
- [x] Implement `database/base.py`
  - Declarative base
  - Common mixins (Timestamps, UUID)
  - Base query methods

### Phase 3: Migrations Setup (Sprint 1, Day 3) ✅ COMPLETED
- [x] Initialize Alembic
```bash
  alembic init database/migrations
```
- [x] Configure `alembic.ini`
  - Set sqlalchemy.url from config
  - Configure migration path
- [x] Create initial migration
```bash
  alembic revision --autogenerate -m "Initial schema"
```
- [x] Test migration
```bash
  alembic upgrade head
```

### Phase 4: Repository Refactor (Sprint 2, Day 1-2) 🚧 IN PROGRESS
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

### Phase 5: Service Layer Updates (Sprint 2, Day 3) ⏳ PENDING
- [ ] Update `QuestService`
  - Use new DB repositories
  - Add transaction handling
- [ ] Update `ProgressionService`
  - Wrap quest completion in transaction
  - Rollback on errors

### Phase 6: Data Migration Script (Sprint 2, Day 3) ⏳ PENDING
- [ ] Create `database/migrate_data.py`
  - Read existing JSON files
  - Transform to SQLAlchemy models
  - Insert into PostgreSQL
  - Validate data integrity
  - Generate migration report

### Phase 7: Testing (Sprint 3, Day 1-2) ⏳ PENDING
- [ ] Unit tests for models
- [ ] Integration tests for repositories
- [ ] End-to-end tests with real DB
- [ ] Performance benchmarks

### Phase 8: Docker Update (Sprint 3, Day 2) ✅ COMPLETED
- [x] Add PostgreSQL service to `docker-compose.yml`
- [x] Add environment variables
- [x] Add volume for data persistence
- [x] Health checks configured