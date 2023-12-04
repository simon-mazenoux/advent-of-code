from .main import compute_power_of_cubes, is_possible, sum_cubes, sum_possible_ids

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
def test_is_possble_valid():
    assert is_possible('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert is_possible('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
    assert is_possible('Game 3: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')


# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
def test_is_possble_invalid():
    assert not is_possible('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
    assert not is_possible('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')


def test_sum_possible_ids():
    lines = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]
    assert sum_possible_ids(lines) == 1 + 2 + 5 == 8

def test_compute_sum_of_cubes():
    assert compute_power_of_cubes('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')  == 4 * 2 * 6 == 48
    assert compute_power_of_cubes('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == 12
    assert compute_power_of_cubes('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == 1560
    assert compute_power_of_cubes('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == 630
    assert compute_power_of_cubes('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == 36

def test_sum_cubes():
    lines = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]
    assert sum_cubes(lines) == 48 + 12 + 1560 + 630 + 36 == 2286
