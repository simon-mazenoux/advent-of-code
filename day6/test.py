from .main import (
    compute_distance_achieved,
    compute_margin_of_error,
    count_ways_to_beat_record,
    Race,
)


def test_compute_distance_achieved():
    assert compute_distance_achieved(1, 7) == 6
    assert compute_distance_achieved(2, 7) == 10
    assert compute_distance_achieved(3, 7) == 12
    assert compute_distance_achieved(4, 7) == 12
    assert compute_distance_achieved(5, 7) == 10
    assert compute_distance_achieved(6, 7) == 6
    assert compute_distance_achieved(7, 7) == 0


def test_count_ways_to_beat_record():
    assert count_ways_to_beat_record(Race(time=7, record_distance=9)) == 4
    assert count_ways_to_beat_record(Race(time=15, record_distance=40)) == 8
    assert count_ways_to_beat_record(Race(time=30, record_distance=200)) == 9


def test_compute_margin_of_error():
    assert (
        compute_margin_of_error(
            [
                Race(time=7, record_distance=9),
                Race(time=15, record_distance=40),
                Race(time=30, record_distance=200),
            ]
        )
        == 4 * 8 * 9
        == 288
    )
