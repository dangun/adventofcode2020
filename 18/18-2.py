import math
import re

def solve(equation):
    balanced = 0
    start = 0
    substring = []
    # Find all the outer enclosed expressions
    for i, symbol in enumerate(equation):
        if symbol == '(':
            if balanced == 0:
                start = i
            balanced += 1
        elif symbol == ')':
            balanced -= 1
            if balanced == 0:
                substring.append(equation[start+1:i])
    # For each expression enclosed in paranthesis, recursively process them
    for string in substring:
        equation = equation.replace('('+string+')', solve(string))

    # Process all additions
    expr = re.findall(r'(\d+\+[\+\d]+)', equation)
    for i in expr:
        listsum = sum([int(x) for x in i.split('+')])
        equation = equation.replace(i, str(listsum))
    # Process all multiplications
    expr = re.findall(r'(\d+\*[\*\d]+)', equation)
    for i in expr:
        listprod = math.prod([int(x) for x in i.split('*')])
        equation = equation.replace(i, str(listprod))

    return equation

with open('input.txt') as f:
    data = f.readlines()

result = 0
for eq in data:
    result += int(solve(eq.strip().replace(' ','')))

print(f'Answer: {result}')
    