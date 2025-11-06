import os
from repositories.hunter_repository import HunterRepository
from repositories.quest_repository import QuestRepository
from services.quest_service import QuestService
from services.progression_service import ProgressionService

class CLI:
    def __init__(self) -> None:
        self.hunter_repo = HunterRepository("data/hunter.json")
        self.quest_repo = QuestRepository("data/quests.json")
        self.quest_service = QuestService(self.quest_repo)
        self.progression_service = ProgressionService(self.hunter_repo, self.quest_repo)
        self.hunter = self.hunter_repo.load()

    def run(self):
        # Loop principal
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

    # Menús
    def show_main_menu(self):
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
        print("TODO: Show profile")
        
    def manage_quests(self):
        print("TODO: Manage quests")
        
    def complete_quests(self):
        print("TODO: Complete quests")

    # Helpers

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("\nPress enter to continue...")