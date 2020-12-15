# Find chain that contains all adapters, 
def adapterchain(adapters):
    diff = [0, 0, 0]
    jolt = 0
    for adapter in adapters:
        if jolt < adapter <= jolt + 3: 
            diff[adapter - jolt - 1] += 1
            jolt = adapter
    diff[2] += 1 # Add final device jump
    return diff[0] * diff[2]

adapters = []
with open('input.txt') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()
print(f'Product of # 1 jolt jumps and 3 jolt jumps: {adapterchain(adapters)}')

