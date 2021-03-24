import pytest

import prims

test_case_1 = (0, 0)
test_case_2 = (0, 0)


@pytest.mark.parametrize("data, expected", [test_case_1, test_case_1])
def test_prims(data, expected):
    actual = prims(data)
    assert actual == expected
