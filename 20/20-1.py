import numpy as np
import math
from copy import deepcopy

def getvariations(block):
    block_variations = []
    block_variations.append(block)
    block_variations.append(np.rot90(block, 1).copy())
    block_variations.append(np.rot90(block, 2).copy())
    block_variations.append(np.rot90(block, 3).copy())
    block_variations.append(np.fliplr(block).copy())
    block_variations.append(np.rot90(np.fliplr(block), 1).copy())
    block_variations.append(np.rot90(np.fliplr(block), 2).copy())
    block_variations.append(np.rot90(np.fliplr(block), 3).copy())

    return block_variations

def checkfit(square, block, pos):

    test = True
    if square[pos[1]][max(0,pos[0]-1)] is not None:
        test &= (square[pos[1]][max(0,pos[0]-1)][:,-1] == block[:,0]).all() # Check left side

    if square[max(0,pos[1]-1)][pos[0]] is not None:
        test &= (square[max(0,pos[1]-1)][pos[0]][-1,:] == block[0,:]).all() # Check top side

    return test

def fit(square, available_blocks, blocks_ids):
    # Finished condition
    if not any(item is None for sublist in square for item in sublist):
        return (blocks_ids, square)

    # Update position to next empty
    for x in range(0, len(square)):
        for y in range(0, len(square)):
            if square[y][x] is None:
                pos = (x, y)
                break
        if square[y][x] is None:
            break    

    for (block_id, block) in available_blocks:
        for blockxy in block:
            if checkfit(square, blockxy, pos):
                new_square = deepcopy(square)
                new_square[pos[1]][pos[0]] = blockxy 
                new_available_blocks = [x for x in available_blocks if not block_id == x[0]]

                answer = fit(new_square, new_available_blocks, blocks_ids)
                # Return back the answer, add on used block ids on the way
                if answer is not None:
                    if (pos[0] == 0 and pos[1] == 0) \
                        or (pos[0] == len(square)-1 and pos[1] == 0)\
                        or (pos[0] == 0 and pos[1] == len(square)-1)\
                        or (pos[0] == len(square)-1 and pos[1] == len(square)-1):
                        answer[0].append(block_id)
                    return answer

def solve(blocks):
    dimension = int(math.sqrt(len(blocks)))
    square = [[None for i in range(dimension)] for i in range(dimension) ]
    grid = fit(square, blocks, [])
    return grid
    
with open('input.txt') as f:
    data = f.read().split('\n\n')

blocks_ids = {}
blocks = []
for i, block in enumerate(data): 
    blocks_ids[i] = block.split(':')[0].split(' ')[1]
    blocks.append((int(blocks_ids[i]), \
        getvariations(np.array([[x for x in line.strip()] for line in block.splitlines()[1:]]))))

grid = solve(blocks)
print(f'Answer: {math.prod(grid[0])}')