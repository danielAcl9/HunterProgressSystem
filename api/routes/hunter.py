"""Hunter endpoints"""

from fastapi import APIRouter, HTTPException
from repositories.hunter_repository import HunterRepository

router = APIRouter(prefix="/hunter", tags=["Hunter"])

# Initialize Repository
hunter_repo = HunterRepository("data/hunter.json")

@router.get("/profile")
def get_gunter_profile():
    """Get hunter profile with all stats."""
    hunter = hunter_repo.load()

    # Convert stats into a serializable format
    stats_data = {}
    for stat_name, stat in hunter.stats.items():
        stats_data[stat_name] = {
            "name": stat.name,
            "level": stat.get_level(),
            "total_xp": stat.total_xp,
            "xp_for_next_level": stat.xp_for_next_level()
        }

    return {
        "name": hunter.name,
        "global level": hunter.get_global_level(),
        "total_XP": stat.total_xp,
        "gold": hunter.gold,
        "stats": stats_data
    }

@router.put("/profile")
def update_hutner_profile(name: str = None, gold: int = None):
    """Update hunter name or gold (for testing/admin)"""
    hunter = hunter_repo.load()

    # Update fields if included
    if name is not None:
        if not name.strip():
            raise HTTPException(status_code=400, detail="Name cannot be empty.")
        hunter.name = name
    
    if gold is not None:
        if gold < 0:
            raise HTTPException(status_code=400, detail="Gold cannot be negative")
        hunter.gold = gold

    hunter_repo.save(hunter)

    return {
        "message": "Hunter updated succesfully",
        "name": hunter.name,
        "gold": hunter.gold
    }