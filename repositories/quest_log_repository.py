"""QuestLog Repository for JSON persistence."""

import json
import os
from datetime import datetime
from entities.quest_log import QuestLog

class QuestLogRepository:
    """Handles loading and saving QuestLog data to JSON file."""
    
    def __init__(self, filepath: str = "data/quest_logs.json"):
        """Initialize repository with file path."""
        self.filepath = filepath
        self._ensure_data_directory()
    
    def _ensure_data_directory(self) -> None:
        """Create data directory if it doesn't exist."""
        dir_path = os.path.dirname(self.filepath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
    def add(self, quest_log: QuestLog) -> None:
        """Add a quest log entry."""
        logs = self._load_all()
        
        log_dict = {
            "quest_id": quest_log.quest_id,
            "completed_at": quest_log.completed_at.isoformat(),
            "xp_earned": quest_log.xp_earned,
            "gold_earned": quest_log.gold_earned
        }
        
        logs.append(log_dict)
        self._save_all(logs)
    
    def get_recent(self, n: int = 10) -> list[dict]:
        """Get the N most recent quest logs."""
        logs = self._load_all()
        return logs[-n:]  # Últimos N elementos
    
    def _load_all(self) -> list:
        """Load all quest logs from JSON."""
        if not os.path.exists(self.filepath):
            return []
        
        with open(self.filepath, 'r') as file:
            return json.load(file)
    
    def _save_all(self, logs: list) -> None:
        """Save all quest logs to JSON."""
        with open(self.filepath, 'w') as file:
            json.dump(logs, file, indent=2)