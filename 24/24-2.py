import re
from collections import Counter

adjacent = [(-1, 0), (1, 0), (-0.5, -1), (-0.5, 1), (0.5, -1), (0.5, 1)]

def step(state):

    add_list = set()
    remove_list = set()

    for pos in state:
        count = 0
        for xy1 in adjacent:
            if (pos[0] + xy1[0], pos[1] + xy1[1]) in state:
                count += 1
            else:
                counter = 0
                for xy2 in adjacent:
                    if (pos[0] + xy1[0] + xy2[0], pos[1] + xy1[1] + xy2[1]) in state:
                        counter += 1
                if counter == 2:
                    add_list.add((pos[0] + xy1[0], pos[1] + xy1[1]))
        if count == 0 or count > 2:
            remove_list.add(pos)

    state = state.union(add_list)
    state = state.difference(remove_list)
    return state

with open('input.txt') as f:
    identified = []
    for line in f.readlines():
        matches = re.findall(r'(sw|se|nw|ne|e|w)', line)
        counter = Counter(matches)
        identified.append((
            0.5*counter['se']+0.5*counter['ne']+counter['e']-counter['w']-0.5*counter['sw']-0.5*counter['nw'],
            float(counter['nw']+counter['ne']-counter['sw']-counter['se'])
        ))

counter = Counter(identified)
state = set([pos for pos in counter if counter[pos] % 2 == 1])
for day in range(100):
    state = step(state)
print(f'Answer: {len(state)}')
    
