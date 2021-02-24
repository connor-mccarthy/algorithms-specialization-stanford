from kosaraju import Kosaraju


def test_kosaru():
    graph = {
        0: [6],
        1: [4],
        2: [8],
        3: [0],
        4: [7],
        5: [2, 7],
        6: [3, 8],
        7: [1],
        8: [5],
    }
    kosaraju = Kosaraju(graph)
    actual = kosaraju.run()
    expected = {1: [1, 4, 7], 2: [2, 5, 8], 3: [0, 3, 6]}
    assert actual == expected
