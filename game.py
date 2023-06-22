"""
In this file, I created a class for the game. In this class I first define the main attributes to use in the game which
are: the list of players, the current player's turn and the game configuration pertaining to the game (all the
variables and values used from the file that is being read at the beginning of this program).
I use these attributes for the game object by setting up the game, playing the game, getting the players' turn,
checking whether a player sunk their opponent's battleship and announcing the results of the game
"""


class Game:
    def __init__(self, game_config, list_of_players: list['Player']) -> None:
        """
        This function initializes the main attributes for the game
        :param game_config: a dictionary of all the variables and values needed in this game (rows, columns, number of
        ships, the character that represents the ship, the size of the ship)
        :param list_of_players: a list of the players involved in the game
        """
        self.list_of_players = list_of_players
        self.curr_turn = 0
        self.game_config = game_config

    def set_up_game(self) -> None:
        """
        This function sets up the game. I followed the order given on prairielearn.
        :return: None
        """
        for player in self.list_of_players:
            print(f'{player.player_name}\'s Placement Board')
            player.placement_board.display_board()
            for ship in self.game_config['inf_ship']:
                ship_char = ship[0]
                ship_size = int(ship[1])
                flag = True
                while flag:
                    orientation = input(f'{player.player_name}, enter the orientation of your {ship_char}, which is {ship_size} long: ').lower().strip()
                    if orientation in 'vertically' or orientation in 'horizontally':
                        player_location = input(f'Enter the starting location for your {ship_char}, which is {ship_size} long, in the form row col: ').strip()
                        if player.placement_board.valid_location(player_location, orientation, ship_size):
                            break
                player.placement_board.add_battleship(ship_char, ship_size, player_location, orientation)
                player.curr_ship_on_board[ship_char] = ship_size
                print(f'{player.player_name}\'s Placement Board')
                player.placement_board.display_board()

    def play_game(self) -> None:
        """
        The game is played in this function by first checking whether the game is over and if it is not over,
        each player's boards are displayed and locations to fire at are asked
        :return: None
        """
        while not self.is_game_over():
            print(f'{self.curr_player().player_name}\'s Firing Board')
            self.next_player().firing_board.display_board()
            print(f'{self.curr_player().player_name}\'s Placement Board')
            self.curr_player().placement_board.display_board()
            player_move = input(f'{self.curr_player().player_name}, enter the location you want to fire at in the form row col: ').strip()
            while not self.next_player().firing_board.valid_player_move(player_move):
                player_move = input(f'{self.curr_player().player_name}, enter the location you want to fire at in the form row col: ').strip()
            player_move = player_move.split(' ')
            row, col = player_move
            row = int(row)
            col = int(col)
            self.go_about_game(row, col)
            self.switch_players()
        self.announce_results()

    def has_ship_been_destroyed(self, target_on_board: str) -> None:
        """
        This function checks whether the player destroyed/sunk their opponent's battleship
        :param target_on_board: the place where the player hit their opponent
        :return:
        """
        if self.next_player().curr_ship_on_board[target_on_board] == 0:
            print(f'{self.curr_player().player_name} destroyed {self.next_player().player_name}\'s {target_on_board}!')

    def go_about_game(self, row: int, col: int) -> None:
        """
        This function indicates how to go about the game in terms of the target
        :param row: the number of rows in the game board
        :param col: the number of columns in the game board
        :return:
        """
        target_on_board = self.next_player().placement_board.game_board[row][col]
        if target_on_board != '*':
            print(f'{self.curr_player().player_name} hit {self.next_player().player_name}\'s {target_on_board}!')
            self.next_player().get_hit(row, col, target_on_board)
            self.has_ship_been_destroyed(target_on_board)
        else:
            print(f'{self.curr_player().player_name} missed.')
            self.next_player().get_hit(row, col, target_on_board)

    def curr_player(self) -> str:
        """
        This function returns the current player of the game
        :return: current player of the game
        """
        return self.list_of_players[self.curr_turn]

    def next_player(self) -> str:
        """
        This function gets the next player according to the current player turn
        :return: next player in game
        """
        if self.curr_turn == 0:
            return self.list_of_players[1]
        else:
            return self.list_of_players[0]

    def is_game_over(self) -> bool:
        """
        This checks whether the game is over
        The game is over if: a player sunk all the battleships of their opponent
        :return: True if the player sunk all the ships and false if they didn't
        """
        for player in self.list_of_players:
            if player.no_ship_left():
                return True
        return False

    def announce_results(self) -> None:
        """
        This function announces the results of the battleship game
        :return: None
        """
        for player in self.list_of_players:
            if not player.no_ship_left():
                winner = player
            else:
                loser = player

        print(f'{winner.player_name}\'s Firing Board')
        loser.firing_board.display_board()
        print(f'{winner.player_name}\'s Placement Board')
        winner.placement_board.display_board()
        print(f'{winner.player_name} won!')

    def switch_players(self) -> None:
        """
        This function switches the player's turn (adaptation of connect n code)
        :return: None
        """
        if self.curr_turn == 0:
            self.curr_turn = 1
        else:
            self.curr_turn = 0

