"""Pydantic schemas for QUest Endpoints"""

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