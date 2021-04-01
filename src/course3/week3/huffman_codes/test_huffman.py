import pytest

from huffman import huffman

input1 = [60, 25, 10, 5]
expected1 = {0: "1", 1: "01", 2: "001", 3: "000"}

input2 = [3, 2, 6, 8, 2, 6]
expected2 = {0: "000", 1: "0010", 2: "10", 3: "01", 4: "0011", 5: "11"}


@pytest.mark.parametrize(
    "input_data, expected", [(input1, expected1), (input2, expected2)]
)
def test_huffman(input_data, expected):
    actual = huffman(input_data)
    print(actual)
    print(expected)
    for i, weight in enumerate(input_data):
        assert actual[i] == expected[i]
