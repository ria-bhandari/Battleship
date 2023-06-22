"""
This main file is the main battleship game.
It is a turn based game where each player first adds their ships to a game board and then shoots their opponent until
someone wins.
In this program, I did a lot of error checking as well as defining of objects and creating classes.
I also read the contents of the file where the rows, columns, number of ships, character representation of ship and
ship size is specified.
"""
from battleship.player import Player
from battleship.game import Game


def read_file_and_get_contents(file):
    """
    This function reads the file and saves its contents into a dictionary that is used throughout the game
    :param file: the file gotten from the path entered by the user
    :return: a dictionary of the contents of the file
    """
    game_config = {"row": 0, "col" : 0, 'no_ships' : 0, 'inf_ship' : []}
    game_config['row'] = int(file.readline())
    game_config['col'] = int(file.readline())
    game_config['no_ships'] = int(file.readline())
    for line in file:
        game_config['inf_ship'].append(line.split(' '))
        game_config['inf_ship'] = sorted(game_config['inf_ship'])
    return game_config


def main() -> None:
    """
    This is the main function where everything is called in order to play the battleship game
    :return: None
    """
    path = input("Please enter the path to the configuration file for this game: ").strip()
    file = open(path, 'r')
    info = read_file_and_get_contents(file)
    no_of_players = 2
    list_of_players = []
    for i in range(no_of_players):
        player_name = input(f'Player {i+1}, please enter your name: ')
        list_of_players.append(Player(player_name, info))

    battleship_game = Game(info, list_of_players)
    battleship_game.set_up_game()
    battleship_game.play_game()


"""
This statement below calls the main function to run
"""
if __name__ == '__main__':
    main()