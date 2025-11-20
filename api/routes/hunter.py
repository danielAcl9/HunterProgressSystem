"""Hunter endpoints"""

from fastapi import APIRouter, HTTPException
from repositories.hunter_repository import HunterRepository
from api.schemas.hunter import HunterResponse, HunterUpdate, StatSchema

router = APIRouter(prefix="/hunter", tags=["Hunter"])

# Initialize Repository
hunter_repo = HunterRepository("data/hunter.json")

@router.get("/profile", response_model = HunterResponse)
def get_gunter_profile():
    """Get hunter profile with all stats."""
    hunter = hunter_repo.load()

    # Convert stats into a StatSchema
    stats_data = {}
    for stat_name, stat in hunter.stats.items():
        stats_data[stat_name] = StatSchema(
            name = stat.name,
            level = stat.get_level(),
            total_xp = stat.total_xp,
            xp_for_next_level = stat.xp_for_next_level()
        )

    return HunterResponse(
        name = hunter.name,
        global_level = hunter.get_global_level(),
        total_xp = hunter.get_global_exp(),
        gold = hunter.gold,
        stats = stats_data
    )

@router.put("/profile", response_model = HunterResponse)
def update_hunter_profile(data: HunterUpdate):
    """Update hunter name or gold (for testing/admin)"""
    hunter = hunter_repo.load()

    # Update fields if included
    if data.name is not None:
        hunter.name = data.name

    if data.gold is not None:
        hunter.gold = data.gold

    hunter_repo.save(hunter)

    stats_data = {}
    for stat_name, stat in hunter.stats.items():
        stats_data[stat_name] = StatSchema(
            name = stat.name,
            level = stat.get_level(),
            total_xp = stat.total_xp,
            xp_for_next_level = stat.xp_for_next_level()
        )

    return HunterResponse(
        name = hunter.name,
        global_level = hunter.get_global_level(),
        total_xp = hunter.get_global_exp(),
        gold = hunter.gold,
        stats = stats_data
    )