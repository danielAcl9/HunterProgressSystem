from repositories.quest_repository import QuestRepository
from entities.quest import Quest
from entities.quest_difficulty import QuestDifficulty

repo = QuestRepository("data/test_quests.json")

# Crear datos raw
quest1 = Quest("Leg Day", "Strength", QuestDifficulty.HARD, 500, 150, "Train")
quest2 = Quest("Study", "Intelligence", QuestDifficulty.NORMAL, 250, 50, "Read")
quest3 = Quest("Coding", "Domain", QuestDifficulty.DAILY, 50, 15, "Code for 10 min a day")

# Convertir a dicts
dict1 = repo._quest_to_dict(quest1)
dict2 = repo._quest_to_dict(quest2)
dict3 = repo._quest_to_dict(quest3)

# Crear estructura completa
all_quests = {
    quest1.id: dict1,
    quest2.id: dict2,
    quest3.id: dict3
}

# Guardar
repo._save_all_data(all_quests)
print("✓ Guardado")

# Cargar
loaded = repo._load_all_data()
print(f"Quests cargadas: {len(loaded)}")  # 3
print(f"IDs: {list(loaded.keys())}")

#Crear una 4ta quest
quest4 = Quest("Exposición del Erudito", "Intelligence", 
               QuestDifficulty.HARD, 500, 150, 
               "Code something big")


repo.add(quest4)

loaded = repo._load_all_data()
print(f"Quests cargadas: {len(loaded)}")
print(f"IDs: {list(loaded.keys())}")


print( " --------------------------------------")
todo = repo.get_all()
print(f"Total quests obtenidas: {len(todo)}")