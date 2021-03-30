from graph_data_structures import Edge, Graph
from kruskal import kruskal


def test_kruskal():
    input_graph = Graph(
        Edge(1, 2, 1), Edge(1, 3, 4), Edge(1, 4, 3), Edge(2, 4, 2), Edge(3, 4, 5)
    )
    expected_graph = Graph(Edge(1, 2, 1), Edge(1, 3, 4), Edge(2, 4, 2))
    actual_graph = kruskal(input_graph)
    print(actual_graph)
    print(expected_graph)
    assert actual_graph == expected_graph
