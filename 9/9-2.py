import os

# Modifies numbers_queue to valid subset
def findsubset(numbers, numbers_queue, number):
    while numbers:
        check = sum(numbers_queue)
        if check == number:
            return True
        elif check > number:
            numbers_queue.pop(0)
        elif check < number:
            numbers_queue.append(numbers.pop(0))
    return False     

numbers = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    for line in f:
        numbers.append(int(line))

# Initial set
numbers_queue = []
for i in range(0,2):
    numbers_queue.append(numbers.pop(0))

# Check if a contigious set exists that sums up to number 
if findsubset(numbers, numbers_queue, number=466456641):
    print(f'Sum of min and max: {min(numbers_queue) + max(numbers_queue)}')
else:
    print('Failed')