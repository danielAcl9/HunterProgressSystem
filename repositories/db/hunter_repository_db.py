"""
Hunter repository using PostgreSQL + SQLAlchemy.
"""
from typing import Optional
from sqlalchemy.orm import Session

from database.models import HunterModel, StatModel
from repositories.db.base_repository import BaseRepository


class HunterRepositoryDB(BaseRepository[HunterModel]):
    """
    Hunter repository with database persistence.
    Handles hunter profile and associated stats.
    """
    
    def __init__(self, session: Session):
        super().__init__(HunterModel, session)
    
    def get_hunter_profile(self) -> Optional[HunterModel]:
        """
        Get the single hunter profile.
        In this system, there's only one hunter per user.
        """
        return self.session.query(HunterModel).first()
    
    def create_default_hunter(self, name: str = "Hunter") -> HunterModel:
        """
        Create default hunter with all 5 stats initialized at level 1.
        """
        hunter = HunterModel(
            name=name,
            global_level=1,
            global_exp=0,
            gold=0
        )
        
        # Create the 5 default stats
        stat_names = ["Strength", "Agility", "Intelligence", "Spirit", "Domain"]
        for stat_name in stat_names:
            stat = StatModel(
                hunter_id=hunter.id,
                name=stat_name,
                level=1,
                current_exp=0.0,
                total_exp=0.0
            )
            hunter.stats.append(stat)
        
        return self.create(hunter)
    
    def update_hunter_profile(self, name: str = None, gold: int = None) -> Optional[HunterModel]:
        """
        Update hunter profile fields.
        """
        hunter = self.get_hunter_profile()
        if not hunter:
            return None
        
        if name is not None:
            hunter.name = name
        if gold is not None:
            hunter.gold = gold
        
        return self.update(hunter)
    
    def get_stat_by_name(self, stat_name: str) -> Optional[StatModel]:
        """
        Get a specific stat by name for the current hunter.
        """
        hunter = self.get_hunter_profile()
        if not hunter:
            return None
        
        return self.session.query(StatModel).filter(
            StatModel.hunter_id == hunter.id,
            StatModel.name == stat_name
        ).first()