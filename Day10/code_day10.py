import pathlib

def split_input(filename: str) -> list:
    file = (pathlib.Path(__file__).parent / filename).read_text().strip().split('\n')
    for i, x in enumerate(file):
        file[i] = x.split() 
    return file

def check_cycle(cycle: int, signal: int) -> int:
    cycle_list = [20, 60, 100, 140, 180, 220]
    if cycle in cycle_list:
        print(signal)
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
            

if __name__ == '__main__':
    file = split_input('input_day10.txt')
    print(f"The sum of the intervaled signal strength is {run_signal(file)}")