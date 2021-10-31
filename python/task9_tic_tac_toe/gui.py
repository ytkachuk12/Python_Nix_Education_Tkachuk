import tkinter as tk

import tic_tac_toe

def menu_window():
    window = tk.Tk()

    window.geometry('800x450')
    window.title("Tic Tac Toe")

    menu = tk.Label(text="МЕНЮ",
                    font=("Arial", 20, "bold"),
                    padx=10,
                    pady=20)
    menu.pack()

    play_game = tk.Button(text="Играть!",
                          # highlightbackground='#708090',
                          width=15,
                          height=2)
    play_game.pack()

    game_log = tk.Button(text="История игр",
                         command="tic_tac_toe.game",
                         width=15,
                         height=2)
    game_log.pack()

    clean_log = tk.Button(text="Очистить историю",
                          width=15,
                          height=2)
    clean_log.pack()

    exit_game = tk.Button(text="Выход",
                          width=15,
                          height=2)
    exit_game.pack()

    window.mainloop()


if __name__ == "__main__":
    menu_window()
