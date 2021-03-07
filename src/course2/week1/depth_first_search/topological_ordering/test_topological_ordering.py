from topological_ordering import TopologicalSort


def test_topological_sort():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    ts = TopologicalSort(graph)
    actual = ts.sort()
    expected_check_dict = {0: [1], 1: [2, 3], 2: [2, 3], 3: [4]}
    for node, sort_id in actual.items():
        assert sort_id in expected_check_dict[node]
