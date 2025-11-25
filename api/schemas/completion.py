"""Pydantic schemas for quest completion"""

from pydantic import BaseModel

class RewardSchema(BaseModel):
    """Rewards obtained from quest completion"""
    xp_gained: int
    stat: str
    gold_gained: int

class ProgressionSchema(BaseModel):
    """Progression information after quest completion"""
    level_before: int
    level_after: int
    leveled_up: bool

class HunterStatusSchema(BaseModel):
    """Hunter status after quest completion"""
    total_gold: int

class CompleteQuestResponse(BaseModel):
    """Shema for quest completion response."""
    message: str
    rewards: RewardSchema
    progression: ProgressionSchema
    hunter_status: HunterStatusSchema

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Quest 'Leg Day' completed!",
                "rewards": {
                    "xp_gained": 500,
                    "stat": "Strength",
                    "gold_gained": 150
                },
                "progression": {
                    "level_before": 5,
                    "level_after": 6,
                    "leveled_up": True
                },
                "hunter_status": {
                    "total_gold": 320
                }
            }
        }