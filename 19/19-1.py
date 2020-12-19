import re

def solve(rules, message, rule):
    if isinstance(rule, str):
        if message and message[0] == rule:
            return message[1:]
        else:
            return 'w'
    results = []
    for x in rule:
        temp_message = message
        for y in x:
            temp_message = solve(rules, temp_message, rules[y])
        if temp_message == '': #optional, skip extra
            return temp_message    
        results.append(temp_message)
    return min(results)

with open('input.txt') as f:
    data = f.read().split('\n\n')

rules = {int(line.split(':')[0]):[[int(x) \
    for x in rule.split(' ') if re.match(r'\d+', x)] \
    for rule in line.split(': ')[1].split(' | ')] \
    for line in data[0].splitlines()}
for rule_number, rule_letter in re.findall(r'(\d+): \"([a-z])', data[0]): 
    rules[int(rule_number)] = rule_letter

messages = [line.strip() for line in data[1].splitlines()]
result = 0
for message in messages:
    if solve(rules, message, rules[0]) == "":
        result += 1

print(f'Answer: {result}')    

