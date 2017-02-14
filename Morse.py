#!/usr/bin/python

# This is a script to parse a line of input and convert to Morse Code

# Get a string from the user

input_string = raw_input("MESSAGE: ")

# Define morse code key mappings. From
# http://thelivingpearl.com/2013/01/08/morse-code-and-dictionaries-in-python-with-sound/

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
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

for c in input_string:
    # If space insert spaces
    if c == ' ':
        print ' '*7,
    # If alpha-num insert corresponding code
    if c.isalnum():
        print CODE[c.upper()],

    # If space insert /
    # If alpha-num insert relevant morse code keycode
# Insert space
