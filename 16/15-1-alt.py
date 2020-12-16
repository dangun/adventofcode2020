import re

error_rate = 0

with open('input.txt') as f:
    valid_ranges = []
    data = f.read().split('\n\n')

    # # Get valid ranges and all numbers
    valid_ranges = [range(int(a),int(b)+1) for a,b in re.findall(r'(\d+)-(\d+)', data[0])]
    numbers = [int(a) for a in re.findall(r'(\d+)', data[2])]

    # Check all ticket numbers for if they are valid or not
    for number in numbers:
        valid = False
        for valid_range in valid_ranges:
            if number in valid_range:
                valid = True
                break
        if not valid:
            error_rate += number

print(f'Answer: {error_rate}')

