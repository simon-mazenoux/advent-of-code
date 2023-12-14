


from .main import compute_sum_of_part_numbers, has_special_around, is_special, pad_matrix, get_number_position, get_part_numbers,transform_lines_to_matrix

def test_is_special():
    assert not is_special('1')
    assert not is_special('2')
    assert not is_special('3')
    assert not is_special('4')
    assert not is_special('5')
    assert not is_special('6')
    assert not is_special('7')
    assert not is_special('8')
    assert not is_special('9')
    assert not is_special('0')
    assert not is_special('.')
    assert is_special('*')
    assert is_special('#')
    assert is_special('$')
    assert is_special('+')


def test_has_special_around_negative_case():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '.']
    ]
    assert not has_special_around(matrix, 1, 1, 3)

def test_has_special_around_left_case():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['#', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '.']
    ]
    assert has_special_around(matrix, 1, 1, 2)


def test_has_special_around_right_case():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '#'],
        ['.', '.', '.', '.', '.']
    ]
    assert has_special_around(matrix, 1, 1, 3)

def test_has_special_around_top_case():
    matrix = [
        ['.', '#', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '.']
    ]
    assert has_special_around(matrix, 1, 1, 3)

def test_has_special_around_bottom_case():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '#', '.']
    ]
    assert has_special_around(matrix, 1, 1, 3)

def test_has_special_around_top_left_case():
    matrix = [
        ['#', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '.']
    ]
    assert has_special_around(matrix, 1, 1, 3)

def test_has_special_around_bottom_right_case():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '#']
    ]
    assert has_special_around(matrix, 1, 1, 3)


def test_transform_lines_to_matrix():
    lines = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]
    matrix = [
        ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
        ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
        ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
        ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
        ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
        ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.'],
    ]
    assert transform_lines_to_matrix(lines) == matrix

def test_pad_matrix():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '.']
    ]
    padded_matrix = [
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '2', '3', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    assert pad_matrix(matrix) == padded_matrix


def test_get_number_position_easy():
    matrix = [
        ['.', '.', '.', '.', '.'],
        ['.', '1', '2', '3', '.'],
        ['.', '.', '.', '.', '.']
    ]
    assert get_number_position(matrix) == {(1, 1): 123}

def test_get_number_position_difficult():
    matrix = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '4', '6', '7', '.', '.', '1', '1', '4', '.', '.', '.'],
        ['.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '3', '5', '.', '.', '6', '3', '3', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
        ['.', '6', '1', '7', '*', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '+', '.', '5', '8', '.', '.'],
        ['.', '.', '.', '5', '9', '2', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '7', '5', '5', '.', '.'],
        ['.', '.', '.', '.', '$', '.', '*', '.', '.', '.', '.', '.'],
        ['.', '.', '6', '6', '4', '.', '5', '9', '8', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    assert get_number_position(matrix) == {(1, 1): 467,
        (1, 6): 114,
        (3, 3): 35,
        (3, 7): 633,
        (5, 1): 617,
        (6, 8): 58,
        (7, 3): 592,
        (8, 7): 755,
        (10, 2): 664,
        (10, 6): 598
    }

def test_get_part_numbers():
    lines = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]

    assert get_part_numbers(lines) == [467, 35, 633, 617, 592, 755, 664, 598]




def test_compute_sum_of_parts_numbers():
    
    lines = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]

    assert compute_sum_of_part_numbers(lines) == 4361
