from collections import namedtuple
from typing import Dict, List, Tuple

StartNode = int
EndNode = int
Weight = int
EdgeType = Tuple[StartNode, EndNode, Weight]
WeightedGraph = List[EdgeType]

Edge: EdgeType = namedtuple("Edge", ["start", "end", "weight"])


def dijkstra(graph: WeightedGraph, start_node: int) -> Dict[int, int]:
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


def dijkstras_greedy_criterion(edge: Edge, distances: Dict[int, int]) -> int:
    return distances[edge.start] + edge.weight
