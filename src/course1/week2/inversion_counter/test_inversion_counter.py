import pytest

from inversion_counter import brute_force, inversion_counter


@pytest.mark.parametrize(
    "array",
    [([1, 3, 5, 2, 4, 6]), ([8, 4, 2, 1]), ([8, 4, 2, 1, 500, 12, 80]), ([10]), ([])],
)
def test_count_inversions(array):
    assert inversion_counter(array)[1] == brute_force(array)
