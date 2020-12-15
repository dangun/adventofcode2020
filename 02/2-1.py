 
passwords = []
correct_passwords = []

with open('input.txt') as f:
    passwords = f.readlines()

for line in passwords:
    rule, password = line.strip().split(':', 2)

    occurrences, letter = rule.strip().split(' ', 2)
    occurrences = [int(x) for x in occurrences.split('-')]
    letter_count = password.count(letter)
    if letter_count >= occurrences[0] and letter_count <= occurrences[1]:
        correct_passwords.append(password)

print(f'# of correct passwords: {len(correct_passwords)}')
