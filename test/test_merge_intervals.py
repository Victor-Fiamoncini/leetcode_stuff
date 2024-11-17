from src.merge_intervals import merge_intervals


def test_merge_intervals() -> None:
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
