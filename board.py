"""
In this file, I created a board class where I initialized all the important attributes of the board to be used in the
game. These attributes include: the rows of the board, the columns of the board and the main game board.
I used these attributes to check whether either the shoot or start location entered by the player is valid or not,
whether the ships overlap on the game board, if there is space available on the game board, if the player's move is
valid, record the hit made by the player and display the game board.
"""


class Board:
    def __init__(self, game_config) -> None:
        """
        This function initializes all the attributes that need to be used by the board
        :param game_config: a dictionary of all the variables and values needed in this game (rows, columns, number of
        ships, the character that represents the ship, the size of the ship)
        """
        self.row = game_config['row']
        self.col = game_config['col']
        self.game_board = []
        for x in range(self.row):
            game_board = []
            for y in range(self.col):
                game_board.append('*')
            self.game_board.append(game_board)

    def valid_location(self, location_on_board: str, orientation: str, ship_size: int) -> bool:
        """
        This function checks whether the location to shoot or start chosen by the player is valid or not
        :param location_on_board: the row and column entered by the player
        :param orientation: vertical or horizontal
        :param ship_size: the size of the ship
        :return: a boolean (True or False)
        """
        if location_on_board.isspace():
            return False
        location_on_board = location_on_board.split(' ')
        if len(location_on_board) != 2:
            return False
        row, col = location_on_board
        if not row.isdigit() or not col.isdigit():
            return False
        row = int(row)
        col = int(col)
        if not (0 <= row < self.row) or not (0 <= col < self.col):
            return False
        if self.does_ship_overlap(row, col, orientation, ship_size):
            return False
        if not self.space_available(row, col, orientation, ship_size):
            return False
        else:
            return True

    def does_ship_overlap(self, row: int, col: int, orientation: str, ship_size: int) -> bool:
        """
        This function checks whether the ship is overlapping on the game board
        :param row: the number of rows in the game board
        :param col: the number of columns in the game board
        :param orientation: vertical or horizontal
        :param ship_size: size of the ship
        :return: a boolean (True or False)
        """
        if orientation in 'vertically':
            for n in range(ship_size):
                if self.game_board[row][col] != '*':
                    return True
                row += 1
                if row == len(self.game_board):
                    break
        elif orientation in 'horizontally':
            for n in range(ship_size):
                if self.game_board[row][col] != '*':
                    return True
                col += 1
                if col == len(self.game_board[0]):
                    break

    def space_available(self, row: int, col: int, orientation: str, ship_size: int) -> bool:
        """
        This fucntion checks whether there is space available on the game board
        :param row: the number of rows in the game board
        :param col: the number of columns in the game board
        :param orientation: vertical or horizontal
        :param ship_size: size of the ship
        :return: a boolean (True or False)
        """
        if orientation in 'vertically':
            board_space = len(self.game_board) - row
            if board_space < ship_size:
                return False
            return True
        elif orientation in 'horizontally':
            board_space = len(self.game_board[0]) - col
            if board_space < ship_size:
                return False
            return True

    def valid_player_move(self, move: str) -> bool:
        """
        This function checks whether the move made by the player is valid or not
        :param move: the palyer's move (row and column)
        :return:
        """
        if move.isspace():
            return False
        move = move.split(' ')
        if len(move) != 2:
            return False
        row, col = move
        if not row.isdigit() or not col.isdigit():
            return False
        row = int(row)
        col = int(col)
        if not (0 <= row < len(self.game_board)) or not (0 <= col < len(self.game_board[0])):
            return False

        if self.game_board[row][col] == 'X' or self.game_board[row][col] == 'O':
            return False
        else:
            return True

    def add_battleship(self, ship_char: str, ship_size: int, player_location: str, orientation: str) -> None:
        """
        This function adds the battleship to the player's placement board
        :param ship_char: the ship represented by the character
        :param ship_size: the size of the ship
        :param player_location: the location given by the player
        :param orientation: vertical or horizontal
        :return: None
        """
        player_location = player_location.split(' ')
        row, col = player_location
        row = int(row)
        col = int(col)
        if orientation in 'vertically':
            for n in range(ship_size):
                self.game_board[row][col] = ship_char
                row += 1
        elif orientation in 'horizontally':
            for n in range(ship_size):
                self.game_board[row][col] = ship_char
                col += 1

    def record_hit_on_board(self, row: int, col: int) -> None:
        """
        This function records the hit made by the player on the game baord
        :param row: the number of rows in the game board
        :param col: the number of columns in the game board
        :return: None
        """
        if self.game_board[row][col] == '*':
            self.game_board[row][col] = 'O'
        else:
            self.game_board[row][col] = 'X'

    def display_board(self) -> None:
        """
        This function is an adaptation of the connect n code to display the game board
        :return: None
        """
        print(end='  ')
        for header in range(self.col):
            print(header, end=' ')
        print()
        x = list(enumerate(self.game_board))
        for row_index, row in x:
            print(row_index, ' '.join(row))
