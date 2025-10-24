""" Quest module for Hunter System

Defines individual quests / missions with rewards and difficulty levels.
"""


import uuid
from entities.quest_dificulty import QuestDifficulty

class Quest:
    """Represents a mission/quest that can be completed for rewards


    Each quest is associated with a specific stat, has a difficulty level, 
    and provides XP and gold rewards when completed. 
    """

    def __init__(self, name: str, stat: str, difficulty: QuestDifficulty,
                 xp_reward: int, gold_reward: int, description: str) -> None:
        """Initialize a quest with rewards and difficulty

        Args:
            name: Name of the quest
            stat: Associated stat type (e.g., 'Fuerza', 'Agilidad')
            difficulty: Difficulty level from QuestDifficulty enum
            xp_reward: Experience points awarded upon completion
            gold_reward: Gold awarded upon completion
            description: Brief description of the quest
        """
        
        self.id = str(uuid.uuid4())
        self.name = name
        self.stat = stat
        self.difficulty = difficulty
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.description = description