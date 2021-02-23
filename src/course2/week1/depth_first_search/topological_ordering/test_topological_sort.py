from topological_sort import TopologicalSort


def test_topological_sort():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    ts = TopologicalSort(graph)
    ts.sort()
    raw_actual = ts.graph_tracker
    {k: v["topo_id"] for k, v in raw_actual.items()}
    expected_check_dict = {0: [1], 1: [2, 3], 2: [2, 3], 3: [4]}
    for node, node_info in raw_actual.items():
        assert node_info["topo_id"] in expected_check_dict[node]
