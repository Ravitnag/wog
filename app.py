from guess_game import play as guess_play
from currency_roulette_game import play as currency_roulette_play
from memory_game import play as memory_game


def welcome(username):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    num_of_game = input(
            "please choose number for a game: \n"
            "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
            "2. Guess Game - guess a number and see if you chose like the computer. \n"
            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    while True:
        num_of_game = int(num_of_game) if num_of_game.isnumeric() else 0
        if 0 < num_of_game < 4:
            break
        num_of_game = input("your choice need to be number between 1-3, try again\n")

    level_of_game = input("please choose the difficulty level between 1-5:\n")

    while True:
        level_of_game = int(level_of_game) if level_of_game.isnumeric() else 0
        if 0 < level_of_game < 6:
            break
        level_of_game = input("your choice need to be number between 1-5, try again\n")

    print(f'you chose game number: {num_of_game}\n'
          f'the level you chose is: {level_of_game}\n'
          'Have Fun :) ! \n')

    game_num_to_play_func = {
        1: memory_game,
        2: guess_play,
        3: currency_roulette_play
    }
    try:
        if game_num_to_play_func[num_of_game](level_of_game):
            print('you won!! :)')
        else:
            print('you lose :(')
    except Exception as e:
        print('something went wrong, try play again')
        print(e)


