"""
Base repository with common database operations.
"""
from typing import TypeVar, Generic, Type, List, Optional
from sqlalchemy.orm import Session
from database.base import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T]):
    """
    Generic base repository with common CRUD operations.
    All DB repositories should inherit from this.
    """
    
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session
    
    def get_by_id(self, id: str) -> Optional[T]:
        """Get entity by ID."""
        return self.session.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self) -> List[T]:
        """Get all entities."""
        return self.session.query(self.model).all()
    
    def create(self, entity: T) -> T:
        """Create new entity."""
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity
    
    def update(self, entity: T) -> T:
        """Update existing entity."""
        self.session.commit()
        self.session.refresh(entity)
        return entity
    
    def delete(self, id: str) -> bool:
        """Delete entity by ID."""
        entity = self.get_by_id(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return True
        return False
    
    def count(self) -> int:
        """Count total entities."""
        return self.session.query(self.model).count()