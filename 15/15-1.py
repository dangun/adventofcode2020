import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    data = f.readline().rstrip().split(',')

numbers = {int(x): data.index(x)+1 for x in data}
start = max(numbers.values())

next = 0
start += 1
stop = 2020
for turn in range(start, stop+1):
    temp = next
    if next not in numbers:
        next = 0
    else:
        next = turn - numbers[next]
    numbers[temp] = turn 
    turn += 1

print(f'Answer on turn {stop}: {temp}')
