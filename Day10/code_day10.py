import pathlib

def split_input(filename: str) -> list:
    file = (pathlib.Path(__file__).parent / filename).read_text().strip().split('\n')
    for i, x in enumerate(file):
        file[i] = x.split() 
    return file

def check_cycle(cycle: int, signal: int) -> int:
    cycle_list = [20, 60, 100, 140, 180, 220]
    if cycle in cycle_list:
        return cycle*signal
    else:
        return 0

def run_signal (input: list) -> int:
    sum, cycle = 0, 1
    signal = 1
    for command in input:
        if command[0] == 'noop':
            sum += check_cycle(cycle, signal)
            cycle += 1
        if command[0] == 'addx':
            sum += check_cycle(cycle, signal)
            cycle += 1
            sum += check_cycle(cycle, signal)
            signal += int(command[1])
            cycle += 1
    return sum
            
#Part Two

def check_crt(cycle: int, signal: int, crt: list):
    col = (cycle-1)%40
    row = (cycle-1) // 40
    x_ = list(range(signal-1, signal+2))
    #print(col, x_)
    if col in x_:
        crt[row][col] = '#'


def crt_signal (input: list) -> int:
    crt = [['.' for _ in range(40)] for _ in range(6)]
    sum, cycle = 0, 1
    signal = 1
    for command in input:
        if command[0] == 'noop':
            check_crt(cycle, signal, crt)
            cycle += 1
        if command[0] == 'addx':
            check_crt(cycle, signal, crt)
            cycle += 1
            check_crt(cycle, signal, crt)
            signal += int(command[1])
            cycle += 1
    
    show_crt(crt)

def show_crt(input: list):
    for row in input:
        print(''.join(row))

if __name__ == '__main__':
    file = split_input('input_day10.txt')
    print(f"The sum of the intervaled signal strength is {run_signal(file)}")
    crt_signal(file)