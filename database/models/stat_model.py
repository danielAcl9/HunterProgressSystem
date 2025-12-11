"""
Stat model - Represents individual player statistics.
"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from database.base import BaseModel


class StatModel(BaseModel):
    """
    Stat entity representing individual statistics (Strength, Agility, etc.).
    
    Attributes:
        hunter_id: Foreign key to hunters table
        name: Stat name (Strength, Agility, Intelligence, Spirit, Domain)
        level: Current level of this stat
        current_exp: Experience in current level
        total_exp: Total accumulated experience
        hunter: Relationship back to HunterModel
    """
    __tablename__ = "stats"
    
    hunter_id = Column(
        String(36), 
        ForeignKey("hunters.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    name = Column(String(50), nullable=False, index=True)
    level = Column(Integer, nullable=False, default=1)
    current_exp = Column(Float, nullable=False, default=0.0)
    total_exp = Column(Float, nullable=False, default=0.0)
    
    # Relationship
    hunter = relationship("HunterModel", back_populates="stats")
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('hunter_id', 'name', name='uq_hunter_stat'),
    )
    
    def __repr__(self):
        return f"<Stat(id={self.id}, name={self.name}, level={self.level}, exp={self.current_exp}/{self.total_exp})>"