import sys
import os

btranslate = {
    ord('B'): ord('1'), 
    ord('F'): ord('0'), 
    ord('R'): ord('1'), 
    ord('L'): ord('0')
    }

def getseatid(bytestring):
    bytestring = bytestring.translate(btranslate)
    return int(bytestring, 2)

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    text = f.readlines()

seatids = []

for value in text:
    value = getseatid(value)
    seatids.append(value)

missing = sum(range(min(seatids),max(seatids)+1)) - sum(seatids)

# If 0, then it is either end of the seatids
print(f'The missing seat id: {missing}')
