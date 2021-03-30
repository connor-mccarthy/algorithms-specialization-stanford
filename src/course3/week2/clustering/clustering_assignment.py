import os

from graph_data_structures import Edge, Graph

# from clustering import clustering


def get_data() -> Graph:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "edges.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    lines = [tuple(line.strip().split()) for line in lines][1:]  # type: ignore
    data = [tuple(int(item) for item in line) for line in lines]
    return Graph(*[Edge(*edge_data) for edge_data in data])
