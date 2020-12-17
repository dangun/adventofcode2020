
# Check if a ticket is valid
def check_valid(ticket, valid_ranges):
    for number in ticket:
        valid = False
        for valid_range in valid_ranges:
            valid |= number in valid_range
            if valid:
                break
        if not valid:
            return False
    return True

def find_fields(tickets, fields):
    # Adds all possible answers for each field independently
    fields_index = {key: [] for key in fields}
    for field in fields:
        for j in range(len(tickets[0])):
            possible_index = True
            for ticket in tickets:
                if not (ticket[j] in fields[field][0] or ticket[j] in fields[field][1]):
                    possible_index = False
                    break
            if possible_index:
                fields_index[field].append(j)

    # Reduces each field's possible value to one single value
    while True:
        modified = False
        for field1 in fields:
            if len(fields_index[field1]) == 1:
                for field2 in fields:
                    if field1 != field2 and fields_index[field1][0] in fields_index[field2]:
                        modified = True
                        fields_index[field2].remove(fields_index[field1][0])
        if not modified:
            break
    return fields_index

with open('input.txt') as f:
    data = f.read().split('\n\n')

# Store field names and ranges, and all valid ranges
fields = {}
valid_ranges = []
for line in data[0].splitlines():
    field_data = line.split(': ')
    fields[field_data[0]] = []
    for range_values in field_data[1].split(' or '):
        range_values = range_values.split('-')
        valid_ranges.append(range(int(range_values[0]), int(range_values[1])+1))
        fields[field_data[0]].append(valid_ranges[-1])

# Store our ticket
myticket = list(map(int, data[1].splitlines()[1].split(',')))

# Store all tickets, but only if the ticket is valid
tickets = []
for line in data[2].splitlines()[1:]:
    ticket = list(map(int, line.split(',')))
    if check_valid(ticket, valid_ranges):
        tickets.append(ticket)

# Answer
answer = 1
fields_index = find_fields(tickets, fields)
for field in fields_index:
    if field.split(' ')[0] == 'departure':
        answer *= myticket[fields_index[field][0]]

print(f'Answer: {answer}')
