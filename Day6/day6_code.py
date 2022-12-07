import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day6.txt"

with open(filename) as f:
    x = f.read()

signal = list(x)[:-1]

def marker(code, chars):
    for i in range(len(code)-3):
        sub = set(code[i:i+chars])
        if len(sub) == chars:
            return i+chars

print(f"First message marker after character {marker(signal,4)}")
print(f"First message marker after character {marker(signal,14)}")