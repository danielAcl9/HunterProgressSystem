from entities.quest_difficulty import QuestDifficulty
from repositories.hunter_repository import HunterRepository
from repositories.quest_repository import QuestRepository

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
    def get_difficulty_rewards(difficulty: QuestDifficulty) -> tuple[int, int]:
        """Get XP and gold rewards for a given difficulty level."""
        return ProgressionService.DIFFICULTY_REWARDS[difficulty]

    def __init__(self, hunter_repository: HunterRepository, quest_repository: QuestRepository):
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
    
    # El método más importante de todo
    def complete_quest(self, quest_id: str) -> dict:
        hunter = self.hunter_repo.load()
        quest = self.quest_repo.get_by_id(quest_id)

        if quest is None:
            return {
                "success": False,
                "error": "Quest not found"
            }

        stat = hunter.stats[quest.stat]

        level_before, level_after = self._calculate_level_change(stat, quest.xp_reward)

        hunter.add_gold(quest.gold_reward)

        self.hunter_repo.save(hunter)


        return {
            "success": True,
            "quest_name": quest.name,
            "stat": quest.stat,
            "xp_gained": quest.xp_reward,
            "level_before": level_before,
            "level_after": level_after,
            "leveled_up": level_after > level_before,
            "gold_gained": quest.gold_reward,
            "total_gold": hunter.gold
        }