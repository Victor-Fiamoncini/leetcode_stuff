from src.two_sum import two_sum


def test_two_sum() -> None:
    assert two_sum([2, 3, 4, 6], 5) == [0, 1]
    assert two_sum([2, 3, 4, 6], 10) == [2, 3]
    assert two_sum([2, 3, 4, 6], 12) == [3, 3]

    assert two_sum([2, 3, 4, 6], 13) == []