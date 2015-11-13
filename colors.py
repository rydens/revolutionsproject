"""Solarized color terminal.

This module contains some mappings for the ANSI terminal escapes support
the 16 colors of the Solarized color palette created by Ethan Schoonover.
"""

base03  = '\033[1;30m'
BASE03  = base03
B03     = base03
b03     = base03

base02  = '\033[0;30m'
BASE02  = base02
B02     = base02
b02     = base02

base01  = '\033[1;32m'
BASE01  = base01
B01     = base01
b01     = base01

base00  = '\033[1;33m'
BASE00  = base00
B00     = base00
b00     = base00
white   = base00

base0   = '\033[1;34m'
BASE0   = base0
B0      = base0
b0      = base0

base1   = '\033[1;36m'
BASE1   = base1
B1      = base1
b1      = base1

base2   = '\033[0;37m'
BASE2   = base2
B2      = base2
b2      = base2

base3   = '\033[1;37m'
BASE3   = base3
B3      = base3
b3      = base3

yellow  = '\033[0;33m'
YELLOW  = yellow
Y       = yellow
y       = yellow

orange  = '\033[1;31m'
ORANGE  = orange
O       = orange
o       = orange

red     = '\033[0;31m'
RED     = red 
R       = red 
r       = red 

magenta = '\033[0;35m'
MAGENTA = magenta
M       = magenta
m       = magenta

violet  = '\033[1;35m'
VIOLET  = violet
V       = violet
v       = violet

blue    = '\033[0;34m'
BLUE    = blue
B       = blue
b       = blue

cyan    = '\033[0;36m'
C       = cyan
c       = cyan

green   = '\033[0;32m'
G       = green
g       = green

reset   = '\033[0m'
RESET   = reset
X       = '\033[0m'
x       = '\033[0m'

conceil = '\033[0;8m'
CONCEIL = conceil

clear   = '\033[H\033[2J'
CLEAR   = clear
CL      = clear
cl      = clear

import random as rand
def random_color():
    return rand.choice([yellow, orange, red, magenta, violet, blue, cyan, green])
rc = random_color
random = random_color

def multi(text):
    """Prints text with each character a random color.
    
    Args:
        text (str): The text to print.

    """
    buf = ''
    for char in text:
        buf += rc() + char + x
    return buf

def merica(text):
    """Prints the most patiotic text possible.

    Args:
        text (str): The text to print

    """

    buf = ''
    the_best_colors_in_the_whole_world = [red,white,blue]
    i = 0
    for char in text:
        buf += the_best_colors_in_the_whole_world[i] + char
        i += 1
        if i == 3: i = 0
    buf += reset
    return buf

def clear_screen():
    """(Deprecated) Clears the screen"""
    print(clear,end='')
cs = clear_screen
clears = clear_screen

if __name__ == '__main__':
    print(clear)
    print(base03 + 'Base03' + reset, end=' ')
    print(base02 + 'Base02' + reset, end=' ')
    print(base01 + 'Base01' + reset, end=' ')
    print(base00 + 'Base00' + reset, end=' ')
    print(base0 + 'Base0' + reset, end=' ')
    print(base1 + 'Base1' + reset, end=' ')
    print(base2 + 'Base2' + reset, end=' ')
    print(base3 + 'Base3' + reset, end=' ')

    print()

    print(yellow + 'Yellow' + reset, end=' ')
    print(orange + 'Orange' + reset, end=' ')
    print(red + 'Red' + reset, end=' ')
    print(magenta + 'Magenta' + reset, end=' ')
    print(violet + 'Violet' + reset, end=' ')
    print(blue + 'Blue' + reset, end=' ')
    print(cyan + 'Cyan' + reset, end=' ')
    print(green + 'Green' + reset, end=' ')

    print()

    for count in range(7):
        print(random_color() + 'Random' + reset, end=' ')
    print()

    print()

    print(multi("multicolor"))
