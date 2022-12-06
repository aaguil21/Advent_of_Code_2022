import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day4.txt"

x = [l.strip() for  l in open(filename)]

def tasks(x):
    elves = x.split(",")
    for elf in elves:
        elf = elf.split("-")
        yield elf

y = list(map(list, map(tasks, x)))

#Part One
def encapsule (x):
    elf1 = list(range(int(x[0][0]), int(x[0][1])+1))
    elf2 = list(range(int(x[1][0]), int(x[1][1])+1))
    if (set(elf1).issubset(elf2)) or (set(elf2).issubset(elf1)):
        return 1
    else:
        return 0

print(sum(list(map(encapsule, y))))

#Part Two
def overlap (x):
    elf1 = list(range(int(x[0][0]), int(x[0][1])+1))
    elf2 = list(range(int(x[1][0]), int(x[1][1])+1))
    for i in elf1:
        if i in elf2:
            return 1
    return 0

print(sum(list(map(overlap, y))))
