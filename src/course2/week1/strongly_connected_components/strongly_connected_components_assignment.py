import itertools
import os
from typing import List

from kosaraju import Graph, Kosaraju


def get_data() -> List[List[int]]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "strongly_connected_components_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    string_lines = [line.strip().split(" ") for line in lines]
    return [[int(num) for num in line] for line in string_lines]


def convert_lines_to_adjacency_list(lines: List[List[int]]) -> Graph:
    adjacency_list: Graph = {}
    for k, g in itertools.groupby(lines, key=lambda x: x[0]):
        edges = list(g)
        adjacent_nodes = [edge[1] for edge in edges]
        adjacency_list[k] = adjacent_nodes

    # we need to fill in the missing indices
    for i in range(list(adjacency_list.keys())[-1]):
        if i not in adjacency_list:
            adjacency_list[i] = []

    return adjacency_list


def main() -> None:
    import sys

    sys.setrecursionlimit(100000)
    lines = get_data()
    graph = convert_lines_to_adjacency_list(lines)
    kosaraju = Kosaraju(graph)
    sccs = kosaraju.run()
    sorted_sccs = sorted(sccs.items(), key=lambda x: len(x[1]))
    no_scss_required = 5
    for i in range(no_scss_required):
        print(sorted_sccs[i][1])


if __name__ == "__main__":  # pragma: no cover
    main()
