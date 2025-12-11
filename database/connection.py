"""
SQLAlchemy engine and session management.
"""
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from database.config import db_config
from database.base import Base

#Create engine 
engine = create_engine(
    db_config.database_url,
    **db_config.get_engine_config()
)

# Session factory
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

def init_bd():
    """
    Initialize database - Create all tables.
    ONLY for development / Testing
    For production use Albemic migrations
    """

    Base.metadata.create_all(bind = engine)

def get_db() -> Session:
    """
    Dependency that provides a database session for FastAPI routes.
    
    Usage:
        @app.get("/items")
        def read_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_session():
    """
    Context manager for database session.

    Usage:
        with get_db_session() as db:
            db.query(Item).all()
    """
    db = SessionLocal()
    try: 
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()