import os
import random
from copy import deepcopy
from typing import Dict, List

GraphAdjacencyLists = Dict[int, List[int]]


def get_data() -> GraphAdjacencyLists:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "randomized_contraction_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    nested_lists = [line.strip().split("\t") for line in lines]
    nested_lists = [[int(num) for num in row] for row in nested_lists]
    return {row[0]: row[1:] for row in nested_lists}


def get_min_cut(graph: GraphAdjacencyLists, num_iters: int) -> int:
    for i in range(num_iters):
        copied_graph = deepcopy(graph)
        min_cut = get_min_cut_single_iter(copied_graph)
        if i == 0:
            output_min_cut = min_cut
        else:
            output_min_cut = min_cut if min_cut < output_min_cut else output_min_cut
    return output_min_cut


def get_min_cut_single_iter(graph: GraphAdjacencyLists) -> int:  # pragma: no cover
    output_min_cut = len(graph)
    while len(graph) > 2:
        v = random.choice(list(graph.keys()))
        w = random.choice(graph[v])
        graph = contract(graph, v, w)
    min_cut = len(list(graph.values())[0])
    output_min_cut = min_cut if min_cut < output_min_cut else output_min_cut
    return output_min_cut


def contract(graph: GraphAdjacencyLists, v: int, w: int) -> GraphAdjacencyLists:
    for node in graph[w]:
        if node != v:
            graph[v].append(node)
            graph[node].append(v)

        graph[node].remove(w)

    del graph[w]
    return graph


if __name__ == "__main__":  # pragma: no cover
    graph = get_data()
    print(get_min_cut(graph, 100))
