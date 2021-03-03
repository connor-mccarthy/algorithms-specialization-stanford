from median_maintenance_assignment import MedianMaintainer, get_data


def test_median_maintainer():
    data = get_data()

    mm = MedianMaintainer()

    total = 0
    for element in data:
        mm.insert(element)
        total += mm.median

    assert mm.median == 5000
    assert total % 10_000 == 1213
