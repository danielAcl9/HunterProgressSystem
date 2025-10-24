"""
Sprint 1 Validation Test - Hunter System Entities

Tests integration of all core entities: Stat, Hunter, Quest, QuestLog
"""

from entities.stats import Stat
from entities.hunter import Hunter
from entities.quest_difficulty import QuestDifficulty
from entities.quest import Quest
from entities.quest_log import QuestLog


def test_sprint1():
    """Test complete integration of Sprint 1 entities."""
    
    print("="*50)
    print("SPRINT 1 - VALIDATION TEST")
    print("="*50)
    
    # Test 1: Create Hunter
    print("\n[TEST 1] Creating Hunter...")
    hunter = Hunter("Andrés")
    print(f"✓ Hunter created: {hunter.name}")
    print(f"  - Global Level: {hunter.get_global_level()}")
    print(f"  - Global XP: {hunter.get_global_exp()}")
    print(f"  - Gold: {hunter.gold}")
    
    # Test 2: Check initial stats
    print("\n[TEST 2] Checking initial stats...")
    for stat_name, stat in hunter.stats.items():
        print(f"  - {stat_name}: Level {stat.get_level()}, {stat.total_xp} XP")
    
    # Test 3: Create Quest
    print("\n[TEST 3] Creating Quest...")
    quest = Quest(
        "Leg Day Training",
        "Fuerza",
        QuestDifficulty.HARD,
        500,
        150,
        "Complete intense leg workout"
    )
    print(f"✓ Quest created: {quest.name}")
    print(f"  - Difficulty: {quest.difficulty.value}")
    print(f"  - Rewards: {quest.xp_reward} XP, {quest.gold_reward} gold")
    print(f"  - ID: {quest.id}")
    
    # Test 4: Complete Quest (manually simulate)
    print("\n[TEST 4] Completing Quest...")
    
    # Add XP to Fuerza stat
    result = hunter.stats["Fuerza"].add_exp(quest.xp_reward)
    print(f"✓ XP added to Fuerza: {result}")
    
    # Add gold to Hunter
    gold_result = hunter.add_gold(quest.gold_reward)
    print(f"✓ Gold added: {gold_result}")
    
    # Test 5: Create QuestLog
    print("\n[TEST 5] Creating QuestLog...")
    log = QuestLog(quest.id, quest.xp_reward, quest.gold_reward)
    print(f"✓ QuestLog created")
    print(f"  - Quest ID: {log.quest_id}")
    print(f"  - Completed at: {log.completed_at}")
    print(f"  - XP earned: {log.xp_earned}")
    print(f"  - Gold earned: {log.gold_earned}")
    
    # Test 6: Check updated stats
    print("\n[TEST 6] Checking updated stats...")
    print(f"  - Fuerza: Level {hunter.stats['Fuerza'].get_level()}, "
          f"{hunter.stats['Fuerza'].total_xp} XP, "
          f"{hunter.stats['Fuerza'].xp_for_next_level()} XP to next level")
    print(f"  - Global Level: {hunter.get_global_level()}")
    print(f"  - Global XP: {hunter.get_global_exp()}")
    print(f"  - Gold: {hunter.gold}")
    
    # Test 7: Multiple level-ups
    print("\n[TEST 7] Testing multiple level-ups...")
    epic_quest = Quest(
        "Epic Challenge",
        "Inteligencia",
        QuestDifficulty.EPIC,
        1000,
        400,
        "Complete epic learning challenge"
    )
    result = hunter.stats["Inteligencia"].add_exp(epic_quest.xp_reward)
    print(f"✓ {result}")
    print(f"  - New Global Level: {hunter.get_global_level()}")
    print(f"  - New Global XP: {hunter.get_global_exp()}")
    
    print("\n" + "="*50)
    print("✅ SPRINT 1 VALIDATION COMPLETE")
    print("="*50)


if __name__ == "__main__":
    test_sprint1()