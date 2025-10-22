"""
Stat module

Defines individual statistics with XP-based leveling.
"""

# XP thresholds for leveling (index corresponds to level - 1)
XP_THRESHOLDS: list[int] = [
    0,      # Level 1
    100, 250, 450, 700, 1000,   # Up to level 5
    1350, 1750, 2200, 2700, 3250,    # Up to level 10
    3850, 4500, 5200, 5950, 6750,    # Up to level 15
    7600, 8500, 9450, 10450, 11500,    # Up to level 20
    12600, 13750, 14950, 16200, 17500,     # Up to level 25
    18850, 20250, 21700, 23200, 24750,    # Up to level 30
    26350, 28000, 29700, 31450, 33250,     # Up to level 35
    35100, 37000, 38950, 40950, 43000,     # Up to level 40
    45100, 47250, 49450, 51700, 54000,     # Up to level 45
    56350, 58750, 61200, 63700, 65000     # Up to level 50
]

class Stat():
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