import numpy as np
import pytest
from numpy.random import default_rng

from strassens import strassens

rng = default_rng()


@pytest.mark.parametrize(
    "matrix1, matrix2",
    [
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[5, 6], [7, 8]]),
        ),
        (
            np.random.randint(0, 1000, size=(4, 4)),
            np.random.randint(0, 1000, size=(4, 4)),
        ),
        (
            np.random.randint(0, 1000, size=(16, 16)),
            np.random.randint(0, 1000, size=(16, 16)),
        ),
    ],
)
def test_count_inversions(matrix1, matrix2):
    actual = strassens(matrix1, matrix2)
    expected = matrix1 @ matrix2
    assert np.array_equal(actual, expected)
