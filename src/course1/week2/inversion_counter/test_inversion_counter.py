import pytest

from inversion_counter import brute_force, sort_and_count


@pytest.mark.parametrize(
    "array",
    [([1, 3, 5, 2, 4, 6]), ([8, 4, 2, 1]), ([8, 4, 2, 1, 500, 12, 80]), ([10]), ([])],
)
def test_count_inversions(array):
    assert sort_and_count(array)[1] == brute_force(array)
