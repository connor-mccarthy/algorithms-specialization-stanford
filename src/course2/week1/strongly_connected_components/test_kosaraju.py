from kosaraju import Kosaraju


def test_kosaraju():
    adj_list = [
        [0, 6],
        [1, 4],
        [2, 8],
        [3, 0],
        [4, 7],
        [5, 2, 7],
        [6, 3, 8],
        [7, 1],
        [8, 5],
    ]
    kosaraju = Kosaraju(adj_list)
    actual = kosaraju.run()
    expected = [[1, 4, 7], [2, 5, 8], [0, 3, 6]]
    for actual_component in actual.values():
        component_found = False
        for expected_component in expected:
            if set(expected_component) == set(actual_component):
                component_found = True
        assert component_found
    # for scc_id, nodes in actual.items():
    #     for node in nodes:
    #         assert node in expected[scc_id]
