import pytest

from karatsuba import karatsuba


@pytest.mark.parametrize(
    "int1, int2", [(12345, 54321), (142123, 198318), (12, 42), (142, 156), (159, 2020)]
)
def test_karatsuba(int1, int2):
    assert karatsuba(int1, int2) == (int1 * int2)
