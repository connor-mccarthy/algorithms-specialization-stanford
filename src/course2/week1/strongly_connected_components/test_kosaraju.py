import pytest

from kosaraju import Kosaraju

adj_list1 = [
    [0, 6],
    [1, 4],
    [2, 8],
    [3, 0],
    [4, 7],
    [5, 2, 7],
    [6, 3, 8],
    [7, 1],
    [8, 5],
]
expected1 = [[1, 4, 7], [2, 5, 8], [0, 3, 6]]
adj_list2 = [
    [0, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [3, 4],
    [3, 6],
    [4, 1],
    [4, 5],
    [4, 6],
    [5, 2],
    [5, 7],
    [6, 7],
    [6, 9],
    [7, 6],
    [8, 6],
    [9, 8],
    [9, 10],
    [10, 11],
    [11, 9],
]
expected2 = [[6, 7, 9, 8, 10, 11], [2, 5], [1, 3, 4], [0]]


@pytest.mark.parametrize(
    "adj_list, expected", [(adj_list1, expected1), (adj_list2, expected2)]
)
def test_kosaraju(adj_list, expected):
    kosaraju = Kosaraju(adj_list)
    actual = kosaraju.run()
    for actual_component in actual.values():
        component_found = any(
            set(actual_component) == set(expected_component)
            for expected_component in expected
        )
        assert component_found
