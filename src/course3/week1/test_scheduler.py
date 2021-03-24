import pytest

from scheduler import scheduler

test_case_1 = ([(3, 5), (1, 2)], [0, 1], 22)
test_case_2 = ([(8, 3), (20, 3), (9, 2)], [1, 2, 0], 169)


@pytest.mark.parametrize(
    "tasks, expected_order, expected_score", [test_case_1, test_case_2]
)
def test_scheduler(tasks, expected_order, expected_score):
    actual_order, actual_score = scheduler(tasks)
    assert actual_order == expected_order
    assert actual_score == expected_score
