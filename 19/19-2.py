import re

def solve(message, queue):
    # If empty message and empty queue, valid string
    if not message and not queue:
        return True
    # Empty string with rules remaining or no more rules, invalid string
    elif (not message and queue) or not queue:
        return False
    # Get the next rule set
    next_rule = rules[queue[0]]
    if isinstance(next_rule, str):
        if message[0] == next_rule: # Process one character
            return solve(message[1:], queue[1:])
        else: # Wrong character match, invalid string
            return False
    # Check if any branch of rules is true, expand and call rules from the left
    return any(solve(message, rule + queue[1:]) for rule in next_rule)

with open('input.txt') as f:
    data = f.read().split('\n\n')

# Process as a dictionary of rules, each list inside is a branch, rule = [[sequence][sequence]]
rules = {int(line.split(':')[0]):[[int(x.strip()) \
    for x in rule.strip().split(' ') if re.match(r'\d+', x)] \
    for rule in line.split(':')[1].split('|')] \
    for line in data[0].splitlines()}

# Find letter rules to process, no lists
for rule_number, rule_letter in re.findall(r'(\d+): \"([a-z])', data[0]): 
    rules[int(rule_number)] = rule_letter

messages = [line.strip() for line in data[1].splitlines()]

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

result = 0
for message in messages:
    if solve(message, [0]):
        result += 1

print(f'Answer: {result}')    

