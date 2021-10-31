"""
Ver 1. without gui
Tic tac toe game. There are 2 players can play.
Player has name and race(X or O)
"""

from random import randint
from time import sleep

from game_board import init_game_board, print_board
from logger import logger


class Player:
    """Class contains player names and races"""
    def __init__(self, name: str, x_race: str):
        self.name = name
        self.x_race = x_race

    def get_race(self) -> str:
        """get race"""
        return self.x_race

    def set_race(self, x_race: str):
        """set race"""
        self.x_race = x_race


def game(first_player: Player = None, second_player: Player = None, revanche_flag=False):
    """game funk"""
    logger.debug("\t\tGAME START")
    # initialize dict which contains all player moves
    game_board = init_game_board()
    # if its first game between players -> take player names and init player objects
    if not revanche_flag:
        first_name, second_name = input_players_name()
        first_player, second_player = get_random_first_player(first_name, second_name)
    # create object of current player(player who is turning
    player = first_player
    move_count = 1
    while True:
        # display game board, and name of current player
        print_board(game_board)
        print(f"{player.name.upper()} turn")
        # players turn
        turn(player, game_board)
        # check for win conditions(nobody can win less than on 5th turn)
        if move_count >= 5:
            if is_player_win(game_board):
                win(player, game_board, revanche_flag)
                break
        # this is case of draw(standoff)
        if move_count == 9:
            standoff(revanche_flag)
            break
        # swap current player(from "X" to "O" and so on)
        player = swap_player_turn(player, first_player, second_player)
        move_count += 1
    # offer to play with the same player(revanche offer)
    revanche(first_player, second_player)


def input_players_name() -> tuple:
    """take players name input"""
    first_name = input("Ведите имя первого игрока: ")
    second_name = input("Ввелите имя второго игрока: ")
    return first_name, second_name


def get_random_first_player(first_name: str, second_name: str) -> tuple:
    """Randomly defines first player(he has race "X).
    Or leaves players input order or swap players(depend on random)
    init 2 Players objects"""
    if randint(0, 1) == 1:
        first_name, second_name = second_name, first_name
    first_player = Player(first_name, "X")
    second_player = Player(second_name, "O")
    # logger
    logger.debug(f"First player: {first_player.name.upper()}, he play '{first_player.get_race()}'. \
                Second player: {second_player.name.upper()}, he play '{second_player.get_race()}'")
    return first_player, second_player


def turn(player: Player, game_board: dict):
    """players turn. add current players pick on game board"""
    # check player pick empty slot
    while True:
        player_pick = int(input("Enter key number to fix spot: "))
        if game_board[player_pick] not in ("X", "O"):
            game_board[player_pick] = player.get_race()
            break
    print()


def swap_player_turn(player: Player, first_player: Player, second_player: Player) -> Player:
    """swap current player(from "X" to "O" and so on)"""
    player = second_player if player.get_race() == 'X' else first_player
    return player


def is_player_win(game_board: dict) -> bool:
    """Check all possible win combinations: 3 rows, 3 columns, 2 diagonals.
    Func check that lies or columns or diagonals has same value"""
    # 3 rows
    if len(set(map(game_board.get, (1, 2, 3)))) == 1 or\
       len(set(map(game_board.get, (4, 5, 6)))) == 1 or\
       len(set(map(game_board.get, (7, 8, 9)))) == 1:
        return True
    # 3 columns
    if len(set(map(game_board.get, (1, 4, 7)))) == 1 or\
       len(set(map(game_board.get, (2, 5, 8)))) == 1 or\
       len(set(map(game_board.get, (3, 6, 9)))) == 1:
        return True
    # 2 diagonals
    if len(set(map(game_board.get, (1, 5, 9)))) == 1 or\
       len(set(map(game_board.get, (3, 5, 7)))) == 1:
        return True
    return False


def win(player, game_board, revanche_flag):
    """Case - one of the player has won"""
    print_board(game_board)
    print(f"\tCongratz, {player.name} you  are win")
    print("\n\tThis game is over\n")
    logger.debug(f"\t\t{player.name.upper()} win. He play '{player.get_race()}'.")
    if revanche_flag:
        logger.info(f"\t\t{player.name.upper()} win. He play '{player.get_race()}'.")
    sleep(2)


def standoff(revanche_flag):
    """Case - standoff"""
    print("\tStandoff")
    print("\n\tThis game is over\n")
    logger.debug("\t\tStandoff.")
    if revanche_flag:
        logger.info("\t\tStandoff.")


def revanche(first_player: Player, second_player: Player):
    """proposition of revanche(play next game with the same opponent)"""
    user_choice = input("Реванш?(Y/N): ")
    print()
    # if player agree - swap players
    if user_choice.lower() in ("y", "yes"):
        first_player, second_player = second_player, first_player
        first_player.set_race("X")
        second_player.set_race("O")
        # logger for revanche
        logger.info("\t\tGAME START")
        logger.info(f"First player: {first_player.name.upper()}, race '{first_player.get_race()}'.\
                    Second player: {second_player.name.upper()}, race '{second_player.get_race()}'")
        # call game func
        game(first_player, second_player, revanche_flag=True)
