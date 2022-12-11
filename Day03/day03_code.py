import os 
import string
from functools import reduce
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day03.txt"

x = [l.strip() for  l in open(filename)]

alphabet = list(string.ascii_letters)
numbers = list(range(1,53))
priority = dict(zip(alphabet, numbers))

##Part One
def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    for letter in string1:
        if letter in string2:
            return priority[letter]

print(sum(list(map(splitstring, x))))

##Part Two
y = np.reshape(x, (len(x)//3, 3))

def group_elves(group):
    for let in group[0]:
        if (let in group[1]) and (let in group[2]):
            return priority[let]

print(sum(list(map(group_elves, y))))

