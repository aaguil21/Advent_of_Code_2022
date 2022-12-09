import pathlib

def split_list(filename: str) -> list:
    file = (pathlib.Path(__file__).parent / filename).read_text().split('\n')
    for i, x in enumerate(file):
         file[i] = x.split()
    return file


class DirTree():
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
        self.level = 0
    
    def add_children(self, child):
        child.parent = self
        child.level = self.level + 1
        self.children.append(child)
        
"""
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
"""

if __name__ == '__main__':
    commands = split_list("input_day7.txt")
