from disjoint_set import DisjointSet

from graph_data_structures import Graph


def sort_graph(graph: Graph) -> Graph:
    return Graph(*sorted(graph, key=lambda edge: edge.weight))


def kruskal(graph: Graph) -> Graph:
    graph = sort_graph(graph)
    ds: DisjointSet = DisjointSet()
    mst = Graph()
    for vertex in graph.vertices:
        ds.find(vertex)
    for edge in graph:
        if not ds.connected(edge.start, edge.end):
            mst += edge
            component_1 = ds.find(edge.start)
            component_2 = ds.find(edge.end)
            ds.union(component_1, component_2)
    return mst
