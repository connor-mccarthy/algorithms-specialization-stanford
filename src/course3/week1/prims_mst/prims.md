# Prim's Minimum Spanning Tree Algorithm

__Informal goal:__ Connect a bunch of points together as cheaply as possible

__Applications:__ clustering, networking

__Blazingly fast greedy algorithms:__
* Prim's MST algorithm
* Kruskal's Algorithm
* O(mlogn) time --> using suitable data structures (m=num edges, n=num nodes)

## Formal problem definition
__Input:__ undirected graph G=(V, E) and a cost c_e for each edge e ∈ E
* Assume adjacency list representation
* Ok if ledge costs are negative

__Output:__ minimum cost (sum of edge costs) tree T <= E that spans all vertices, i.e.:
1) T has no cycles
2) The subgraph (V, T) is connected (i.e., contains path between each pair of vertices)

A couple of assumptions to make things easier:
* Assumption 1: input graph G is itself connected
    * If this weren't true, there is no minimum spanning tree
    * Easy to check in preprocessing (e.g. depth-first search)
    * The more general problem with the possibility of a disconnected graph is called "minimum spanning forest"
* Assumption 2: edge costs are distinct
    * Prim + Krustkal remain correct with ties (which can be broken arbitrarily)
    * Correctness proof a bit more annoying

## The algorithm
