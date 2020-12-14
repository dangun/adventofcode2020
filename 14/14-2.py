import os

def write(memory, address, value):
    if address.count('X') == 0:
        memory[int(address, 2)] = value
        return
    write(memory, address.replace('X', '0', 1), value)
    write(memory, address.replace('X', '1', 1), value)

def write_helper(bitmasks):
    memory = {}
    for bitmask in bitmasks:
        for assign in bitmask[1]:
            address = ''
            for mask, addr in zip(bitmask[0], '{0:036b}'.format(assign[0])):
                if mask == '0':
                    address += addr
                else:
                    address += mask
            write(memory, address, assign[1])
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

print(f'Answer: {sum(write_helper(bitmasks).values())}')
