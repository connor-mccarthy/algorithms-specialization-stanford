from mwis import mwis


def test_mwis():
    input_nodes = [1, 4, 5, 4]
    expected_indices = {1, 3}
    actual = mwis(input_nodes)
    assert actual == expected_indices
