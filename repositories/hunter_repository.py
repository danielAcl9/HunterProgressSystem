from entities.hunter import Hunter
import os
import json

class HunterRepository:

    def __init__(self, filepath: str = "data/hunter_profile.json") -> None:
        """Repository for saving and loading Hunter profiles to/from JSON files."""
        self.filepath = filepath
        self._ensure_data_directory()

    def _ensure_data_directory(self) -> None:
        """Ensure the data directory exists before file operations."""
        dir_path = os.path.dirname(self.filepath)

        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
            

    def _hunter_to_dict(self, hunter: Hunter) -> dict:
        """Create a base dictionary with simple data from a Hunter object."""
        data = {
            "name": hunter.name,
            "gold": hunter.gold
        }

        stats_data = {}

        for stat_name, stat_object in hunter.stats.items():
            stats_data[stat_name] = {
                "name": stat_object.name,
                "total_xp": stat_object.total_xp
            }

        data["stats"] = stats_data

        return data
    
    def _dict_to_hunter(self, data: dict) -> Hunter:
        """Convert a dictionary representation of a Hunter back into a Hunter object."""
        name = data["name"]
        gold = data["gold"]

        hunter = Hunter(name)
        hunter.gold = gold

        for stat_name, stat_data in data["stats"].items():
            hunter.stats[stat_name].total_xp = stat_data["total_xp"]
        
        return hunter
    
    def save(self, hunter: Hunter) -> None:
        """Save a Hunter object to a JSON file."""
        data = self._hunter_to_dict(hunter)
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent = 2)

    def load(self) -> Hunter:
        """Load a Hunter object from a JSON file."""
        if not os.path.exists(self.filepath):
            default_hunter = Hunter("Player")
            self.save(default_hunter)
            return default_hunter
        
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            
        hunter = self._dict_to_hunter(data)

        return hunter