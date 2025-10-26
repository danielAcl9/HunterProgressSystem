# utils/hunter_constants.py

"""
Constants related to levels and experience (XP).
"""

from typing import Final

XP_THRESHOLDS: Final[list[int]] = [
    0,      # Level 1
    100, 250, 450, 700, 1000,   # Up to level 5
    1350, 1750, 2200, 2700, 3250,    # Up to level 10
    3850, 4500, 5200, 5950, 6750,    # Up to level 15
    7600, 8500, 9450, 10450, 11500,    # Up to level 20
    12600, 13750, 14950, 16200, 17500,     # Up to level 25
    18850, 20250, 21700, 23200, 24750,    # Up to level 30
    26350, 28000, 29700, 31450, 33250,     # Up to level 35
    35100, 37000, 38950, 40950, 43000,     # Up to level 40
    45100, 47250, 49450, 51700, 54000,     # Up to level 45
    56350, 58750, 61200, 63700, 65000      # Up to level 50
]
