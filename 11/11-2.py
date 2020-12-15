import numpy as np

def process(seats):

    rowrange = range(len(seats))
    colrange = range(len(seats[0]))
    
    while True:
        change_matrix = np.ones_like(seats)
        # Check first seat in all 8 directions
        for row in rowrange:
            for col in colrange:
                if seats[row][col] == 0:
                    continue
                occupied = 0 
                for i in (-1, 0, 1):    
                    for j in (-1, 0, 1):
                        if (row + i in rowrange and 
                            col + j in colrange and 
                            not i == j == 0):

                            step = 1
                            while row+step*i in rowrange and col+step*j in colrange:
                                if seats[row+step*i][col+step*j] == 1:
                                    occupied += 1
                                    break
                                elif seats[row+step*i][col+step*j] == -1:
                                    break
                                step += 1
                if (occupied == 0 and seats[row][col] == -1) or (occupied >= 5 and seats[row][col] == 1):
                    change_matrix[row][col] = -1

        # Check if nothing is gonna change, if yes then return the sum of all occupied seats
        if np.isin(change_matrix, 1).all():
            return (seats == 1).sum()
        seats = change_matrix * seats # Multiply each corresponding element
    
seats = [] # 0 = floor, 1 = occupied, -1 = empty
with open('input.txt') as f:
    row = []
    for line in f:
        row =  [-1 if x == 'L' else 0 for x in line.strip()] 
        seats.append(row)

seats = np.array(seats)

print(f'# of occupied seats: {process(seats)}')
