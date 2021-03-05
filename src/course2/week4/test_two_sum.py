import pytest

from two_sum import brute_force, hash_table_2_sum, sorted_array


@pytest.mark.parametrize(
    "implementation", [brute_force, sorted_array, hash_table_2_sum]
)
@pytest.mark.parametrize(
    "array, t, expected",
    [
        ([1, 2, 3], 4, [(1, 3)]),
        ([10, 6, 9, 7, 3], 16, [(6, 10), (7, 9)]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, [(1, 9), (2, 8), (3, 7), (4, 6)]),
    ],
)
def test_two_sum(implementation, array, t, expected):
    actual = implementation(array, t)
    for pair in actual:
        assert tuple(sorted(pair)) in expected
