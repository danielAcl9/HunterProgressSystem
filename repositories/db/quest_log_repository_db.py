"""
QuestLog repository using PostgreSQL + SQLAlchemy.
"""
from typing import List, Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from database.models import QuestLogModel
from repositories.db.base_repository import BaseRepository


class QuestLogRepositoryDB(BaseRepository[QuestLogModel]):
    """
    QuestLog repository with database persistence.
    Handles quest completion history and analytics.
    """
    
    def __init__(self, session: Session):
        super().__init__(QuestLogModel, session)
    
    def get_by_hunter(self, hunter_id: str, limit: int = 50) -> List[QuestLogModel]:
        """
        Get quest logs for a specific hunter, ordered by most recent.
        
        Args:
            hunter_id: The hunter's ID
            limit: Maximum number of logs to return
            
        Returns:
            List of quest logs
        """
        return self.session.query(QuestLogModel).filter(
            QuestLogModel.hunter_id == hunter_id
        ).order_by(desc(QuestLogModel.completed_at)).limit(limit).all()
    
    def get_by_quest(self, quest_id: str) -> List[QuestLogModel]:
        """
        Get all completion logs for a specific quest.
        
        Args:
            quest_id: The quest's ID
            
        Returns:
            List of completion logs
        """
        return self.session.query(QuestLogModel).filter(
            QuestLogModel.quest_id == quest_id
        ).order_by(desc(QuestLogModel.completed_at)).all()
    
    def get_recent(self, days: int = 7) -> List[QuestLogModel]:
        """
        Get quest logs from the last N days.
        
        Args:
            days: Number of days to look back
            
        Returns:
            List of recent quest logs
        """
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        return self.session.query(QuestLogModel).filter(
            QuestLogModel.completed_at >= cutoff_date
        ).order_by(desc(QuestLogModel.completed_at)).all()
    
    def get_completion_count(self, hunter_id: str) -> int:
        """
        Get total number of quests completed by a hunter.
        
        Args:
            hunter_id: The hunter's ID
            
        Returns:
            Total completion count
        """
        return self.session.query(QuestLogModel).filter(
            QuestLogModel.hunter_id == hunter_id
        ).count()
    
    def get_total_rewards(self, hunter_id: str) -> dict:
        """
        Calculate total XP and gold earned by a hunter.
        
        Args:
            hunter_id: The hunter's ID
            
        Returns:
            Dictionary with total_exp and total_gold
        """
        result = self.session.query(
            func.sum(QuestLogModel.exp_gained).label('total_exp'),
            func.sum(QuestLogModel.gold_gained).label('total_gold')
        ).filter(
            QuestLogModel.hunter_id == hunter_id
        ).first()
        
        return {
            "total_exp": float(result.total_exp or 0),
            "total_gold": int(result.total_gold or 0)
        }
    
    def log_completion(self, quest_id: str, hunter_id: str, 
                      exp_gained: float, gold_gained: int) -> QuestLogModel:
        """
        Create a new quest completion log.
        
        Args:
            quest_id: The completed quest's ID
            hunter_id: The hunter's ID
            exp_gained: Experience gained
            gold_gained: Gold gained
            
        Returns:
            Created QuestLogModel
        """
        log = QuestLogModel(
            quest_id=quest_id,
            hunter_id=hunter_id,
            exp_gained=exp_gained,
            gold_gained=gold_gained,
            completed_at=datetime.utcnow()
        )
        return self.create(log)