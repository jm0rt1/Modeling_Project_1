from src.system import System

if __name__ == "__main__":
    system = System()
    a = ""
    while a.lower() != "x":
        print("1: Load Games From JSON File")
        print("2: Load a team's season stats From Snoozel Server")
        print("3: Save Current Data to JSON File")
        print("4: Add a Game Via This Console")
        print("5: Print Games")
        print("6: Print Games by name")

        print("X - Exit")

        a = input("Enter Number of Desired Option:")

        if a == "1":
            system.load_data_from_file()
        elif a == "2":
            system.load_data_from_snoozle_server()
        elif a == "3":
            system.save_data()
        elif a == "4":
            system.add_game()
        elif a == "5":
            system.print_games()
        elif a == "6":
            system.find()
