
def solve(numbers, stop):
    next = 0
    start = max(numbers.values()) + 1 
    for turn in range(start, stop):
        temp = next
        if next not in numbers:
            next = 0
        else:
            next = turn - numbers[next]
        numbers[temp] = turn 
        turn += 1
    return next

with open('input.txt') as f:
    data = f.readline().rstrip().split(',')

numbers = {int(x): data.index(x)+1 for x in data}
stop = 2020

print(f'Answer on turn {stop}: {solve(numbers, stop)}')
