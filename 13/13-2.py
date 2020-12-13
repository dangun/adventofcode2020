import os

def findtime(buses):
    jump = buses[0][0]
    i = 0
    for bus, offset in buses[1:]:
        while (i + offset) % bus != 0: 
            i += jump
        jump *= bus # Divisible by all previous buses, multiply to preserve property
    return i

buses = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    f.readline()
    for offset, symbol in enumerate(f.readline().rstrip().split(',')):
        if symbol != 'x':
            buses.append((int(symbol), offset))

print(f'Answer: {findtime(buses)}')
