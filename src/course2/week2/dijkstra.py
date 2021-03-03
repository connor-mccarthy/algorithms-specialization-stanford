from collections import namedtuple
from typing import Dict, List, Tuple

Weight = int
StartNode = int
EndNode = int
EdgeType = Tuple[Weight, StartNode, EndNode]
WeightedGraph = List[EdgeType]

Edge: EdgeType = namedtuple("Edge", ["weight", "start", "end"])


def dijkstra(graph: WeightedGraph, start_node: int):
    graph = [Edge(*edge_data) for edge_data in graph]
    visited = {start_node}
    distances = {start_node: 0}
    vertices = {edge.start for edge in graph}
    while vertices != visited:
        possible_edges = [
            edge
            for edge in graph
            if (edge.start in visited) and (edge.end not in visited)
        ]
        dijkstra_scores = [
            (edge, dijkstras_greedy_criterion(edge, distances))
            for edge in possible_edges
        ]
        w_star, total_distance = min(dijkstra_scores, key=lambda tup: tup[1])
        visited.add(w_star.end)
        distances[w_star.end] = total_distance
    return distances


def dijkstras_greedy_criterion(edge: Edge, distances: Dict[int, int]):
    return distances[edge.start] + edge.weight


if __name__ == "__main__":
    graph = [
        (1, 1, 2),
        (2, 1, 8),
        (1, 2, 1),
        (1, 2, 3),
        (1, 3, 2),
        (1, 3, 4),
        (1, 4, 3),
        (1, 4, 5),
        (1, 5, 4),
        (1, 5, 6),
        (1, 6, 5),
        (1, 6, 7),
        (1, 7, 6),
        (1, 7, 8),
        (1, 8, 7),
        (2, 8, 1),
    ]
    print(dijkstra(graph, 1))
