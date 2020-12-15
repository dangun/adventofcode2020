from itertools import combinations

sum = 2020

def findsumpair(sum, values):
    for target in combinations(values, 3):
        if target[0] + target[1] + target[2] == sum:
            return target

with open('input.txt') as f:
    values = [int(x) for x in f]

value_pair = findsumpair(2020, values)

print(f'Sum: {sum}')
print(f'Pair: {value_pair[0]} {value_pair[1]} {value_pair[2]}')
print(f'Product: {value_pair[0] * value_pair[1] * value_pair[2]}')
