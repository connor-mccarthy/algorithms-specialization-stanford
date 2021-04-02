from knapsack import Item, knapsack


def test_knapsack():
    input_data = [Item(3, 4), Item(2, 3), Item(4, 2), Item(4, 3)]
    capacity = 6
    actual = knapsack(input_data, capacity)
    expected = {2, 3}
    assert actual == expected
