from dijkstra import dijkstra


def test_dijkstra():
    graph = [
        (1, 1, 2),
        (2, 1, 8),
        (1, 2, 1),
        (1, 2, 3),
        (1, 3, 2),
        (1, 3, 4),
        (1, 4, 3),
        (1, 4, 5),
        (1, 5, 4),
        (1, 5, 6),
        (1, 6, 5),
        (1, 6, 7),
        (1, 7, 6),
        (1, 7, 8),
        (1, 8, 7),
        (2, 8, 1),
    ]
    actual = dijkstra(graph, 1)
    expected = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3, 8: 2}
    assert actual == expected
