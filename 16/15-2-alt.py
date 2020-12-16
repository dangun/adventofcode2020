import re

# Check if a ticket is valid
def check_valid(ticket, valid_ranges):
    for number in ticket:
        valid = False
        for valid_range in valid_ranges:
            if number in valid_range:
                valid = True
                break
        if not valid:
            return False
    return True

def find_fields(tickets, fields):
    # Adds all possible answers for each field independently
    fields_index = {key: list(range(0,len(fields))) for key in fields}
    for field in fields_index:
        for ticket in tickets:
            for i, number in enumerate(ticket):
                if i in fields_index[field] and \
                    number not in fields[field][0] and number not in fields[field][1]:
                    fields_index[field].remove(i)

    # Reduces each field's possible value to one single value
    modified = True
    while modified:
        modified = False
        for field1 in fields:
            if len(fields_index[field1]) == 1:
                for field2 in fields:
                    if field1 != field2 and fields_index[field1][0] in fields_index[field2]:
                        modified = True
                        fields_index[field2].remove(fields_index[field1][0])
    return fields_index

with open('input.txt') as f:
    data = f.read().split('\n\n')

fields = {field:[range(int(a),int(b)+1), range(int(c),int(d)+1)] \
    for field,a,b,c,d in re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', data[0])}

# Store our ticket
myticket = list(map(int, data[1].splitlines()[1].split(',')))

# Store all tickets, but only if the ticket is valid
tickets = []
for line in data[2].splitlines()[1:]:
    ticket = list(map(int, line.split(',')))
    if check_valid(ticket, sum(fields.values(), [])):
        tickets.append(ticket)

# Answer
answer = 1
fields_index = find_fields(tickets, fields)
for field in fields_index:
    if field.split(' ')[0] == 'departure':
        answer *= myticket[fields_index[field][0]]

print(f'Answer: {answer}')
