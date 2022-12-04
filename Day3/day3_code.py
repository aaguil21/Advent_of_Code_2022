import os 
import string
from functools import reduce

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day3.txt"

x = [l.strip() for  l in open(filename)]

alphabet = list(string.ascii_letters)
numbers = list(range(1,53))
priority = dict(zip(alphabet, numbers))

def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    for letter in string1:
        if letter in string2:
            return priority[letter]

print(sum(list(map(splitstring, x))))




