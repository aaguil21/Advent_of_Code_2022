import pathlib

def marker(code, chars):
    for i in range(len(code)-3):
        if  len(set(code[i:i+chars])) == chars:
            return i+chars

if __name__ == '__main__':
    signal = (pathlib.Path(__file__).parent / "input_day06.txt").read_text().strip()
    print(f"First start-of-packet marker after character {marker(signal,4)}")
    print(f"First start-of-message marker after character {marker(signal,14)}")