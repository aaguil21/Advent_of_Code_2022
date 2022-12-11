import pathlib
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def split_input(filename: str) -> list:
    input = [l for  l in open('input_day11.txt')]
    x = ('\n').join(input).split('\n\n')
    y = ('\n').join(x).split('\n\n')

    monkeys = 
    for i, monkey in enumerate(y):
        split_list = lambda x: x.split()
        data = list(map(split_list, ('').join(y[0]).split('\n')))
         = []
        monkeys[i].append(data[0])

    return monkeys

class monkey():
    def __init__(self, data):
        self.name = data[0]
        self.items = data[1]
        self.inspect = data[2]


if __name__ == '__main__': 
    file = split_input('input_day11.txt')
    print(file)