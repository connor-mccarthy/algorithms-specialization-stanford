import os
from typing import List, Tuple

from knapsack import Item, construct_array


def get_data(filename) -> Tuple[List[Item], int]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    lines = [tuple(line.strip().split()) for line in lines]  # type: ignore
    capacity = int(lines[0][0])
    items = [Item(*(int(item) for item in line)) for line in lines[1:]]
    return items, capacity


def main() -> None:
    filenames = [
        "knapsack_assignment_data_small.txt",
        "knapsack_assignment_data_big.txt",
    ]
    for filename in filenames:
        items, capacity = get_data(filename)
        knapsack_array = construct_array(items, capacity)
        max_value = knapsack_array[len(items)][capacity]
        print(max_value)


if __name__ == "__main__":
    main()
