# TODO - Clean Code Review
# [ ] Improve variable naming if needed

"""
Hunter module

Defines charactheristics for the hunters, players or users.
"""

from entities.stats import Stat

# XP thresholds for leveling (index corresponds to level - 1)
XP_THRESHOLDS :list[int] = [
    0,      # Nivel 1
    100, 250, 450, 700, 1000,   # Hasta nivel 5
    1350, 1750, 2200, 2700, 3250,    # Hasta nivel 10
    3850, 4500, 5200, 5950, 6750,    # Hasta nivel 15
    7600, 8500, 9450, 10450, 11500,    # Hasta nivel 20
    12600, 13750, 14950, 16200, 17500,     # Hasta nivel 25
    18850, 20250, 21700, 23200, 24750,    # Hasta nivel 30
    26350, 28000, 29700, 31450, 33250,     # Hasta nivel 35
    35100, 37000, 38950, 40950, 43000,     # Hasta nivel 40
    45100, 47250, 49450, 51700, 54000,     # Hasta nivel 45
    56350, 58750, 61200, 63700, 65000     # Hasta nivel 50
]

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

        stat_names: list[str] = ["Strength", "Agility", "Intelligence", "Spirit", "Domain"]
        self.stats = {}
        for stat_name in stat_names:
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