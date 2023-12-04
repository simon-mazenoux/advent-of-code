#!/usr/bin/env python

import pathlib


def is_possible(line : str) -> bool:
    line = line.split(': ')[1].strip()

    for set in line.split('; '):
        d = {'red': 0, 'blue': 0, 'green': 0}
        for color in set.split(', '):
            v, color = color.split(' ')
            d[color] += int(v)

        if not (d['red'] <= 12 and d['green'] <= 13 and d['blue'] <= 14):
            return False

    return True

def sum_possible_ids(lines):
    return sum(i for i, line in enumerate(lines, 1) if is_possible(line))

def compute_power_of_cubes(line) -> int:

    d = {'red': 0, 'blue': 0, 'green': 0}
    line = line.split(': ')[1].strip()

    for set in line.split('; '):
        for color in set.split(', '):
            v, color = color.split(' ')
            d[color] = max(int(v), d[color])

    return d['red'] * d['green'] * d['blue']

def sum_cubes(lines):
    return sum(compute_power_of_cubes(line) for line in lines)

if __name__ == '__main__':
    with open(pathlib.Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()
        print(f'Sum of possible ids: {sum_possible_ids(lines)}')
        print(f'Sum of cubes: {sum_cubes(lines)}')