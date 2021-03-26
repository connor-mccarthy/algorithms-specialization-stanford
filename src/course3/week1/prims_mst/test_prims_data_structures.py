from prims_data_structures import Edge, Graph


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


def test_graph_indexing():
    graph = Graph(Edge(1, 2, 1), Edge(1, 3, 4))
    assert graph[0] == Edge(1, 2, 1)
    assert graph[-1] == Edge(1, 3, 4)


def test_graph_deletion():
    graph = Graph(Edge(1, 2, 1), Edge(1, 3, 4))
    del graph[0]
    assert graph.size == 1


def test_graph_setting():
    graph = Graph(Edge(1, 2, 1), Edge(1, 3, 4))
    new_edge = Edge(1, 3, 5)
    graph[1] = new_edge
    assert graph[1] == new_edge
