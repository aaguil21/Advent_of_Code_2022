#Day 1 of Advent of Code challenge 
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


filename = "input_Day1.txt"

cal = [l.strip() for  l in open(filename)]

elves = ('\n').join(cal).split('\n\n')

def splitsum (x):
    y = list(map(int, x.split()))
    return sum(y)

sum_elves = list(map(splitsum, elves))
sum_elves.sort(reverse=True)

print(sum_elves[0])
print(sum(sum_elves[0:3]))

