import heapq
from typing import List, Tuple

from prims_data_structures import Edge, Graph

PrimsHeap = List[Tuple[int, Edge]]


def create_heap(graph: Graph, start_vertex: int) -> PrimsHeap:
    heap = [(edge.weight, edge) for edge in graph if edge.start == start_vertex]
    heapq.heapify(heap)
    return heap


def prims(graph: Graph) -> Graph:
    start_vertex = graph[0].start  # arbitrary start vertex
    visited_vertices = {start_vertex}
    mst = Graph()
    heap = create_heap(graph, start_vertex)
    while heap:
        weight, edge = heapq.heappop(heap)
        if edge.end not in visited_vertices:
            visited_vertices.add(edge.end)
            mst += edge
            for next_edge in graph:
                if (
                    next_edge.start == edge.end
                    and next_edge.end not in visited_vertices
                ):
                    heapq.heappush(heap, (next_edge.weight, next_edge))
    return mst
