"""
Quest model - Represents missions/tasks in the system.
"""
from sqlalchemy import Column, String, Float, Integer, Text, CheckConstraint
from sqlalchemy.orm import relationship

from database.base import BaseModel


class QuestModel(BaseModel):
    """
    Quest entity representing missions/tasks.
    
    Attributes:
        name: Quest name
        stat_name: Associated stat (Strength, Agility, etc.)
        difficulty: Quest difficulty level (DAILY, EASY, NORMAL, HARD, EPIC, LEGENDARY)
        exp_reward: Experience points reward
        gold_reward: Gold reward
        description: Quest description
        quest_logs: Relationship to QuestLogModel (one-to-many)
    """
    __tablename__ = "quests"
    
    name = Column(String(200), nullable=False)
    stat_name = Column(String(50), nullable=False, index=True)
    difficulty = Column(String(20), nullable=False, index=True)
    exp_reward = Column(Float, nullable=False)
    gold_reward = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    
    # Relationship
    quest_logs = relationship(
        "QuestLogModel",
        back_populates="quest",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    # Constraints
    __table_args__ = (
        CheckConstraint('exp_reward > 0', name='chk_exp_positive'),
        CheckConstraint('gold_reward >= 0', name='chk_gold_non_negative'),
    )
    
    def __repr__(self):
        return f"<Quest(id={self.id}, name={self.name}, difficulty={self.difficulty}, stat={self.stat_name})>"