import os

def decode(bitmasks):
    memory = {}
    for bitmask in bitmasks:
        zeroes = int(bitmask[0].replace('1', '0').replace('X', '1'), 2)
        ones = int(bitmask[0].replace('X', '0'), 2)
        for assign in bitmask[1]:
            memory[assign[0]] = assign[1] & zeroes | ones
    return memory

bitmasks = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    mem_assign = None
    for line in f:
        data = line.strip().split(' = ')
        if data[0] == 'mask':
            mem_assign = []
            bitmasks.append((data[1], mem_assign))
        else:
            mem_assign.append((int(data[0][4:-1]), int(data[1])))

print(f'Answer: {sum(decode(bitmasks).values())}')
