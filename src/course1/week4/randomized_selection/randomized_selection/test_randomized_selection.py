import numpy as np
import pytest

from randomized_selection import randomized_selection


@pytest.mark.parametrize(
    "unsorted",
    [
        ([12, 15, 23, 4, 6, 10, 35, 28]),  # even number of elements
        ([4, 6, 10, 12, 15, 23, 28, 35]),  # already sorted array
        ([12, 15, 23, 4, 6, 10, 35]),  # odd length array
        ([35, 28, 23, 15, 12, 10, 6, 4]),  # descending sorted array input
        ([12]),  # one element
        ([12, 4]),  # two elements
        (
            [
                12,
                15,
                23,
                4,
                6,
                10,
                35,
                28,
                100,
                130,
                500,
                1000,
                235,
                554,
                75,
                345,
                800,
                222,
                333,
                888,
                444,
                111,
                666,
                777,
                60,
            ]
        ),  # large list of elements
        ([12, 15, -23, -4, 6, 10, -35, 28]),  # negative elements
    ],
)
def test_randomized_selection(unsorted):
    select_i = 0 if len(unsorted) == 1 else np.random.randint(0, len(unsorted) - 1)
    expected = randomized_selection(unsorted, select_i)
    actual = sorted(unsorted)[select_i]
    assert actual == expected
