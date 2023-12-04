#!/bin/python

import pathlib

SPELLED_NUMBERS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine' : 9,
}

def compute(lines: list[str]) -> int:
    total = 0
    for line in lines:
        for i, c in enumerate(line):
            if c.isnumeric():
                a = c
                break
            else:
                break_loop = False
                for spelled_number, value in SPELLED_NUMBERS.items():
                    if line[i:].startswith(spelled_number):
                        a = value
                        break_loop = True
                        break
                if break_loop:
                    break

        
        for i, c in reversed(list(enumerate(line))):
            if c.isnumeric():
                b = c
                break
            else:
                break_loop = False
                for spelled_number, value in SPELLED_NUMBERS.items():
                    if line[i:].startswith(spelled_number):
                        b = value
                        break_loop = True
                        break
                if break_loop:
                    break
        
        total += int(f'{a}{b}')
    
    return total

if __name__ == '__main__':
    with open(pathlib.Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()
        print(compute(lines))
