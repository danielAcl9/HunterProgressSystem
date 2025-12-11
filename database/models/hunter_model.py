"""
Hunter model - Represents the player / user in the system.
"""

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from database.base import Base

class HunterModel(Base):
    """
    Hunter entity representing a player in the system.

    Attributes:
        name (str): Player's name.
        global_level (int): Overall level calculated fromt total XP
        global_exp (int): Total experience across all stats.
        gold (int): Current gold amount
        stats (list): Relationship to StatModel (one-to-many)
        quest_logs: Relationship to QuestLogModel (one-to-many)
    """

    __tablename__ = "hunters"

    name = Column(String(100), nullable=False, index=True, comment="Player's name")
    global_level = Column(Integer, default=1, nullable=False, comment="Overall level calculated from total XP")
    global_exp = Column(Integer, default=0, nullable=False, comment="Total experience across all stats")
    gold = Column(Integer, default=0, nullable=False, comment="Current gold amount")

    #Relationships

    # Defines a one-to-many relationship between HunterModel and StatModel (ORM models)
    stats = relationship(
        "StatModel", 
        back_populates="hunter", 
        cascade="all, delete-orphan", 
        lazy="selectin"
    )

    quest_logs = relationship(
        "QuestLogModel",
        back_populates="hunter",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    # Return a string representation of the Hunter instance
    def __repr__(self):
        return f"<Hunter(id={self.id}, name={self.name}, global_level={self.global_level}, global_exp={self.global_exp}, gold={self.gold})>"