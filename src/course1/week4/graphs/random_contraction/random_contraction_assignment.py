import os

from random_contraction import GraphAdjacencyLists, get_min_cut


def get_data() -> GraphAdjacencyLists:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "random_contraction_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    nested_lists = [line.strip().split("\t") for line in lines]
    nested_lists = [[int(num) for num in row] for row in nested_lists]
    return {row[0]: row[1:] for row in nested_lists}


if __name__ == "__main__":  # pragma: no cover
    graph = get_data()
    print(get_min_cut(graph, 100))
