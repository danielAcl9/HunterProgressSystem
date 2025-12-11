"""
QuestLog model - Represents completed quest history.
"""
from sqlalchemy import Column, String, Float, Integer, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import BaseModel


class QuestLogModel(BaseModel):
    """
    QuestLog entity representing quest completion records.
    
    Attributes:
        quest_id: Foreign key to quests table
        hunter_id: Foreign key to hunters table
        completed_at: Timestamp of completion
        exp_gained: Experience gained from this completion
        gold_gained: Gold gained from this completion
        quest: Relationship to QuestModel
        hunter: Relationship to HunterModel
    """
    __tablename__ = "quest_logs"
    
    quest_id = Column(
        String(36),
        ForeignKey("quests.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    hunter_id = Column(
        String(36),
        ForeignKey("hunters.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    completed_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        index=True
    )
    
    exp_gained = Column(Float, nullable=False)
    gold_gained = Column(Integer, nullable=False)
    
    # Relationships
    quest = relationship("QuestModel", back_populates="quest_logs")
    hunter = relationship("HunterModel", back_populates="quest_logs")
    
    # Constraints
    __table_args__ = (
        CheckConstraint('exp_gained > 0', name='chk_exp_gained_positive'),
        CheckConstraint('gold_gained >= 0', name='chk_gold_gained_non_negative'),
    )
    
    def __repr__(self):
        return f"<QuestLog(id={self.id}, quest_id={self.quest_id}, hunter_id={self.hunter_id}, completed_at={self.completed_at})>"