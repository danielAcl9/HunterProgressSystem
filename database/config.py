"""
Database configuration for PostgreSQL connection.
Environment variables for database credentials.
"""
import os
from typing import Optional


class DatabaseConfig:
    """Database configuration class for PostgreSQL connection."""
    
    def __init__(self):
        self.DB_USER: str = os.getenv("DB_USER", "hunter_user")
        self.DB_PASSWORD: str = os.getenv("DB_PASSWORD", "hunter_password")
        self.DB_HOST: str = os.getenv("DB_HOST", "localhost")
        self.DB_PORT: str = os.getenv("DB_PORT", "5432")
        self.DB_NAME: str = os.getenv("DB_NAME", "hunter_system")
        
        # SQLAlchemy settings
        self.POOL_SIZE: int = int(os.getenv("DB_POOL_SIZE", "5"))
        self.MAX_OVERFLOW: int = int(os.getenv("DB_MAX_OVERFLOW", "10"))
        self.POOL_TIMEOUT: int = int(os.getenv("DB_POOL_TIMEOUT", "30"))
        self.ECHO_SQL: bool = os.getenv("DB_ECHO_SQL", "False").lower() == "true"
    
    @property
    def database_url(self) -> str:
        """
        Generate synchronous SQLAlchemy database URL.
        
        Returns:
            str: PostgreSQL connection string for SQLAlchemy
        """
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    @property
    def async_database_url(self) -> str:
        """
        Generate asynchronous SQLAlchemy database URL.
        
        Returns:
            str: Async PostgreSQL connection string for SQLAlchemy
        """
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    def get_engine_config(self) -> dict:
        """
        Get SQLAlchemy engine configuration.
        
        Returns:
            dict: Engine configuration parameters
        """
        return {
            "pool_size": self.POOL_SIZE,
            "max_overflow": self.MAX_OVERFLOW,
            "pool_timeout": self.POOL_TIMEOUT,
            "echo": self.ECHO_SQL,
            "pool_pre_ping": True,  # Verify connections before using
        }


# Singleton instance
db_config = DatabaseConfig()