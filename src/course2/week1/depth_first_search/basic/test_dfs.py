from dfs import dfs


def test_dfs():
    graph = {0: [1, 4], 1: [0, 4, 2, 3], 2: [1, 3], 3: [1, 4, 2], 4: [3, 0, 1]}
    raw_actual = dfs(graph)
    is_explored_list = [v["is_explored"] for _, v in raw_actual.items()]
    assert all(is_explored_list)
