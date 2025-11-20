"""Pydantic schemas for Hunter endpoints."""

from pydantic import BaseModel, Field
from typing import Dict

class StatSchema(BaseModel):
    """Schema for individual stat."""
    name: str
    level: str
    total_xp: int
    xp_for_next_level: int

class HunterResponse(BaseModel):
    """Schema for returning Hunter Profile"""
    name: str
    global_level: int
    total_xp: int
    gold: int
    stats: Dict[str, StatSchema]

    class Config:
        json_schema_extra= {
            "example": {
                "name": "Andrés",
                "global_level": 5,
                "total_xp": 1250,
                "gold": 320,
                "stats": {
                    "Strength": {
                        "name": "Strength",
                        "level": 6,
                        "total_xp": 750,
                        "xp_for_next_level": 250
                    }
                }
            }
        }

class HunterUpdate(BaseModel):
    """Schema for updating hunter profile."""
    name: str | None = Field(None, min_length = 1, description = "Hunter name (optional)")
    gold: int | None = Field(None, ge = 0, description = "Gold amount (optional, must be greater than 0)")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "New Name",
                "gold": 500
            }
        }