from entities.quest import Quest
from entities.quest_difficulty import QuestDifficulty
import os
import json

class QuestRepository:
    def __init__(self, filepath: str = "data/quests.json") -> None:
        self.filepath = filepath
        self._ensure_data_directory()

    # Privados
    def _ensure_data_directory(self):
        dir_path = os.path.dirname(self.filepath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def _quest_to_dict(self, quest: Quest) -> dict:
        # 1. Crear diccionaro base con datos simples
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
        """ Read the RAW JSON and return a dict of all the Quests"""

        if not os.path.exists(self.filepath):
            return {}
        
        with open(self.filepath, 'r') as file:
            data = json.load(file)

        return data

    def _save_all_data(self, quest_dict: dict) -> None:
        """Write the whole dict to the json"""
        
        with open(self.filepath, 'w') as file:
            json.dump(quest_dict, file, indent = 2)

    # # Públicos 

    def add(self, quest: Quest) -> None:
        data = self._load_all_data()
        quest_dict = self._quest_to_dict(quest)

        data[quest.id] = quest_dict

        self._save_all_data(data)

    def get_by_id(self, quest_id: str) -> Quest | None:
        data = self._load_all_data()
        if quest_id not in data:
            return None
        
        quest_dict = data[quest_id]

        quest = self._dict_to_quest(quest_dict)

        return quest
        
    def get_all(self) -> list[Quest]:
        quest_dict = self._load_all_data()

        quest_list = [self._dict_to_quest(data) for data in quest_dict.values()]

        count = 0
        for q in quest_list:
            count += 1
            print(f"{count}. [{q.stat}] {q.name} ({q.difficulty.name})")

        return quest_list

    # def update(self, quest: Quest) -> None:
    #     pass

    def delete(self, quest_id: str) -> bool:
        data = self._load_all_data()
        if quest_id not in data:
            return False
        
        del data[quest_id]

        self._save_all_data(data)

        return True
    
    # def get_by_stat(self, stat_name: str) -> list[Quest] | None:
    #     pass