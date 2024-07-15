from utils import SCORES_FILE_NAME

def add_score(difficulty):
    with open(SCORES_FILE_NAME, 'r+') as scores_file:
        curr_scores = scores_file.read()
        new_scores = int(curr_scores) + ((difficulty * 3) + 5)
        scores_file.seek(0)
        scores_file.write(str(new_scores))
        scores_file.truncate()
        return new_scores

def zero_score():
    with open(SCORES_FILE_NAME, 'w') as scores_file:
        scores_file.write("0")




zero_score()