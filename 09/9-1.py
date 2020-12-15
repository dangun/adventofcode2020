import os

# Checks if number has the property
def isvalid(numbers_queue, number):
    for i, num in enumerate(numbers_queue):
        for j in range(i + 1, len(numbers_queue)):
            if num + numbers_queue[j] == number:
                return True 
    return False

numbers = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    for line in f:
        numbers.append(int(line))

# Preamble
numbers_queue = []
for i in range(0,25):
    numbers_queue.append(numbers.pop(0))

# Check every number, slide number window if valid
for counter, number in enumerate(numbers):
    if not isvalid(numbers_queue, number):
        print(f'Invalid: {number}')
        break
    else:
        numbers_queue.pop(0)
        numbers_queue.append(numbers[counter])

