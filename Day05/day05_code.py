import os 
import string
from functools import reduce
import numpy as np
import copy

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day05.txt"
input = [l for  l in open(filename)]
x = ('\n').join(input).split('\n\n')
y = ('\n').join(x).split('\n\n')

cargo = ('').join(y[0]).split('\n')
instruct = ('').join(y[1]).split('\n')


#Format cargo
cargo_set = {}
for i, key in enumerate([*cargo[-1]]):
    if key != ' ':
        cargo_set[key] = []
        for j in range(len(cargo)-2, -1, -1):
            if [*cargo][j][i] != ' ':
                cargo_set[key].append([*cargo][j][i])


def format_instruct (x):
    return x.split()[1::2]

instruct = list(map(format_instruct, instruct))


def crane_9000(input, cargo):
    boxes = copy.deepcopy(cargo)
    for move in input[:-1]:
        for i in range(int(move[0])):
            box = boxes[move[1]].pop()
            boxes[move[2]].append(box)
    return boxes

def top_boxes(cargo):
    for col, boxes in cargo.items():
        if boxes !=[]:
            yield boxes[-1]

print("".join(list(top_boxes(crane_9000(instruct, cargo_set)))))

#Part Two
def crane_9001(input, cargo):
    boxes = copy.deepcopy(cargo)
    for move in input[:-1]:
        box_num = int(move[0])
        end =len(boxes[move[1]])
        stay = boxes[move[1]][:end-box_num]
        swap = boxes[move[1]][end-box_num:]

        boxes[move[1]] = stay
        boxes[move[2]].extend(swap)
    return boxes

print("".join(list(top_boxes(crane_9001(instruct, cargo_set)))))
