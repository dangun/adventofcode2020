
passwords = []
correct_passwords = []

with open('input.txt') as f:
    passwords = f.readlines()

for line in passwords:
    rule, password = line.strip().split(':', 2)

    positions, letter = rule.strip().split(' ', 2)
    positions = [int(x) for x in positions.split('-')]
    if (password[positions[0]] == letter) ^ (password[positions[1]] == letter):
        #print(f'{occurrences} {letter} : {password}')
        correct_passwords.append(password)

print(f'# of correct passwords: {len(correct_passwords)}')
