import pathlib
import numpy as np

def split_list(filename: str) -> list:
    file = (pathlib.Path(__file__).parent / filename).read_text().strip().split('\n')
    for i, x in enumerate(file):
        file[i] = list(map(int, list(x)))
    return file

def visible_trees(forest: list) -> int:
    vis_count = 0
    forest = np.array(forest)
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            if row==0 or col==0:
                vis_count +=1
            else:
                tree = forest[row][col]
                height = lambda x: x >= tree
                left_vis = len(list(filter(height, forest[:row, col]))) == 0
                rght_vis = len(list(filter(height, forest[row+1:, col]))) == 0
                top_vis = len(list(filter(height, forest[row, :col]))) == 0
                bot_vis = len(list(filter(height, forest[row, col+1:]))) == 0
                if (left_vis) or (rght_vis) or (top_vis) or (bot_vis):
                    vis_count += 1
    return vis_count

def tree_view(trees: list):
    forest = np.array(trees)
    view_score = 0
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            tree  = forest[row][col]
            top  = row_view(tree, np.flip(forest[:row, col]))
            bot = row_view(tree, forest[row+1:, col])
            left   = row_view(tree, np.flip(forest[row, :col]))
            right   = row_view(tree, forest[row, col+1:])

            score = left*right*top*bot
            if score > view_score:
                view_score = score
    return view_score
           
                

def row_view(x, array) -> int:
    view = []
    for i in array:
        view.append(i)
        if i >= x:
            break
    return len(view)


if __name__ == '__main__':
    trees = split_list("input_day8.txt")
    print(f"The number of visible trees is {visible_trees(trees)}")
    print(f"The highest scenic score is {tree_view(trees)}")