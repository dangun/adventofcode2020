
def loopsize(key):
    value = 1
    subject_number = 7
    loop = 0
    while True:
        loop += 1
        value *= subject_number
        value %= 20201227
        if value == key:
            break
    return loop
        
def encryptionkey(key, loopsize):
    value = 1
    for i in range(loopsize):
        value *= key
        value %= 20201227
    return value

with open('input.txt') as f:
    data = f.readlines()
    
cardpub = int(data[0])
doorpub = int(data[1])

print(f'Answer: {encryptionkey(doorpub, loopsize(cardpub))}')
