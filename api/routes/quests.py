"""Quest endpoints."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from repositories.quest_repository import QuestRepository
from services.quest_service import QuestService

router = APIRouter(prefix="/quests", tags=["Quests"])

quest_repo = QuestRepository("data/quests.json")
quest_service = QuestService(quest_repo)

@router.get("/")
def list_quest(stat: Optional[str] = Query(None, description="Fitler by stat type")):
    """
    List all quests, optionally filtered by stat.
    
    - **stat**: Optional filter by stat name (Strength, Agility, Intelligence, Spirit, Domain)
    """

    if stat: 
        quests = quest_service.list_by_stat(stat)
        if not quests: 
            return {
                "total": 0,
                "stat_filter": stat,
                "quests": []
            }
    else: 
        quests = quest_service.get_all()
    
    quests_data = []
    for quest in quests:
        quests_data.append({
            "id": quest.id,
            "name": quest.name,
            "stat": quest.stat,
            "difficulty": quest.difficulty.name,  # Enum a string
            "xp_reward": quest.xp_reward,
            "gold_reward": quest.gold_reward,
            "description": quest.description
        })
    
    return {
        "total": len(quests_data),
        "stat_filter": stat if stat else None,
        "quests": quests_data
    }


@router.get("/{quest_id}")
def get_quest(quest_id: str):
    """
    Get a specific quest by ID.
    
    - **quest_id**: UUID of the quest
    """
    quest = quest_repo.get_by_id(quest_id)
    
    if not quest:
        raise HTTPException(
            status_code=404,
            detail=f"Quest with ID '{quest_id}' not found"
        )
    
    return {
        "id": quest.id,
        "name": quest.name,
        "stat": quest.stat,
        "difficulty": quest.difficulty.name,
        "xp_reward": quest.xp_reward,
        "gold_reward": quest.gold_reward,
        "description": quest.description
    }