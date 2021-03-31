from clustering import clustering
from graph_data_structures import Edge, Graph


def test_clustering():
    input_graph = Graph(
        Edge(1, 2, 1), Edge(1, 3, 4), Edge(1, 4, 3), Edge(2, 4, 2), Edge(3, 4, 5)
    )
    expected_max_cost = 4
    actual_max_cost = clustering(input_graph, 2)
    assert actual_max_cost == expected_max_cost
