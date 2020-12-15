# Find all combinations of adapters 
# Using tribonacci sequence, assumes no 2 jumps already exist
def adapterchain(adapters):
    combinations = 1
    consecutive = 0

    jolt = 0
    adapters.append(adapters[-1] + 3)
    for adapter in adapters:
        if adapter == jolt + 1:
            consecutive += 1
        elif adapter == jolt + 3:
            if consecutive > 1:
                # Multiply combinations depending on consecutive 1s
                combinations *= int(consecutive*(consecutive-1)/2 + 1)
            consecutive = 0
        jolt = adapter
    return combinations

adapters = []
with open('input.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()

print(f'Combinations: {adapterchain(adapters)}')

