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

    # Get all numbers and operands, apply them one by one from the left
    expr = re.findall(r'(\d+|\*|\+)', equation)
    result = int(expr[0])
    operand = ''
    for i in expr[1:]:
        if i == '*' or i == '+':
            operand = i
        else:
            if operand == '*':
                result *= int(i)
            elif operand == '+':
                result += int(i)

    return str(result)

with open('input.txt') as f:
    data = f.readlines()

result = 0
for eq in data:   
    result += int(solve(eq.strip()))

print(f'Answer: {result}')
    

