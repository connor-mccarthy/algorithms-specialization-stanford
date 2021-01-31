import pytest

from karatsuba import karatsuba


@pytest.mark.parametrize(
    "int1, int2",
    [
        (12345, 54321),
        (142123, 198318),
        (12, 42),
        (142, 156),
        (159, 2020),
        (
            3141592653589793238462643383279502884197169399375105820974944592,
            2718281828459045235360287471352662497757247093699959574966967627,
        ),
    ],
)
def test_karatsuba(int1, int2):
    assert karatsuba(int1, int2) == (int1 * int2)
