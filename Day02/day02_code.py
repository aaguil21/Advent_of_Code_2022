import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day02.txt"

x = [l.strip() for  l in open(filename)]
split_text = lambda x: x.split()
y = list(map(split_text, x))

scores = {'X': {'A':4, 'B':1, 'C':7}, 'Y': {'A':8, 'B':5, 'C':2}, 'Z': {'A':3, 'B':9, 'C':6} }

def score_3 (x,) :
    return scores[x[1]][x[0]]

total_score = sum(list(map(score_3, y)))
print(total_score)

outcome = {'X': {'A':3, 'B':1, 'C':2}, 'Y': {'A':4, 'B':5, 'C':6}, 'Z': {'A':8, 'B':9, 'C':7} }
def outcome_3 (x):
    return outcome[x[1]][x[0]]

total_outcome = sum(list(map(outcome_3, y)))
print(total_outcome)
