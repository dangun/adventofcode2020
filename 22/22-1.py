
def play(player1, player2):
    if player1[0] > player2[0]:
        player1 += [player1.pop(0), player2.pop(0)]
    else:
        player2 += [player2.pop(0), player1.pop(0)]

def score(player):
    count = 0
    for i, n in enumerate(player):
        count += n * (len(player) - i)
    return count

with open('input.txt') as f:
    data = f.read().split('\n\n')

player1 = [int(x) for x in data[0].splitlines()[1:]]
player2 = [int(x) for x in data[1].splitlines()[1:]]

while player1 and player2:
    play(player1, player2)

print(f'Answer: {score(player1 if player1 else player2)}')
