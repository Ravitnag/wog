import random
import time
import sys
from colorama import init


init()


def generate_sequence(difficulty):
    return random.sample(range(1, 101), difficulty)


def get_list_from_user(difficulty):
    while True:
        user_input = input(f"please enter {difficulty} number as you remember (with space between): \n")
        try:
            return list(map(int, user_input.split(' ')))
        except Exception as e:
            print("something went wrong try again")


def is_list_equal(rand_list, user_list):
    return rand_list == user_list


def play(difficulty):
    rand_list = generate_sequence(difficulty)
    print("the number are going to be display for 0.7sec ")
    print(' '.join(map(str, rand_list)))
    time.sleep(0.7)
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')
    user_list = get_list_from_user(difficulty)
    return is_list_equal(rand_list, user_list)
