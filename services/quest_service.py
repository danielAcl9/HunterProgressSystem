from entities.quest import Quest
from entities.quest_difficulty import QuestDifficulty
from repositories.quest_repository import QuestRepository

from utils.valid_stats import VALID_STATS

class QuestService:
    def __init__(self, quest_repository: QuestRepository) -> None:
        self.quest_repository = quest_repository

    def get_all(self) -> list[Quest]:
        return self.quest_repository.get_all()
    
    def create_quest(self, name: str, stat_type: str, difficulty: QuestDifficulty,
                     xp_reward: int, gold_reward: int, description: str) -> tuple[bool, str]:

        if not name or name.strip() == "":
            return (False, "Quest name cannot be empty")      
        
        if stat_type not in VALID_STATS:
            return (False, "Invalid stat type for quest")
        
        if xp_reward <= 0:
            return (False, "XP reward must be greater than zero")
        
        if gold_reward <= 0:
            return (False, "Gold reward must be greater than zero")
        
        new_quest = Quest(
            name,
            stat_type,
            difficulty,
            xp_reward,
            gold_reward,
            description
        )

        self.quest_repository.add(new_quest)

        return (True, "Quest created successfully")
    
    
    def list_by_stat(self, stat_name: str) -> list[Quest]:
        """List quests filtered by a specific stat name.
        Args:
            stat_name (str): The stat name to filter quests by.
        Returns:
            list[Quest]: A list of Quest objects that match the stat name.
        """

        if stat_name not in VALID_STATS:
            return []
        
        listed_quests = self.quest_repository.get_by_stat(stat_name)
        return listed_quests
    
    def delete_quest(self, quest_id: str) -> bool:
        """Delete a quest by its ID.
        Args:
            quest_id (str): The ID of the quest to delete.
        Returns:
            bool: True if the quest was found and deleted, False otherwise.
        """
        
        return self.quest_repository.delete(quest_id)