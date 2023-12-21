import itertools
import pathlib

def compute_number_of_steps(navigation_instructions: str, map: dict[str, tuple[str, str]], start: str = 'AAA', end: str = 'ZZZ') -> int:
    position = start
    for i, direction in enumerate(itertools.cycle(navigation_instructions)):
        if position == end:
            return i
        position = map[position][0] if direction == 'L' else map[position][1]


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as f:
        navigation_instructions = f.readline().strip()
        f.readline()
        map = {}
        for line in f.readlines():
            parts = line.strip().split('=')
            variable_name = parts[0].strip()
            left, right = parts[1].strip().lstrip('(').rstrip(')').split(', ')
            map[variable_name] = (left, right)
        print(navigation_instructions)
        print(map)
        print(compute_number_of_steps(navigation_instructions, map))
