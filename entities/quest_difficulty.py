""" Quest dificulty levels for the Hunter System"""

from enum import Enum

class QuestDifficulty(Enum):
    """ Enumeration of standard quest difficulty """

    DAILY = "Daily"
    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    EPIC = "Epic"
    LEGENDARY = "Legendary"