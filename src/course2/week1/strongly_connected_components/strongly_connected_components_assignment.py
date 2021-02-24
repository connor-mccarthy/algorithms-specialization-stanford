import os
import sys
import threading
from typing import Dict, List

from kosaraju import Kosaraju


def get_data() -> List[List[int]]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "strongly_connected_components_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    string_lines = [line.strip().split(" ") for line in lines]
    return [[int(num) - 1 for num in line] for line in string_lines]


def get_largest_component_sizes(sccs: Dict[int, List[int]], components: int) -> str:
    sorted_sccs = sorted(sccs.items(), key=lambda x: len(x[1]))
    components = 5
    output = ""
    for i in range(components):
        try:
            output += str(len(sorted_sccs[i][1]))
        except IndexError:
            output += str(0)
        if i != components - 1:
            output += ","
    return output


def get_small_data():
    lines = [
        [1, 4],
        [2, 8],
        [3, 6],
        [4, 7],
        [5, 2],
        [6, 9],
        [7, 1],
        [8, 5],
        [8, 6],
        [9, 7],
        [9, 3],
    ]
    return [[node - 1 for node in line] for line in lines]


def main() -> str:
    lines = get_data()
    kosaraju = Kosaraju(lines)
    sccs = kosaraju.run()
    components = 5
    return get_largest_component_sizes(sccs, components)


sys.setrecursionlimit(2097152)  # adjust numbers
threading.stack_size(134217728)  # for your needs

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

if __name__ == "__main__":  # pragma: no cover
    print(main())
