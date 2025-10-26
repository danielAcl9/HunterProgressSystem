from repositories.quest_repository import QuestRepository
from entities.quest import Quest
from entities.quest_difficulty import QuestDifficulty

repo = QuestRepository("data/test_crud.json")

# CREATE
print("=== CREATE ===")
q1 = Quest("Leg Day", "Strength", QuestDifficulty.HARD, 500, 150, "Train legs")
q2 = Quest("Study Python", "Intelligence", QuestDifficulty.NORMAL, 250, 50, "Learn")
repo.add(q1)
repo.add(q2)
print("✓ 2 quests añadidas")

# READ (individual)
print("\n=== READ BY ID ===")
loaded = repo.get_by_id(q1.id)
print(f"Loaded: {loaded.name}")

# READ (all)
print("\n=== READ ALL ===")
all_quests = repo.get_all()
print(f"Total quests: {len(all_quests)}")

# UPDATE
print("\n=== UPDATE ===")
q1.name = "SUPER Leg Day"
success = repo.update(q1)
print(f"Update success: {success}")

updated = repo.get_by_id(q1.id)
print(f"New name: {updated.name}")

# DELETE
print("\n=== DELETE ===")
deleted = repo.delete(q2.id)
print(f"Delete success: {deleted}")

remaining = repo.get_all()
print(f"Remaining quests: {len(remaining)}")