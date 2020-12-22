
def run_round(player1, player2, states):

        if (str(player1) + str(player2)) in states:
            player2.clear()
            return
        else:
            states.add(str(player1) + str(player2))
        
        player1top = player1.pop(0)
        player2top = player2.pop(0)

        if player1top <= len(player1) and player2top <= len(player2):
            player1rec = player1[:player1top]
            player2rec = player2[:player2top]

            game(player1rec, player2rec)

            if player1rec:
                player1 += [player1top, player2top]
            else:
                player2 += [player2top, player1top]

        elif player1top > player2top:
            player1 += [player1top, player2top]
        else:
            player2 += [player2top, player1top]

def game(player1, player2):
    states = set()
    while player1 and player2:
        run_round(player1, player2, states)

def score(player):
    count = 0
    for i, n in enumerate(player):
        count += n * (len(player) - i)
    return count

with open('input.txt') as f:
    data = f.read().split('\n\n')

player1 = [int(x) for x in data[0].splitlines()[1:]]
player2 = [int(x) for x in data[1].splitlines()[1:]]

game(player1, player2)

print(f'Answer: {score(player1 if player1 else player2)}')
