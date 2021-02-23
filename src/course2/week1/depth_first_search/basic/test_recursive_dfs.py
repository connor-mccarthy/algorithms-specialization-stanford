from recursive_dfs import dfs


def test_recursive_dfs():
    graph = {0: [1, 4], 1: [0, 4, 2, 3], 2: [1, 3], 3: [1, 4, 2], 4: [3, 0, 1]}
    graph_tracker = {
        node: {"nodes": graph[node], "is_explored": False} for node in graph
    }
    raw_actual = dfs(graph_tracker)
    is_explored_list = [v["is_explored"] for _, v in raw_actual.items()]
    assert all(is_explored_list)
