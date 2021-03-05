import os
from typing import List


def two_sum():
    pass


def get_data() -> List[int]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "two_sum_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    string_lines = [line.strip().split() for line in lines]
    return [int(i) for line in string_lines for i in line]


if __name__ == "__main__":
    get_data()
