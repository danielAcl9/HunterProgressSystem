"""Quest endpoints."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from repositories.quest_repository import QuestRepository
from services.quest_service import QuestService
from entities.quest_difficulty import QuestDifficulty

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

@router.post("/", status_code=201)
def create_quest(
    name: str,
    stat: str,
    difficuly: str,
    xp_reward: int,
    gold_reward: int,
    description: str = ""):
    """
    Create a new quest.
    
    - name: Quest name
    - stat: Stat type (Strength, Agility, Intelligence, Spirit, Domain)
    - difficulty: Difficulty level (DAILY, EASY, NORMAL, HARD, EPIC, LEGENDARY)
    - xp_reward: XP reward amount
    - gold_reward: Gold reward amount
    - description: Optional quest description
    """

    try:
        difficuly_enum = QuestDifficulty[difficuly.upper()]
    except KeyError:
        raise HTTPException(
            status_code=400,
            detail = f"Invalid difficulty. Must be one of: {[d.name for d in QuestDifficulty]}"
        )
    
    success, message = quest_service.create_quest(
        name = name,
        stat_type = stat,
        difficulty = difficuly_enum,
        xp_reward = xp_reward,
        gold_reward = gold_reward,
        description = description
    )

    if not success:
        raise HTTPException(status_code = 400, detail = message)
    
    quests = quest_service.get_all()
    created_quest = quests[-1]

    return {
        "message": message, 
        "quest": {
            "id": created_quest.id,
            "name": created_quest.name,
            "stat": created_quest.stat,
            "difficulty": created_quest.difficulty.name,
            "xp_reward": created_quest.xp_reward,
            "gold_reward": created_quest.gold_reward,
            "description": created_quest.description
        }
    }

@router.put("/{quest_id}")
def update_quest(quest_id: str,
    name: str = None,
    stat: str = None,
    difficulty: str = None,
    xp_reward: int = None,
    gold_reward: int = None,
    description: str = None
):
    """
    Update an existing quest.
    
    - **quest_id**: UUID of the quest to update
    - All other fields are optional - only provided fields will be updated
    """

    # Check quest exists
    quest = quest_repo.get_by_id(quest_id)
    if not quest:
        raise HTTPException(status_code = 404, detail = f"Quest with ID '{quest_id} not  found")
    
    # Update provided fields
    if name is not None:
        if not name.strip():
            raise HTTPException(status_code = 400, detail = "Quest name cannot be empty")
    
    if stat is not None:
        from utils.valid_stats import VALID_STATS
        if stat not in VALID_STATS:
            raise HTTPException(
                status_code = 400,
                detail = f"Invalid stat. Must be one of: {', '.join(VALID_STATS)}"
            )
        quest.stat = stat

    if difficulty is not None:
        try:
            quest.difficulty = QuestDifficulty[difficulty.upper()]
        except KeyError:
            raise HTTPException(
                status_code = 400, 
                detail = f'Invalid difficulty. Must be one of: {[d.name for d in QuestDifficulty]}'
            )
        
    if xp_reward is not None:
        if xp_reward <= 0:
            raise HTTPException(status_code = 400, detail = "XP reward must be greater than 0")
        quest.xp_reward = xp_reward

    if gold_reward is not None:
        if gold_reward <= 0:
            raise HTTPException(status_code = 400, detail = "Gold reward must be greater than 0")
        quest.gold_reward = gold_reward
        
    if description is not None:
        quest.description = description

    success = quest_repo.update(quest)
    if not success:
        raise HTTPException(status_code = 500, detail = "Failed to update quest")
    
    return {
        "message": "Quest updated successfully",
        "quest": {
            "id": quest.id,
            "name": quest.name,
            "stat": quest.stat,
            "difficulty": quest.difficulty.name,
            "xp_reward": quest.xp_reward,
            "gold_reward": quest.gold_reward,
            "description": quest.description
        }
    }

@router.delete("/{quest_id}", status_code = 204)
def delete_quest(quest_id: str):
    """
    Delete a quest
    
    Parameters:
        - quest_id: UUID of the quest to delete
    """ 

    success = quest_service.delete_quest(quest_id)

    if not success:
        raise HTTPException(status_code = 404, detail = f"Quest wiht id {quest_id} not found")
    
    return None

