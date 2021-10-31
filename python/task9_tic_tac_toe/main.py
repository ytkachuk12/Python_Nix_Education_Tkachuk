"""Tic tac toe game program. Ver 1.0
has log file with history of played games.
has no GUI and no AI minimax"""
import os


import tic_tac_toe
# import gui


def main():
    """Enter in the program. Run user choice.,
    it can be: tic tac toe game, display game history, clear game history and exit """
    while True:
        user_choice = menu()
        # run the game
        if user_choice == "1":
            tic_tac_toe.game()
        # display games history
        elif user_choice == "2":
            display_log_files()
        # clean game history
        elif user_choice == "3":
            clean_log_files()
        # exit
        else:
            print("Заходи еще")
            break


def menu() -> str:
    """Display menu. Player can pick one of the menu paragraph"""
    print("\tTIC TAC TOE")
    print(
        "Играть(нажми 1)\nИстория игр(нажми 2)\nОчистить историю(нажми 3)\nВыйти(нажми 4)"
        )

    while True:
        user_choice = input()
        if user_choice in ("1", "2", "3", "4"):
            break
        print("Выберите нужный пункт меню")
    return user_choice


def display_log_files():
    """print log files"""
    def display_log_file(file_name: str):
        """print log file"""
        print(f"\n{file_name.upper()}\n")
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Error: {OSError.filename} - {OSError.strerror}.")
    display_log_file("matches.log")
    display_log_file("revanche.log")


def clean_log_files():
    """remove log files"""
    def clean_log_file(file):
        """remove log file"""
        # Try to delete the file
        try:
            os.remove(file)
        except OSError:  # if failed, report it back to the user
            print(f"Error: {OSError.filename} - {OSError.strerror}.")
    clean_log_file("matches.log")
    clean_log_file("revanche.log")


if __name__ == "__main__":
    main()
