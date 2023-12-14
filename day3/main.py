from collections import defaultdict
import math
import pathlib

def transform_lines_to_matrix(lines):
    # Split each line into a list of characters
    matrix = [list(line) for line in lines]

    return matrix

def pad_matrix(matrix):
    # Get the dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Create a new matrix with additional rows and columns
    padded_matrix = [['.' for _ in range(cols + 2)] for _ in range(rows + 2)]

    # Copy the original matrix into the center of the padded matrix
    for i in range(rows):
        for j in range(cols):
            padded_matrix[i + 1][j + 1] = matrix[i][j]

    return padded_matrix

def get_number_position2(matrix: list[list[str]]) -> dict[tuple[int, int], int]:

    # We start at the top left corner
    d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j].isnumeric():
                left = j
                right = j
                while matrix[i][right].isnumeric():
                    right += 1
                v = int(''.join(matrix[i][left:right]))
                d[(i, j)] = v

                for k in range(left, right):
                    matrix[i][k] = '.'

    return d

def get_number_position(matrix: list[list[str]]) -> dict[tuple[int, int], int]:

    # We start at the top left corner
    d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j].isnumeric():
                left = j
                right = j
                while matrix[i][right].isnumeric():
                    right += 1
                v = int(''.join(matrix[i][left:right]))
                d[(i, j)] = v

                for k in range(left, right):
                    matrix[i][k] = '.'

    return d

def is_special(c: str) -> bool:
    return not (c.isnumeric() or c == '.')

def has_special_around(grid: list[list[str]], i: int, left: int, right) -> bool:
    return (
        is_special(grid[i][left-1]) or 
        is_special(grid[i][right+1]) or
        any(is_special(grid[i-1][k]) for k in range(left-1, right+2)) or
        any(is_special(grid[i+1][k]) for k in range(left-1, right+2))
    )



def get_part_numbers(lines: list[str]) -> list[int]:
    # Transforn the lines into a matrix
    # We pad the matrix with '.' to avoid edge cases
    matrix = transform_lines_to_matrix(lines)
    matrix = pad_matrix(lines)
    d = get_number_position(matrix)

    numbers = []
    for (i, j), v in d.items():
        if has_special_around(matrix, i, j, j+len(str(v))-1):
            print(f'Found a special at {i}, {j}')
            numbers.append(v)
    return numbers

def compute_sum_of_part_numbers(lines) -> int:
    return sum(get_part_numbers(lines))


def get_gear_ratios(lines: list[str]) -> list[int]:
    matrix = transform_lines_to_matrix(lines)
    grid = pad_matrix(matrix)
    d = get_number_position(grid)

    dd = defaultdict(list)
    for (i, j), v in d.items():
        left = j
        right = j+len(str(v))-1
        if grid[i][left-1] == '*':
            dd[(i, left-1)].append(v)
        if grid[i][right+1] == '*':
            dd[(i, right+1)].append(v)
        for k in range(left-1, right+2):
            if grid[i-1][k] == '*':
                dd[(i-1, k)].append(v)
        for k in range(left-1, right+2):
            if grid[i+1][k] == '*':
                dd[(i+1, k)].append(v)
    return [math.prod(v) for v in dd.values() if len(v) == 2]

def compute_sum_of_gear_ratios(lines) -> int:
    return sum(get_gear_ratios(lines))

if __name__ == '__main__':
    with open(pathlib.Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()
        # remove newline characters
        lines = [line.rstrip('\n') for line in lines]
        remove = ['\n', ' ']
        print(f'Sum of part numbers: {compute_sum_of_part_numbers(lines)}')
        print(f'Sum of gear ratios: {compute_sum_of_gear_ratios(lines)}')