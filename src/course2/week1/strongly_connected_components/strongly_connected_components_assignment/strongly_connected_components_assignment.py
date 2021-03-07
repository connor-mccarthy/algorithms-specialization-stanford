import os
import resource
import sys
from typing import Dict, List

from kosaraju import Kosaraju

# tncrease recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK, (hardlimit, hardlimit))


def get_data() -> List[List[int]]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "strongly_connected_components_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    string_lines = [line.strip().split(" ") for line in lines]
    return [[int(num) - 1 for num in line] for line in string_lines]


def get_largest_component_sizes(sccs: Dict[int, List[int]], components: int) -> str:
    sorted_sccs = sorted(sccs.items(), key=lambda x: len(x[1]), reverse=True)
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


def main() -> str:
    lines = get_data()
    kosaraju = Kosaraju(lines)
    sccs = kosaraju.run()
    components = 5
    return get_largest_component_sizes(sccs, components)


if __name__ == "__main__":  # pragma: no cover
    print(main())
