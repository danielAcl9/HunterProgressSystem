"""
SQLAlchemy declarative base and common mixins.
All database models inherit from Base.
"""
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base, declared_attr


# Declarative base for all models
Base = declarative_base()


class TimestampMixin:
    """
    Mixin to add automatic timestamp tracking.
    Adds created_at and updated_at columns to any model.
    """
    
    created_at = Column(
        DateTime, 
        default=datetime.utcnow, 
        nullable=False,
        comment="Timestamp when record was created"
    )
    
    updated_at = Column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow, 
        nullable=False,
        comment="Timestamp when record was last updated"
    )


class UUIDMixin:
    """
    Mixin to add UUID primary key.
    Automatically generates UUID v4 for new records.
    """
    
    @declared_attr
    def id(cls):
        return Column(
            String(36), 
            primary_key=True, 
            default=lambda: str(uuid4()),
            comment="Unique identifier (UUID v4)"
        )


class BaseModel(Base, UUIDMixin, TimestampMixin):
    """
    Abstract base model with UUID primary key and timestamps.
    All domain models should inherit from this.
    """
    __abstract__ = True
    
    def __repr__(self):
        """Generic string representation."""
        return f"<{self.__class__.__name__}(id={self.id})>"