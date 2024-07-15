import sys
import time

SCORES_FILE_NAME = "./user_scores.txt"
BAD_RETURN_CODE = 500

def screen_cleaner():
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')


