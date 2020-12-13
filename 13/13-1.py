import os

def findfirstbus(buses, time):
    i = time
    while True:
        for bus in buses:
            if i % bus == 0:
                print(bus)
                return (i - time) * bus
        i += 1

time = 0
buses = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    time = int(f.readline())
    buses = [int(bus) for bus in f.readline().rstrip().split(',') if bus != 'x']

print(f'Answer: {findfirstbus(buses, time)}')
