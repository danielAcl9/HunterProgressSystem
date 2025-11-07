import os
from repositories.hunter_repository import HunterRepository
from repositories.quest_repository import QuestRepository
from services.quest_service import QuestService
from services.progression_service import ProgressionService

class CLI:
    def __init__(self) -> None:
        """Initialize the CLI with repositories and services."""

        self.hunter_repo = HunterRepository("data/hunter.json")
        self.quest_repo = QuestRepository("data/quests.json")
        self.quest_service = QuestService(self.quest_repo)
        self.progression_service = ProgressionService(self.hunter_repo, self.quest_repo)
        self.hunter = self.hunter_repo.load()

    def run(self):
        """Run the main loop of the CLI."""
        # Main Loop
        while True:
            choice = self.show_main_menu()

            if choice == '1':
                self.show_profile()
            elif choice == '2':
                self.manage_quests()
            elif choice == '3':
                self.complete_quests()
            elif choice == '4':
                print("Exiting the Hunter System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            self.pause()

    # Menus
    def show_main_menu(self):
        """Display the main menu and return the user's choice."""

        self.clear_screen()
        print("=== Main Menu - Hunter System ===")
        print("1. View Hunter Profile")
        print("2. Manange Quests")
        print("3. Complete Quests")
        print("4. Exit")
        print("===================================")
        choice = input("Select an option: ")
        return choice

    def show_profile(self):
        """Display hunter profile."""
        self.clear_screen()
        
        # Header
        print("=" * 50)
        print("         HUNTER PROFILE".center(50))
        print("=" * 50)
        
        # Hunter info
        print(f"\nName: {self.hunter.name}")
        print(f"Global Level: {self.hunter.get_global_level()}")
        print(f"Total XP: {self.hunter.get_global_exp():,}")
        print(f"Gold: {self.hunter.gold:,}")
        
        # Stats header
        print("\n" + "=" * 50)
        print("         STATISTICS".center(50))
        print("=" * 50)
        print()
        
        # Stats list
        for stat_name, stat in self.hunter.stats.items():
            current_xp = stat.total_xp
            next_level_xp = stat.xp_for_next_level()
            total_needed = current_xp + next_level_xp
            
            print(f"{stat_name:12} : Level {stat.get_level()}  ({current_xp}/{total_needed} XP)")
        
        print("\n" + "=" * 50)
        
    def manage_quests(self):
        print("TODO: Manage quests")
        
    def complete_quests(self):
        print("TODO: Complete quests")

    # Helpers

    def clear_screen(self):
        """Clear the console screen."""
        
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        """Pause the execution and wait for user input."""
        input("\nPress enter to continue...")