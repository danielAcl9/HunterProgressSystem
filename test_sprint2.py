from services.progression_service import ProgressionService
from repositories.hunter_repository import HunterRepository
from repositories.quest_repository import QuestRepository
from entities.quest import Quest
from entities.quest_difficulty import QuestDifficulty

# Setup
hunter_repo = HunterRepository("data/hunter.json")
quest_repo = QuestRepository("data/quests.json")
service = ProgressionService(hunter_repo, quest_repo)

# Crear quest
quest = Quest("Programar", "Intelligence", QuestDifficulty.HARD, 500, 150, "Code 10 minutes")
quest_repo.add(quest)

# Completar quest
result = service.complete_quest(quest.id)

print(f"Success: {result['success']}")
print(f"Quest: {result['quest_name']}")
print(f"XP gained: {result['xp_gained']}")
print(f"Level: {result['level_before']} → {result['level_after']}")
print(f"Leveled up: {result['leveled_up']}")
print(f"Gold: {result['gold_gained']} (total: {result['total_gold']})")