import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "input_day7.txt"

x = [l.strip() for  l in open(filename)]

def split_list(x):
    return x.split()
print(list(map(split_list, x)))

class DirTree():
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_children(self, child):
        child.parent = self
        self.children.append(child)