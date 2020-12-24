import re
from collections import Counter

with open('input.txt') as f:
    identified = []
    for line in f.readlines():
        matches = re.findall(r'(sw|se|nw|ne|e|w)', line)
        counter = Counter(matches)
        identified.append((
            0.5*counter['se']+0.5*counter['ne']+counter['e']-counter['w']-0.5*counter['sw']-0.5*counter['nw'],
            float(counter['nw']+counter['ne']-counter['sw']-counter['se'])
        ))

print(f'Answer: {sum([x % 2 for x in Counter(identified).values() if x % 2 == 1])}')
