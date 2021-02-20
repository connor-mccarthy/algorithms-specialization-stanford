from copy import deepcopy

from random_contraction import get_min_cut
from random_contraction_assignment import get_data


def test_randomized_contract():
    """NOTE: This is not a deterministic test, though it is highly unlikely to fail."""
    failed = True
    repeats = 0
    max_repeats = 5

    expected = 17

    while failed and (repeats < max_repeats):
        graph = get_data()
        copied_graph = deepcopy(graph)
        min_cuts = get_min_cut(copied_graph, 100)
        failed = min_cuts == expected
        repeats += 1

    assert min_cuts == expected
