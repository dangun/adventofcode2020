import os

def getquestionsum(group):
    answers = []
    for symbol in group:
        if symbol != '\n':
            answers.append(symbol)
    return len(set(answers))

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    text = f.read()

group_answers = text.split('\n\n')

answer_sum = 0
for group in group_answers:
    answer_sum += getquestionsum(group)

print(f'Sum of answers unique for each group: {answer_sum}')
