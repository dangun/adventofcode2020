
OP = 0
ARG = 1

def execute(ins_list):
    exhausted = set()
    acc = 0
    i = 0
    while i < len(ins_list): 
        if i in exhausted:
            break
        exhausted.add(i)
        if ins_list[i][OP] == 'nop':
            i += 1
        elif ins_list[i][OP] == 'acc':
            acc += int(ins_list[i][ARG])
            i += 1
        elif ins_list[i][OP] == 'jmp':
            i += int(ins_list[i][ARG])

ins_list = []
with open('input.txt') as f:
    for line in f:
        ins_list.append(tuple(line.split()))

print(f'Accumalator value: {execute(ins_list)}')
