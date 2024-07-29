import random


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guess_number = input(f'Enter your guess, number between 0 to {difficulty}\n')
    while True:
        guess_number = int(guess_number) if guess_number.isnumeric() else False
        if 0 <= guess_number <= difficulty:
            break
        guess_number = input(f'oops! you should enter number between 0 to {difficulty}\n'
                             'try again!\n')
    return guess_number


def compare_results(secret_number, guess_number):
    return secret_number == guess_number


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess_number = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess_number)




