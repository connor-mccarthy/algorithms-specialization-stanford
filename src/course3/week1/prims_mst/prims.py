import heapq
from typing import List

from prims_data_structures import Edge, Graph

PrimsHeap = List[Edge]


def create_heap(graph: Graph, start_vertex: int) -> PrimsHeap:
    heap = [edge for edge in graph if edge.start == start_vertex]
    heapq.heapify(heap)
    return heap


def prims(graph: Graph) -> Graph:
    graph = Graph(*graph.edges + graph.reverse().edges)
    start_vertex = graph[0].start  # arbitrary start vertex
    visited_vertices = {start_vertex}
    mst = Graph()
    heap = create_heap(graph, start_vertex)

    while visited_vertices != graph.vertices:
        winner = heapq.heappop(heap)
        visited_vertices.add(winner.end)
        mst += winner

        for i, unvisited_edge in enumerate(heap):
            if unvisited_edge.end == winner.end:
                heap[i].weight = float("inf")

        heapq.heapify(heap)

        for other_edge in graph:
            if (
                other_edge.start == winner.end
                and other_edge.end not in visited_vertices
            ):
                heapq.heappush(heap, other_edge)

    return mst
