from bfs import bfs


def test_bfs():
    graph = {0: [1, 4], 1: [0, 4, 2, 3], 2: [1, 3], 3: [1, 4, 2], 4: [3, 0, 1]}
    raw_actual = bfs(graph)
    is_explored_list = [v["is_explored"] for _, v in raw_actual.items()]
    assert all(is_explored_list)
