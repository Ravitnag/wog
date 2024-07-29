from freecurrencyapi import Client
import random
def get_money_interval(difficulty):
    try:
        api_client = Client("fca_live_GSZqminuIR3xjXcxhCqNMRxFp287KfHFImVlWyWn")
        exchange_rate = api_client.latest(currencies=['USD', 'ILS'])
        exchange_rate = exchange_rate['data']['ILS']
    except Exception as e:
        print('error occured getting the exchange rate.\n please try again.')
        raise ()
    interval = 10 - difficulty
    return exchange_rate, interval


def get_guess_from_user():
    amount_dollars = random.randint(1, 100)
    while True:
        guess = input(f'please guess how much shekels are {amount_dollars}$\n')
        try:
            guess = float(guess)
            return amount_dollars, guess
        except Exception as e:
            print("the guess must be a number \n")


def compare_result(difficulty):
    amount_dollars, guess = get_guess_from_user()
    exchange_rate, interval = get_money_interval(difficulty)
    right_answer = amount_dollars * exchange_rate

    if right_answer - interval < guess < right_answer + interval:
        return True

    return False


def play(difficulty):
    return compare_result(difficulty)


