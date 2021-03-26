from prims import Edge, Graph, prims


def test_edge_equality():
    assert Edge(1, 2) == Edge(1, 2)
    assert Edge(1, 2) == Edge(2, 1)
    assert Edge(1, 2) != Edge(1, 3)
    assert Edge(1, 2, 3) == Edge(1, 2, 3)
    assert Edge(1, 2, 3) == Edge(2, 1, 3)
    assert Edge(1, 2, 3) != Edge(1, 2, 4)
    assert Edge(1, 2, 3) != Edge(1, 3, 3)


def test_graph_iterable():
    graph = Graph(
        Edge(1, 2, 1), Edge(1, 3, 4), Edge(1, 4, 3), Edge(2, 4, 2), Edge(3, 4, 5)
    )
    for edge in graph:
        assert isinstance(edge, Edge)


def test_graph_equality():
    assert Graph(Edge(1, 2, 1), Edge(1, 3, 4)) == Graph(Edge(1, 3, 4), Edge(1, 2, 1))
    assert Graph(Edge(1, 2, 1), Edge(1, 3, 4)) == Graph(Edge(1, 3, 4), Edge(2, 1, 1))
    assert Graph(Edge(1, 2, 1), Edge(1, 3, 4)) != Graph(
        Edge(1, 3, 4), Edge(1, 2, 1), Edge(1, 2, 1)
    )


def test_prims():
    input_graph = Graph(
        Edge(1, 2, 1), Edge(1, 3, 4), Edge(1, 4, 3), Edge(2, 4, 2), Edge(3, 4, 5)
    )
    expected_graph = Graph(Edge(1, 2, 1), Edge(1, 3, 4), Edge(2, 4, 2))
    actual_graph = prims(input_graph)
    assert actual_graph == expected_graph
