import operator
from functools import reduce

road_choices = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def convertmap(symbol):
    if symbol == '.': return 0
    elif symbol == '#': return 1

def createroadmap(area):
    area = [s.strip() for s in area]
    return [list(map(convertmap, x)) for x in area]

def traverseroadmap(roadmap, right, down):
    x = 0
    y = 0
    width = len(roadmap[0])
    tree_count = 0

    while y < len(roadmap) - 1:
        x = (x + right) % width
        y += down 
        tree_count += roadmap[y][x]

    return tree_count

with open('input.txt') as f:
    area = f.readlines()

roadmap = createroadmap(area)
tree_counts = [traverseroadmap(roadmap, steps[0], steps[1]) for steps in road_choices]
tree_product = reduce(operator.mul, tree_counts, 1)

print(f'The product of the # of trees encountered on each slope: {tree_product}')