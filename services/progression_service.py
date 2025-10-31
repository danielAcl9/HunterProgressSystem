import stat
from entities.quest_difficulty import QuestDifficulty
from repositories import hunter_repository, quest_repository

class ProgressionService:

    DIFFICULTY_REWARDS = {
        QuestDifficulty.DAILY: (50, 10),
        QuestDifficulty.EASY: (100, 20),
        QuestDifficulty.NORMAL: (250, 50),
        QuestDifficulty.HARD: (500, 150),
        QuestDifficulty.EPIC: (1000, 400),
        QuestDifficulty.LEGENDARY: (5000, 1000)
    }

    @staticmethod
    def get_difficulty_rewards(difficulty: QuestDifficulty):
        """Get XP and gold rewards for a given difficulty level."""
        return ProgressionService.DIFFICULTY_REWARDS[difficulty]
    
    def __init__(self, hunter_repository, quest_repository):
        """Initialize ProgressionService with required repositories."""
        self.hunter_repo = hunter_repository
        self.quest_repo = quest_repository  

    def _calculate_level_change(self, stat, xp_to_add: int) -> tuple[int, int]:
        """Calculate level before and after adding XP.
        Returns:
            Tuple of (level_before, level_after)
        """
        level_before = stat.get_level()
        stat.add_exp(xp_to_add)
        level_after = stat.get_level()
        return (level_before, level_after)