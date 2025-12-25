"""
Quest repository using PostgreSQL + SQLAlchemy.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

from database.models import QuestModel
from repositories.db.base_repository import BaseRepository


class QuestRepositoryDB(BaseRepository[QuestModel]):
    """
    Quest repository with database persistence.
    Handles quest CRUD operations and filtering.
    """
    
    def __init__(self, session: Session):
        super().__init__(QuestModel, session)
    
    def get_by_stat(self, stat_name: str) -> List[QuestModel]:
        """
        Get all quests filtered by stat name.
        
        Args:
            stat_name: The stat to filter by (e.g., "Strength")
            
        Returns:
            List of quests for that stat
        """
        return self.session.query(QuestModel).filter(
            QuestModel.stat_name == stat_name
        ).all()
    
    def get_by_difficulty(self, difficulty: str) -> List[QuestModel]:
        """
        Get all quests filtered by difficulty.
        
        Args:
            difficulty: The difficulty level (DAILY, EASY, NORMAL, etc.)
            
        Returns:
            List of quests with that difficulty
        """
        return self.session.query(QuestModel).filter(
            QuestModel.difficulty == difficulty
        ).all()
    
    def search_by_name(self, query: str) -> List[QuestModel]:
        """
        Search quests by name (case-insensitive partial match).
        
        Args:
            query: Search term
            
        Returns:
            List of matching quests
        """
        return self.session.query(QuestModel).filter(
            QuestModel.name.ilike(f"%{query}%")
        ).all()
    
    def get_stats_summary(self) -> dict:
        """
        Get summary statistics about quests.
        
        Returns:
            Dictionary with quest counts by stat and difficulty
        """
        total = self.count()
        
        by_stat = self.session.query(
            QuestModel.stat_name,
            func.count(QuestModel.id)
        ).group_by(QuestModel.stat_name).all()
        
        by_difficulty = self.session.query(
            QuestModel.difficulty,
            func.count(QuestModel.id)
        ).group_by(QuestModel.difficulty).all()
        
        return {
            "total": total,
            "by_stat": {stat: count for stat, count in by_stat},
            "by_difficulty": {diff: count for diff, count in by_difficulty}
        }