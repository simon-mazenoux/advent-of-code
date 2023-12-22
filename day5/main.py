import pathlib



def get_mapping(map: list[tuple[int, int, int]], seeds: list[int]) -> list[int]:
    return [0 for _ in range(len(seeds))]

def get_lowest_location_number(lines: list[str]) -> int:
    return 0

if __name__ == '__main__':
    with open(pathlib.Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()
        print(f'Lowest location number: {get_lowest_location_number(lines)}')