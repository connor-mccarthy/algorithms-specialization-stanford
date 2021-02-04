import os
from typing import List

from inversion_counter import inversion_counter


def get_data() -> List[int]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "inversions_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [int(number.strip()) for number in lines]


if __name__ == "__main__":
    integers = get_data()
    _, inversions = inversion_counter(integers)
    print("Number of inversions:", inversions)
