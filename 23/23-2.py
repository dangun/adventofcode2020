from collections import deque  
from collections import defaultdict

def play(cups):

    cups = deque(cups)
    pseudo_insert = defaultdict(list)

    def next():
        next_value = cups.popleft()
        if next_value in pseudo_insert:
            cups.extendleft(pseudo_insert[next_value][::-1])
            del pseudo_insert[next_value]
        return next_value

    for n in range(10000000):
        current = next()
        picked = [next(), next(), next()]

        desto = current
        while desto in picked or desto == current:
            desto -= 1
            if desto < 1:
                desto = 1000000
        
        pseudo_insert[desto] += picked
        cups.append(current)

    while (next_value := next()) != 1:
        cups.append(next_value)

    return next() * next()

cups = [int(x) for x in '614752839']
cups += list(range(max(cups)+1, 1000000+1))

print(f'Answer: {play(cups)}')
