from disjoint_set import DisjointSet

from graph_data_structures2 import Graph


class DisjointSetWithSize(DisjointSet):
    def __len__(self):
        return len(list(self.itersets()))


def sort_graph(graph: Graph) -> Graph:
    return Graph(*sorted(graph, key=lambda edge: edge.weight))


def clustering(graph: Graph, k: int) -> int:
    graph = sort_graph(graph)
    ds: DisjointSetWithSize = DisjointSetWithSize()
    for vertex in graph.vertices:
        ds.find(vertex)

    for edge in graph:
        if not ds.connected(edge.start, edge.end):
            if len(ds) == k:
                return edge.weight

            component_1 = ds.find(edge.start)
            component_2 = ds.find(edge.end)
            ds.union(component_1, component_2)

    raise Exception("Clustering did not terminate.")
