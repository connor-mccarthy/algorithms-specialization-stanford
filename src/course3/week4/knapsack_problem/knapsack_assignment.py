import os
from typing import List


def get_data(filename) -> List[List[int]]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    lines = [tuple(line.strip().split()) for line in lines][1:]  # type: ignore
    return [[int(item) for item in line] for line in lines]
