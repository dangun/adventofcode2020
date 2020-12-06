import os

def getquestionsum(group):
    individuals = group.strip().split('\n')
    answers = set(individuals[0])
    for individual_answers in individuals[1:]:
        if not answers:
            break
        answers = answers.intersection(set(individual_answers))
    return len(answers)

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    text = f.read()

group_answers = text.split('\n\n')

answer_sum = 0
for group in group_answers:
    answer_sum += getquestionsum(group)

print(f'Sum of answers with full agreement for each group: {answer_sum}')
