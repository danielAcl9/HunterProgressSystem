"""Pydantic schemas for QUest Endpoints"""

from typing import List
from pydantic import BaseModel, Field
from enum import Enum

class QuestDifficultyEnum(str, Enum):
    """Quest difficulty levels."""
    DAILY = "DAILY"
    EASY = "EASY"
    NORMAL = "NORMAL"
    HARD = "HARD"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"

class QuestCreate(BaseModel):
    """Schema for creating a quest."""
    name: str = Field(..., min_length = 1, description = "Quest name")
    stat: str = Field(..., description = "Stat type)") 
    difficulty: QuestDifficultyEnum = Field(..., description = "Quest difficulty level")
    xp_reward: int = Field(..., gt = 0, description = "XP reward (must be > 0)")
    gold_reward: int = Field(..., gt = 0, description = "Gold reward (must ne > 0)")
    description: str = Field("", description = "Quest description (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Morning Run",
                "stat": "Agility",
                "difficulty": "EASY",
                "xp_reward": 100,
                "gold_reward": 20,
                "description": "Run 5KM"
            }
        }

class QuestUpdate(BaseModel):
    """Schema for updating a quest."""
    name: str | None = Field(None, min_length = 1, description = "Quest name (optional)")
    stat: str | None = Field(None, description = "Stat type (optional)") 
    difficulty: QuestDifficultyEnum | None = Field(None, description = "Quest difficulty level (optional)")
    xp_reward: int | None = Field(None, gt = 0, description = "XP reward (optional, must be > 0)")
    gold_reward: int | None = Field(None, gt = 0, description = "Gold reward (optional, must be > 0)")
    description: str | None = Field(None, description = "Quest description (optinoal)")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "SUPER Leg Day",
                "xp_reward": 1000
            }
        }

class QuestResponse(BaseModel):
    """Schema for returning a single quest."""
    id: str
    name: str
    stat: str
    difficulty: str
    xp_reward: int
    gold_reward: int
    description: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "abc-123-def-456",
                "name": "Leg Day",
                "stat": "Strength",
                "difficulty": "HARD",
                "xp_reward": 500,
                "gold_reward": 150,
                "description": "Complete leg workout"
            }
        }

class QuestList(BaseModel):
    """Schema for listing multiple quests."""
    total: int
    stat_filter: str | None
    quests: List[QuestResponse]
    
    class Config:
        json_schema_extra = {
            "example": {
                "total": 2,
                "stat_filter": "Strength",
                "quests": [
                    {
                        "id": "abc-123",
                        "name": "Leg Day",
                        "stat": "Strength",
                        "difficulty": "HARD",
                        "xp_reward": 500,
                        "gold_reward": 150,
                        "description": "Train legs"
                    }
                ]
            }
        }