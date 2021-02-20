import random
from copy import deepcopy
from typing import Dict, List

GraphAdjacencyLists = Dict[int, List[int]]


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
