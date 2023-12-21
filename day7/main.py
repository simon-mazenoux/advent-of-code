from dataclasses import dataclass
from enum import Flag, IntEnum
import pathlib
from typing import Iterable, Self
from enum import auto

class Card(Flag):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

d = {
    'A': Card.ACE,
    'K': Card.KING,
    'Q': Card.QUEEN,
    'J': Card.JACK,
    'T': Card.TEN,
    '9': Card.NINE,
    '8': Card.EIGHT,
    '7': Card.SEVEN,
    '6': Card.SIX,
    '5': Card.FIVE,
    '4': Card.FOUR,
    '3': Card.THREE,
    '2': Card.TWO,
}


class HandType(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


@dataclass
class FiveOfAKindHand():

    card: Card
    def __init__(self, hand: str):

    def __lt__(self, other: Self) -> bool:
        return other.hand[0]:


def parse_input(lines: list[str]) -> dict[str, int]:
    return {
        line.split()[0]: int(line.split()[1])
        for line in lines
    }

def get_hand_type(hand: str) -> HandType:
    hand = sorted(hand)
    # Five of a kind
    if len(set(hand)) == 1:
        return HandType.FIVE_OF_A_KIND
    if len(set(hand)) == 2:
        # Four of a kind
        if len(set(hand[:-1])) == 1 or len(set(hand[1:])) == 1:
            return HandType.FOUR_OF_A_KIND
        else: # Full house
            return HandType.FULL_HOUSE
    if len(set(hand)) == 3:
        if len(set(hand[:-2])) == 1 or len(set(hand[2:])) == 1 or len(set(hand[1:-1])) == 1:
            return HandType.THREE_OF_A_KIND
        else: # Two pairs
            return HandType.TWO_PAIRS
    # One pair
    if len(set(hand)) == 4:
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD

def sort_hands_of_the_same_kind(hands: list[str]) -> list[str]:
    return sorted(hands, key=lambda hand: sum(d[card] for card in hand))

def sort_four_of_a_kind(hands: list[str]) -> list[str]:
    # find the card that is part of the four of a kind
    # for this, we pick the card from the middle of the sorted hand

def sort_hands(hands: Iterable[str]) -> list[str]:
    categorised_hands = {
        hand_type: []
        for hand_type in HandType
    }
    for hand in hands:
        categorised_hands[get_hand_type(hand)].append(hand)
    
    sorted_hands = [
        hand
        for hand_type in HandType
        for hand in categorised_hands[hand_type]
    ]
    return sorted_hands[::-1]


def compute_total_winnings(lines):
    bets = parse_input(lines)
    return sum(bets[hand] * i for i, hand in enumerate(sort_hands(bets.keys()), start=1))


if __name__ == '__main__':
    with open(pathlib.Path(__file__).parent / 'input.txt') as f:
        lines = f.readlines()
        print(compute_total_winnings(lines))