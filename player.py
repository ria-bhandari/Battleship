"""
In this file, I created a class for the player with various attributes that are used throughout the battleship game.
The main attributes of a player are: player name, the game configuration pertaining to this player (all the
variables and values used from the file that is being read at the beginning of this program), the current ship
the player is adding to their board and 2 boards for the player (placement and firing).
Using these attributes, I can check whether there are any ships left to hit for the player and I can add an 'X' or an
'O' if the player hit their opponent or not
"""
from . import board


class Player:
    def __init__(self, player_name: str, game_config) -> None:
        """
        This function initializes all the attributes for the player
        :param player_name: the player's name entered by the player as the game starts
        :param game_config: a dictionary of all the variables and values needed in this game (rows, columns, number of
        ships, the character that represents the ship, the size of the ship)
        """
        self.player_name = player_name
        self.game_config = game_config
        self.coordinate_point = 0
        self.curr_ship_on_board = {}
        self.placement_board = board.Board(game_config)
        self.firing_board = board.Board(game_config)

    def no_ship_left(self) -> bool:
        """
        This function checks if the player has any battleships left
        :return: a boolean value (true or false)
        """
        ships_left_on_board = 0
        for pos in self.curr_ship_on_board.values():
            ships_left_on_board += pos
        return ships_left_on_board == 0

    def get_hit(self, row: int, col: int, target_board: str) -> None:
        """
        This function gets the hit from the player and adds it to the game boards
        :param row: the number of rows in the game board
        :param col: the number of columns in the game board
        :param target_board: the area of the game board hit by the player
        :return: None
        """
        if target_board == '*':
            self.placement_board.game_board[row][col] = 'O'
            self.firing_board.game_board[row][col] = 'O'

        else:
            self.placement_board.game_board[row][col] = 'X'
            self.firing_board.game_board[row][col] = 'X'
            self.curr_ship_on_board[target_board] -= 1
