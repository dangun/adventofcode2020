import math
from collections import deque  

def play(cups):
    
    current = cups[0]
    cups = deque(cups)
    picked = deque([])

    for n in range(100):
        cups.rotate(-1)
        picked.append(cups.popleft())
        picked.append(cups.popleft())
        picked.append(cups.popleft())

        for i in range(1, current+1):
            if current - i in cups:
                desto = cups[cups.index(current - i)]
                break
            elif current - i == 0:
                desto = max(cups)
                break

        desto_index = (cups.index(desto)+1) % len(cups)
        if desto_index == 0:
            cups += picked
        else:
            for i in range(3):
                cups.insert(desto_index+i, picked.popleft())

        current = cups[0]

    return list(cups)

cups = [int(x) for x in '614752839']

cups = play(cups)
print(f'Answer: {"".join([str(i) for i in cups[cups.index(1)+1:] + cups[:cups.index(1)]])}')
