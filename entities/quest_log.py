"""QuestLog module for the Hunter System.

Records historical completion of quests with rewards earned.
"""

from datetime import datetime

class QuestLog:
    """Represents a historical record of a completed quest.

    Logs the quest ID, timestamp, and rewards earned at completion time.
    """

    def __init__(self, quest_id: str, xp_earned: int, gold_earned: int) -> None:
        """Initialize a quest completion log.
        
        Args:
            quest_id: Unique identifier of the completed quest
            xp_earned: Experience points earned from completion
            gold_earned: Gold earned from completion
        """
        self.quest_id = quest_id
        self.xp_earned = xp_earned
        self.gold_earned = gold_earned
        
        self.completed_at = datetime.now()