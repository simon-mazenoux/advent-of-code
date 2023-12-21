from dataclasses import dataclass
import math
from typing import Iterable


@dataclass
class Race:
    time: int
    record_distance: int


def parse_input(lines: list[str]) -> list[Race]:
    times = int(lines[0].split(":")[1].split())
    distances = int(lines[1].split(":")[1].split())

    return [Race(time, distance) for time, distance in zip(times, distances)]


def parse_input_without_spaces(lines: list[str]) -> Race:
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return Race(time, distance)


def compute_distance_achieved(acceleration_duration: int, race_duration: int) -> int:
    return (race_duration - acceleration_duration) * acceleration_duration


def count_ways_to_beat_record(race: Race) -> int:
    ways = 0
    for acceleration_duration in range(race.time + 1):
        if (
            compute_distance_achieved(acceleration_duration, race.time)
            > race.record_distance
        ):
            ways += 1

    return ways


def compute_margin_of_error(races: Iterable[Race]) -> int:
    return math.prod(count_ways_to_beat_record(race) for race in races)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        races = parse_input(lines)
        print(compute_margin_of_error(races))

        race = parse_input_without_spaces(lines)
        print(count_ways_to_beat_record(race))
