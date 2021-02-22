import pytest

from .shortest_path import shortest_path


@pytest.mark.parametrize(
    "target_node, expected_distance", [(0, 0), (1, 1), (2, 2), (3, 2), (4, 1)]
)
def test_shortest_path(target_node, expected_distance):
    graph = {0: [1, 4], 1: [0, 4, 2, 3], 2: [1, 3], 3: [1, 4, 2], 4: [3, 0, 1]}
    actual = shortest_path(graph, target_node)
    assert actual == expected_distance
