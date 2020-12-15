 
right = 3
down = 1

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

tree_count = traverseroadmap(roadmap, right, down)

print(f'# of trees encountered: {tree_count}')
