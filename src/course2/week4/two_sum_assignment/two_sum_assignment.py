import os
from typing import Dict, List

Array = List[int]


def get_data() -> Array:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "two_sum_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    string_lines = [line.strip().split() for line in lines]
    return [int(i) for line in string_lines for i in line]


def create_hash_table_from_array(array: Array) -> Dict[int, bool]:
    hash_table: Dict[int, bool] = {}
    for e in array:
        hash_table[e] = True
    return hash_table


def hash_table_2_sum(array: Array, target_start: int, target_end: int):
    # deduping the array makes the search space smaller
    array = list(set(array))
    hash_table = create_hash_table_from_array(array)
    targets = set()
    for t in range(target_start, target_end + 1):
        for e in array:
            if (e != t - e) and (
                hash_table.get(t - e, False)
            ):  # put e != t-e first so that and evaluation fails fast
                targets.add(t)
    return len(targets)


def main() -> int:
    data = get_data()
    return hash_table_2_sum(array=data, target_start=-10000, target_end=10000)


if __name__ == "__main__":
    print(main())
