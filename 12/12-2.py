
def move(instructions):
    shipx = 0
    shipy = 0
    waypointx = 10
    waypointy = 1

    for instruction in instructions:
        if instruction[0] == 'N':
            waypointy += instruction[1]
        elif instruction[0] == 'S':
            waypointy -= instruction[1]
        elif instruction[0] == 'E':
            waypointx += instruction[1]
        elif instruction[0] == 'W':
            waypointx -= instruction[1]

        elif instruction[0] == 'F':
            shipx += waypointx*instruction[1]
            shipy += waypointy*instruction[1]

        elif instruction[1] == 180:
            waypointx *= -1
            waypointy *= -1
        
        elif ((instruction[0] == 'R' and instruction[1] == 90) or
            (instruction[0] == 'L' and instruction[1] == 270)):
            temp = waypointy
            waypointy = -waypointx
            waypointx = temp
        elif ((instruction[0] == 'R' and instruction[1] == 270) or
            (instruction[0] == 'L' and instruction[1] == 90)):
            temp = waypointy
            waypointy = waypointx
            waypointx = -temp

    return (shipx, shipy)

instructions = [] # Tuples, (action, value)
with open('input.txt') as f:
    for line in f:
        instructions.append((line[0], int(line[1:])))

shipxy = move(instructions)
print(abs(shipxy[0]) + abs(shipxy[1]))
