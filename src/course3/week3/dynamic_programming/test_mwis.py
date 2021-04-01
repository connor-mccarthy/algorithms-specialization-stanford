import pytest

from mwis import mwis

input1 = [1, 4, 5, 4]
expected1 = {1, 3}

input2 = [1, 2, 3, 4, 5, 6]
expected2 = {1, 3, 5}

input3 = [1, 2, 6, 6, 6]
expected3 = {0, 2, 4}

input4 = [100, 10, 0, 0, 123, 321]
expected4 = {0, 3, 5}

input5 = [3, 2, 1, 6, 4, 5]
expected5 = {0, 3, 5}


@pytest.mark.parametrize(
    "input_nodes, expected_nodes",
    [
        (input1, expected1),
        (input2, expected2),
        (input3, expected3),
        (input4, expected4),
        (input5, expected5),
    ],
)
def test_mwis(input_nodes, expected_nodes):
    actual = mwis(input_nodes)
    assert actual == expected_nodes
