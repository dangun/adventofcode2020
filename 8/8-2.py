import os

OP = 0
ARG = 1

def execute(ins_list, change):
    exhausted = set()
    acc = 0
    i = 0
    while i < len(ins_list): 
        if i in exhausted:
            break
        exhausted.add(i)
        if ins_list[i][OP] == 'nop':
            if i == change: # Do a jmp instead
                i += int(ins_list[i][ARG])
            else:
                i += 1
        elif ins_list[i][OP] == 'jmp':
            if i == change: # Do a nop instead
                i += 1
            else:
                i += int(ins_list[i][ARG])
        elif ins_list[i][OP] == 'acc':
            acc += int(ins_list[i][ARG])
            i += 1
    return (i, acc)

ins_list = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    for line in f:
        ins_list.append(tuple(line.split()))

change = 0
while change < len(ins_list): 
    if ins_list[change][OP] != 'acc':
        result = execute(ins_list, change)
        if result[0] == len(ins_list):
            print(f'Successful, index changed: {change}')
            print(f'Accumalator value: {result[1]}')
            break
    change += 1