"""
Stat module

Defines individual statistics with XP-based leveling.
"""

from utils.level_constants import XP_THRESHOLDS

class Stat:
    """Represents an individual player statistic (Strength, Agility, etc.)."""

    def __init__(self, name: str, total_xp: int) -> None:
        """Initialize a stat with name and total XP accumulated.
        
        Args:
            name: Name of the stat (e.g., 'Strenght', 'Agility')
            total_xp: Total experience points accumulated
        """
        self.name = name
        self.total_xp = total_xp

    def get_level(self) -> int:
        """Calculate current level based on total XP accumulated."""
        level: int = 1
        for i in range(len(XP_THRESHOLDS)):
            if self.total_xp >= XP_THRESHOLDS[i]:
                level = i + 1
            else:
                break
        return level
            
    def xp_for_next_level(self) -> int:
        """Calculate XP needed to reach next level.
        
        Returns:
            XP needed for next level, or 0 if at max level
        """

        current_level = self.get_level()
        if current_level >= len(XP_THRESHOLDS):
            return 0
        next_level_threshold = XP_THRESHOLDS[current_level]
        xp_needed = next_level_threshold - self.total_xp
        return xp_needed    

    def add_exp(self, exp: int) -> str:
        """Add experience points and detect level-ups.
        
        Args:
            exp: Amount of XP to add
            
        Returns:
            Message describing XP gain and level changes
        """
        if exp <= 0:
            return 'Cannot add negative or zero XP'
        
        level_before = self.get_level()
        self.total_xp += exp
        level_after = self.get_level()

        if level_after == level_before:
            return (f'XP gained: {exp} | Total XP: {self.total_xp} | '
                   f'XP to next level: {self.xp_for_next_level()}')
        
        else: 
            return f'XP gained: {exp} - Level Up! {level_before} -> {level_after}'