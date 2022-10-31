from src.system import System

if __name__ == "__main__":
    system = System()
    a = ""
    while a.lower() != "x":
        print("1: Load Games From JSON File")
        print("2: Save Current Data to JSON File")
        print("3: Add a game")
        print("4: Print Games")
        print("X - Exit")

        a = input("Enter Number of Desired Option:")

        if a == "1":
            system.load_data()
        elif a == "2":
            system.save_data()
        elif a == "3":
            system.add_game()
        elif a == "4":
            system.print_games()
    pass
