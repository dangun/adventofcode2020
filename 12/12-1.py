import os

def move(instructions):
    shipx = 0
    shipy = 0
    xdir = 1
    ydir = 0

    for instruction in instructions:
        if instruction[0] == 'N':
            shipy += instruction[1]
        elif instruction[0] == 'S':
            shipy -= instruction[1]
        elif instruction[0] == 'E':
            shipx += instruction[1]
        elif instruction[0] == 'W':
            shipx -= instruction[1]

        elif instruction[0] == 'F':
            shipx += xdir*instruction[1]
            shipy += ydir*instruction[1]

        elif instruction[1] == 180:
            xdir *= -1
            ydir *= -1
        
        elif ((instruction[0] == 'R' and instruction[1] == 90) or
            (instruction[0] == 'L' and instruction[1] == 270)):
            if xdir:
                ydir = -xdir
                xdir = 0
            else:
                xdir = ydir
                ydir = 0
        elif ((instruction[0] == 'R' and instruction[1] == 270) or
            (instruction[0] == 'L' and instruction[1] == 90)):
            if xdir:
                ydir = xdir
                xdir = 0
            else:
                xdir = -ydir
                ydir = 0

    return (shipx, shipy)

instructions = [] # Tuples, (action, value)
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    for line in f:
        instructions.append((line[0], int(line[1:])))

shipxy = move(instructions)
print(abs(shipxy[0]) + abs(shipxy[1]))
