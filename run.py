from src.system import System

if __name__ == "__main__":
    system = System()
    a = ""
    while a.lower() != "x":
        print("1: Load Games From JSON File")
        print("2: Load a Team's Season Stats From Snoozel Server")
        print("3: Save Current Data to JSON File")
        print("4: Add a Game Via This Console")
        print("5: Print Games")
        print("6: Print Games by Name")
        print("7: Get a Team's Season Record From Snoozel Server")

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
        elif a == "7":
            system.get_team_record()
