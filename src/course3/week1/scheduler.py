from typing import List, Tuple

Weight = int
Length = int

Tasks = List[Tuple[Weight, Length]]

Ordering = List[int]


def score_task(weight: Weight, length: Length):
    return weight / length


def get_weighted_sum_completion_time(ordered_tasks: Tasks):
    score = 0
    cum_length = 0
    for weight, length in ordered_tasks:
        cum_length += length
        score += cum_length * weight
    return score


def scheduler(tasks: Tasks) -> Tuple[Ordering, int]:
    idx_and_task = list(enumerate(tasks))
    ordered_idx_and_task = sorted(
        idx_and_task, key=lambda x: score_task(*x[1]), reverse=True
    )
    ordered_idx, ordered_tasks = list(zip(*ordered_idx_and_task))
    weighted_sum_completion_time = get_weighted_sum_completion_time(list(ordered_tasks))
    return list(ordered_idx), weighted_sum_completion_time
