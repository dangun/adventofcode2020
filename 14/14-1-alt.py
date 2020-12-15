import re

def decode(bitmasks):
    memory = {}
    for bitmask in bitmasks:
        for assign in bitmask[1]:
            memory[assign[0]] = assign[1] & ~bitmask[0][0] | bitmask[0][1]
    return memory

bitmasks = []
with open('input.txt') as f:
    current_mask = None
    for line in f:
        data = line.strip().split(' = ')
        if data[0] == 'mask':
            zeroes = sum([2**(abs(m.start(0)-36)-1) for m in re.finditer(r'0', data[1])])
            ones = sum([2**(abs(m.start(0)-36)-1) for m in re.finditer(r'1', data[1])])
            current_mask = []
            bitmasks.append(((zeroes, ones), current_mask))
        else:
            bitmasks[-1][1].append((int(data[0][4:-1]), int(data[1])))

print(f'Answer: {sum(decode(bitmasks).values())}')
