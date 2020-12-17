import numpy as np

with open('input.txt') as f:
    data = f.readlines()

data = np.array([[0 if x == '.' else 1 for x in line.strip()] for line in data])
data = data[:, :, np.newaxis, np.newaxis]

for i in range(0,6):
    # Pad the data with 0s at every axis
    data = np.pad(data, ((1,1),(1,1),(1,1),(1,1)))
    next_data = np.zeros_like(data)
    it = np.nditer(data, flags=['multi_index'],op_flags=['readonly'])
    while not it.finished:
        (x, y, z, w) = it.multi_index
        # Grab the sum from the relevant area, then update the next one depending on result
        subset_sum = data[max(0,x-1):x+2, max(0,y-1):y+2, max(0,z-1):z+2, max(0,w-1):w+2].sum()
        if data[x,y,z,w] == 1:
            if subset_sum == 3 or subset_sum == 4:
                next_data[x,y,z,w] = 1
        else:
            if subset_sum == 3:
                next_data[x,y,z,w] = 1
        it.iternext()
    data = next_data

print(f'Answer: {data.sum()}')