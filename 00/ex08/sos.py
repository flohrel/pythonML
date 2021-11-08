import sys
import string

morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def to_morse(s):
    return ' '.join(morse.get(i.upper()) for i in s)

lst = []
if len(sys.argv) < 2:
    exit()
else:
    for arg in sys.argv[1:]:
        for char in arg:
            if char in string.punctuation:
                print("ERROR")
                exit()
        lst += arg.split(' ')
print(' / '.join(to_morse(word) for word in lst))