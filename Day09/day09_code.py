import numpy as np
import pathlib

key = {'U': [0.,1.], 'D': [0.,-1.], 'L':[-1.,0.], 'R':[1.,0.]}

def split_list(filename: str) -> list:
    file = (pathlib.Path(__file__).parent / filename).read_text().strip().split('\n')
    for i, x in enumerate(file):
        file[i] = x.split() 
    return file

def ceil_neg(arr):
    _arr = np.abs(arr)
    np.ceil(_arr, _arr) # inplace
    np.copysign(_arr, arr, out = _arr)
    return _arr

def rope_path(input: list) -> int:
    head = np.array([0.,0.])   
    tail = np.array([0.,0.])
    positions = []
    positions.append(tail)
    for i in input:
        for x in range(int(i[1])):
            head += np.array(key[i[0]])
            dist = head - tail
            dist_val = np.linalg.norm(dist, ord=2)
            if dist_val >= 2:
                tail += ceil_neg(dist/dist_val)
            positions.append(list(tail))
    
    pos_set = {tuple(pos) for pos in positions}
    return len(pos_set)



#Part Two
def make_rope(length):
    rope = []
    for i in range(length):
        rope.append(np.array([0.,0.]))
    return rope

def longer_rope_path(input: list) -> int:
    rope = make_rope(10)
    positions = []
    positions.append(rope[-1])
    for i in input:
        for x in range(int(i[1])):
            rope[0] += np.array(key[i[0]])
            for seg in range(1,len(rope)):
                dist = rope[seg-1] - rope[seg]
                dist_val = np.linalg.norm(dist, ord=2)
                if dist_val >= 2:
                    rope[seg] +=ceil_neg(dist/dist_val)
            positions.append(list(rope[-1]))
    
    pos_set = {tuple(pos) for pos in positions}
    return len(pos_set)


if __name__ == '__main__': 
    file = split_list("input_day09.txt")
    print(f"The number of positions the tail was at is {rope_path(file)}")
    print(f"The number of positions the tail was at for the longer rope is {longer_rope_path(file)}")
