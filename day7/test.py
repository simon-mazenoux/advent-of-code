

from .main import HandType, compute_total_winnings, sort_hands,get_hand_type

def test_get_hand_type():
    assert get_hand_type('KKKKK') == HandType.FIVE_OF_A_KIND
    assert get_hand_type('AQQQQ') == HandType.FOUR_OF_A_KIND
    assert get_hand_type('QQQQJ') == HandType.FOUR_OF_A_KIND
    assert get_hand_type('KKQQQ') == HandType.FULL_HOUSE
    assert get_hand_type('QQQJJ') == HandType.FULL_HOUSE
    assert get_hand_type('AKQQQ') == HandType.THREE_OF_A_KIND
    assert get_hand_type('KQQQJ') == HandType.THREE_OF_A_KIND
    assert get_hand_type('QQQJT') == HandType.THREE_OF_A_KIND
    assert get_hand_type('KQQJJ') == HandType.TWO_PAIRS
    assert get_hand_type('KKQJJ') == HandType.TWO_PAIRS
    assert get_hand_type('KKQQJ') == HandType.TWO_PAIRS
    assert get_hand_type('KKQJT') == HandType.ONE_PAIR
    assert get_hand_type('KQQJT') == HandType.ONE_PAIR
    assert get_hand_type('KQJJT') == HandType.ONE_PAIR
    assert get_hand_type('KQJTT') == HandType.ONE_PAIR
    assert get_hand_type('AKQJT') == HandType.HIGH_CARD


def test_sort_hands():
    hands = [
        '32T3K',
        'T55J5',
        'KK677',
        'KTJJT',
        'QQQJA'
    ]

    assert sort_hands(hands) == [
        'QQQJA',
        'T55J5',
        'KK677',
        'KTJJT',
        '32T3K'
    ]

def test_compute_total_winnings():
    lines = [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
    ]

    assert compute_total_winnings(lines) == 765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5 == 6440

