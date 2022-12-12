import pathlib
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def split_input(filename: str) -> list:
    input = [l for  l in open('input_day11.txt')]
    x = ('\n').join(input).split('\n\n')
    y = ('\n').join(x).split('\n\n')

    monkeys = []
    for i, monkey in enumerate(y):
        split_list = lambda x: x.split()
        data = list(map(split_list, ('').join(y[0]).split('\n')))
        name = " ".join(data[0][0], data[0][1][0])
        items = 

        monkeys[i].append(monkey(name, items, test, cond1, cond2))

    return monkeys

class monkey():
    def __init__(self, name, items, test, cond1, cond2):
        self.name = items
        self.items = items
        self.test = test
        self.cond1 = cond1
        self.cond2 = cond2


if __name__ == '__main__': 
    file = split_input('input_day11.txt')
    print(file)