# Find all combinations of adapters 
# Using dynamic programming, checking the previous possibilities
def adapterchain(adapters):
    # Initialize list
    paths = [0] * len(adapters)
    paths[0] = 1

    for i in range(1, len(adapters)):
        path_possibilites = 0
        # Check previous total paths
        for j in range(1, 4):
            # If we are at the beginning, skip
            if i - j < 0:
                continue
            # Add previous path counts to new # of paths
            if adapters[i] - adapters[i - j] <= 3:
                path_possibilites += paths[i - j]
        paths[i] = path_possibilites
    return paths[-1] # Return last 

adapters = []
with open('input.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)

print(f'Combinations: {adapterchain(adapters)}')

