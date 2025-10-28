from entities.quest import Quest
from entities.quest_difficulty import QuestDifficulty
import os
import json

class QuestRepository:
    def __init__(self, filepath: str = "data/quests.json") -> None:
        self.filepath = filepath
        self._ensure_data_directory()

    # Private methods
    def _ensure_data_directory(self):
        """Ensure that the directory for the data file exists."""
        dir_path = os.path.dirname(self.filepath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def _quest_to_dict(self, quest: Quest) -> dict:
        """Convert a Quest object to a dictionary for JSON serialization.

        Args:
            quest (Quest): The Quest object to convert.
        Returns:
            dict: A dictionary representation of the Quest.
        """
        # 1. Create the dictionary with simple data types
        data = {
            "id": quest.id,
            "name": quest.name,
            "stat": quest.stat,
            "difficulty": quest.difficulty.value,
            "xp_reward": quest.xp_reward,
            "gold_reward": quest.gold_reward,
            "description": quest.description
        }
        
        return data

    def _dict_to_quest(self, data: dict) -> Quest:
        """Convert a dictionary to a Quest object.
        
        Args:
            data (dict): The dictionary containing quest data.
        Returns:
            Quest: The constructed Quest object.
        """

        id = data["id"]
        name = data["name"]
        stat = data["stat"]
        difficulty = QuestDifficulty(data["difficulty"])
        xp_reward = data["xp_reward"]
        gold_reward = data["gold_reward"]
        description = data["description"]

        quest = Quest(name, stat, difficulty, xp_reward, gold_reward, description)

        quest.id = id

        return quest
        
    def _load_all_data(self) -> dict:
        """ Read the RAW JSON and return a dict of all the Quests
        
        Returns:
            dict: A dictionary with quest_id as keys and quest data as values.
        """

        if not os.path.exists(self.filepath):
            return {}
        
        with open(self.filepath, 'r') as file:
            data = json.load(file)

        return data

    def _save_all_data(self, quest_dict: dict) -> None:
        """Write the whole dict to the json
        
        Args:
            quest_dict (dict): A dictionary with quest_id as keys and quest data as values.
        """
        
        with open(self.filepath, 'w') as file:
            json.dump(quest_dict, file, indent = 2)

    # Public methods

    def add(self, quest: Quest) -> None:
        """Add a new quest to the repository.
        
        Args:
            quest (Quest): The Quest object to add.
        """
        data = self._load_all_data()
        quest_dict = self._quest_to_dict(quest)
        data[quest.id] = quest_dict
        self._save_all_data(data)

    def get_by_id(self, quest_id: str) -> Quest | None:
        """Get a quest by its ID. Returns None if not found.
        
        Args:
            quest_id (str): The ID of the quest to retrieve.

        Returns:
            Quest | None: The Quest object if found, None otherwise.
        """

        data = self._load_all_data()
        if quest_id not in data:
            return None
        
        quest_dict = data[quest_id]
        quest = self._dict_to_quest(quest_dict)

        return quest
        
    def get_all(self) -> list[Quest]:
        """Get all quests as a list of Quest objects.
        
        Returns:
            list[Quest]: A list of all Quest objects.
        """
        
        data = self._load_all_data()
        quest_list = [self._dict_to_quest(quest_data) for quest_data in data.values()]
        return quest_list

    def update(self, quest: Quest) -> bool:
        """Update an existing quest. Returns True if found and updated.
        
        Args:
            quest (Quest): The Quest object with updated data.
        Returns:
            bool: True if the quest was found and updated, False otherwise.
        """

        data = self._load_all_data()
        
        if quest.id not in data:
            return False  # Quest no existe
        
        quest_dict = self._quest_to_dict(quest)
        data[quest.id] = quest_dict
        self._save_all_data(data)
        return True

    def delete(self, quest_id: str) -> bool:
        """Delete a quest by its ID. Returns True if found and deleted.
        
        Args:
            quest_id (str): The ID of the quest to delete.
        Returns:
            bool: True if the quest was found and deleted, False otherwise.
        """

        data = self._load_all_data()
        if quest_id not in data:
            return False
        
        del data[quest_id]

        self._save_all_data(data)

        return True
    
    def get_by_stat(self, stat_name: str) -> list[Quest]:
        """Get all quests for a specific stat.
        
        Args:
            stat_name (str): The name of the stat to filter quests by.
        Returns:
            list[Quest]: A list of Quest objects that match the stat.
        """

        all_quests = self.get_all()
        filtered = [q for q in all_quests if q.stat == stat_name]
        return filtered