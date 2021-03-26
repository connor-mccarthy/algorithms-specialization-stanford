import heapq
from typing import List, Set, Tuple, Union

from prims_data_structures import Edge, Graph

PrimsHeap = List[Tuple[Union[int, float], int, Edge]]


def create_heap(graph: Graph, start_vertex: int):
    heap: PrimsHeap = []
    for edge in graph:
        if edge.end != start_vertex:
            if edge.start == start_vertex:
                heapq.heappush(heap, (edge.weight, edge.end, edge))
            else:
                heapq.heappush(heap, (float("inf"), edge.end, edge))
    return heap


def get_edges_crossing_frontier(graph: Graph, visited_vertices: Set[int]) -> List[Edge]:
    unvisited_vertices = set(graph.vertices) - visited_vertices
    return [edge for edge in graph if edge.end in unvisited_vertices]


def prims(graph: Graph) -> Graph:
    start_vertex = graph[0].start  # arbitrary start vertex
    visited_vertices = {start_vertex}
    mst = Graph()
    heap = create_heap(graph, start_vertex)
    while heap:
        weight, end_vertex, min_edge = heapq.heappop(heap)
        visited_vertices.add(end_vertex)
        mst += min_edge

        edges_crossing_frontier = get_edges_crossing_frontier(graph, visited_vertices)
        for new_edge in edges_crossing_frontier:
            for index, (weight, end_vertex, old_edge) in enumerate(heap):
                if old_edge.end == new_edge.end and new_edge.weight < old_edge.weight:
                    del heap[index]
                    heapq.heapify(heap)
                    heapq.heappush(heap, (new_edge.weight, new_edge.end, new_edge))
    return mst
