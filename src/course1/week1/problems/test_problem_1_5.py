import pytest

from problem_1_5 import find_second_largest


# problem defined as having input array with unique numbers with length that's a power of two
@pytest.mark.parametrize(
    "unsorted", [(4, 3, 2, 1), (1, 2, 3, 4), (6, 7, 3, 1, 22, 9, 4, 2), (1000, 2000)]
)
def test_find_second_largest(unsorted):
    assert find_second_largest(unsorted) == sorted(unsorted)[-2]
