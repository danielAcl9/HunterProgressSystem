"""
Hunter module

Defines charactheristics for the hunters, players or users.
"""

from entities.stats import Stat
from utils.level_constants import XP_THRESHOLDS
from utils.valid_stats import VALID_STATS

class Hunter:
    """Represents an individual player called Hunter"""
    def __init__(self, name: str, gold: int = 0) -> None:
        """ Initialize a player with name and gold in zero. 

        Args:
            name: Name or nickname of the player.
            gold: Total gold or monetary unit accumulated      
        """

        self.name = name
        self.gold = gold
        
        self.stats = {}
        for stat_name in VALID_STATS:
            self.stats[stat_name] = Stat(stat_name,  0)
    
    def get_global_level(self) -> int:
        """Calculate the global level of the player based on the sum of the XP accumulated in each stat."""
        total_xp: int = self.get_global_exp()

        for i in range(len(XP_THRESHOLDS)):
            if total_xp >= XP_THRESHOLDS[i]:
                level: int = i + 1
            else:
                break
        return level

    def get_global_exp(self) -> int:
        """Calculate the global level of the player based on the sum of the XP accumulated in each stat.

        Returns:
            The sum of all the XP for each class
        """

        total_xp: int = 0

        for stat in self.stats.values():
            total_xp += stat.total_xp
        return total_xp
    
    def add_gold(self, new_gold: int) -> str:
        """ Add gold to the player gold stat

        Args:
            new_gold: Amount of gold recieved

        Returns:
            A string combining the gold recieved and the total gold after de addition.
        """
        if new_gold <= 0:
            return 'No se puede añadir oro negativo o cero'
        
        else:
            self.gold += new_gold

        return f'Oro ganado: {new_gold}\nOro Total: {self.gold}'
    
    def get_stat(self, name: str) -> Stat | None: 
        """ Get an specific stat by name

        Args:
            name: Name of the stat to return

        Returns:
            Message with the name and data of the stat, or None, if stat does not exist.
        """
        return self.stats.get(name)