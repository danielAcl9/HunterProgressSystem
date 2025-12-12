from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import all models and config
import sys
import os

# Add the root directory to the path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from database.config import db_config
from database.base import Base

# Import all the models so Alembic can detect them
from database.models import HunterModel, StatModel, QuestModel, QuestLogModel

# this is the Alembic Config object
config = context.config

# Config the SQLAlchemy URL 
config.set_main_option("sqlalchemy.url", db_config.database_url)

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Alembic target metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    
    # FIX: Crear configuración directamente en lugar de usar get_section
    configuration = {
        "sqlalchemy.url": db_config.database_url,
    }
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()