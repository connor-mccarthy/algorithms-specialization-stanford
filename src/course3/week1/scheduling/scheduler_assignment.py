import os
from typing import Dict, List, Tuple

from scheduler import get_weighted_sum_completion_time
from scheduler import scheduler as optimal_scheduler

Weight = int
Length = int

Tasks = List[Tuple[Weight, Length]]

Ordering = List[int]


def get_data() -> Tasks:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "jobs.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    lines = [tuple(line.strip().split()) for line in lines][1:]  # type: ignore
    return [(int(weight), int(length)) for weight, length in lines]  # type: ignore


def score_task(weight: Weight, length: Length) -> int:
    return weight - length


def suboptimal_scheduler(tasks: Tasks) -> Tuple[Ordering, int]:
    idx_and_task = list(enumerate(tasks))
    idx_and_task.sort(key=lambda x: (score_task(*x[1]), x[1][0]), reverse=True)
    ordered_idx, ordered_tasks = list(zip(*idx_and_task))
    weighted_sum_completion_time = get_weighted_sum_completion_time(list(ordered_tasks))
    return list(ordered_idx), weighted_sum_completion_time


def main() -> Dict[str, int]:
    tasks = get_data()
    _, suboptimal_score = suboptimal_scheduler(tasks)
    _, optimal_score = optimal_scheduler(tasks)
    return {"suboptimal score": suboptimal_score, "optimal score": optimal_score}


if __name__ == "__main__":
    print(main())
