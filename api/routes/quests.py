"""Quest endpoints."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from repositories.quest_repository import QuestRepository
from services.quest_service import QuestService
from services.progression_service import ProgressionService
from repositories.hunter_repository import HunterRepository
from api.schemas.quest import QuestCreate, QuestUpdate, QuestResponse, QuestList 
from api.schemas.completion import CompleteQuestResponse

from api.exceptions import QuestNotFoundException


router = APIRouter(prefix="/quests", tags=["Quests"])

quest_repo = QuestRepository("data/quests.json")
quest_service = QuestService(quest_repo)

hunter_repo = HunterRepository("data/hunter.json")
progression_service = ProgressionService(hunter_repo, quest_repo)

@router.get("/", response_model=QuestList)
def list_quests(stat: Optional[str] = Query(None, description="Filter by stat type")):
    """List all quests, optionally filtered by stat."""
    if stat:
        quests = quest_service.list_by_stat(stat)
    else:
        quests = quest_service.get_all()
    
    # Convertir a QuestResponse
    quests_data = [
        QuestResponse(
            id=quest.id,
            name=quest.name,
            stat=quest.stat,
            difficulty=quest.difficulty.name,
            xp_reward=quest.xp_reward,
            gold_reward=quest.gold_reward,
            description=quest.description
        )
        for quest in quests
    ]
    
    return QuestList(
        total=len(quests_data),
        stat_filter=stat,
        quests=quests_data
    )

@router.get("/{quest_id}", response_model=QuestResponse)
def get_quest(quest_id: str):
    """Get a specific quest by ID."""
    quest = quest_repo.get_by_id(quest_id)
    
    if not quest:
        raise QuestNotFoundException(quest_id)
    
    return QuestResponse(
        id=quest.id,
        name=quest.name,
        stat=quest.stat,
        difficulty=quest.difficulty.name,
        xp_reward=quest.xp_reward,
        gold_reward=quest.gold_reward,
        description=quest.description
    )

@router.post("/", status_code=201)
def create_quest(data: QuestCreate):
    """
    Create a new quest.

    Parameters:    
        - data: QuestCreate schema with quest details

    Returns:
        - message: Success message
        - quest: Created quest object
    """

    from entities.quest_difficulty import QuestDifficulty

    difficuly_enum = QuestDifficulty[data.difficulty.value]
    
    success, message = quest_service.create_quest(
        name = data.name,
        stat_type = data.stat,
        difficulty = difficuly_enum,
        xp_reward = data.xp_reward,
        gold_reward = data.gold_reward,
        description = data.description
    )

    if not success:
        raise HTTPException(status_code = 400, detail = message)
    
    # Return created quest details
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
def update_quest(quest_id: str, data: QuestUpdate):
    """
    Update an existing quest.
    
    Parameters:
        - quest_id: UUID of the quest to update
        - All other fields are optional - only provided fields will be updated

    Returns:
        - message: Success message
        - quest: Updated quest object
    """
    from entities.quest_difficulty import QuestDifficulty

    # Check quest exists
    quest = quest_repo.get_by_id(quest_id)
    if not quest:
        raise HTTPException(status_code = 404, detail = f"Quest with ID '{quest_id} not  found")
    
    # Update provided fields
    if data.name is not None:
        if not data.name.strip():
            raise HTTPException(status_code = 400, detail = "Quest name cannot be empty")
        quest.name = data.name
    
    if data.stat is not None:
        from utils.valid_stats import VALID_STATS
        if data.stat not in VALID_STATS:
            raise HTTPException(
                status_code = 400,
                detail = f"Invalid stat. Must be one of: {', '.join(VALID_STATS)}"
            )
        quest.stat = data.stat

    if data.difficulty is not None:
        quest.difficulty = QuestDifficulty[data.difficulty.value]
        
    if data.xp_reward is not None:
        quest.xp_reward = data.xp_reward
        

    if data.gold_reward is not None:
        quest.gold_reward = data.gold_reward
        
    if data.description is not None:
        quest.description = data.description

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

@router.post("/{quest_id}/complete", response_model=CompleteQuestResponse)
def complete_quest(quest_id: str):
    """Complete a quest and apply rewards to hunter."""
    result = progression_service.complete_quest(quest_id)
    
    if not result["success"]:
        error = result.get("error", "Unknown error")
        if "not found" in error.lower():
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)
        
    from api.schemas.completion import RewardSchema, ProgressionSchema, HunterStatusSchema
    
    return CompleteQuestResponse(
        message = f"Quest '{result['quest_name']}' completed!",
        rewards = RewardSchema(
            xp_gained=result["xp_gained"],
            stat=result["stat"],
            gold_gained=result["gold_gained"]
        ),
        progression = ProgressionSchema(
            level_before=result["level_before"],
            level_after=result["level_after"],
            leveled_up=result["leveled_up"]
        ),
        hunter_status=HunterStatusSchema(
            total_gold=result["total_gold"]
        )
    )