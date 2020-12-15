
btranslate = {
    ord('B'): ord('1'), 
    ord('F'): ord('0'), 
    ord('R'): ord('1'), 
    ord('L'): ord('0')
    }

def getseatid(bytestring):
    bytestring = bytestring.translate(btranslate)
    return int(bytestring, 2)

with open('input.txt') as f:
    text = f.readlines()

seatids = []

for value in text:
    value = getseatid(value)
    seatids.append(value)

# Highest seat id
print(f'The highest seat id: {max(seatids)}')