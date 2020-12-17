
error_rate = 0
valid_ranges = []

with open('input.txt') as f:
    data = f.read().split('\n\n')

# Get valid ranges
for line in data[0].splitlines():
    for range_values in line.split(': ')[1].split(' or '):
        range_values = range_values.split('-')
        valid_ranges.append(range(int(range_values[0]), int(range_values[1])+1))

# Check all ticket numbers for if they are valid or not
for line in data[2].splitlines()[1:]:
    for number in line.split(','):
        valid = False
        number = int(number)
        for valid_range in valid_ranges:
            if number in valid_range:
                valid = True
                break
        if not valid:
            error_rate += number

print(f'Answer: {error_rate}')

