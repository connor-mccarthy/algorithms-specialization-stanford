# Application of DFS: Topological sort
__Definition:__ A topological ordering of a directed graph G is a labelling f of G's nodes such that:
1. The f(v)'s are the set {1, 2, ..., n}
2. (u, v) ∈ G, where f(u) < f(v)

__Motivation:__ Sequence tasks while respecting all precendence constraints

__Note:__ If G has directed cycle -> no topological ordering

__Theorem:__ If G has no directed cycle, can compute topological ordering in O(n+m) time

## Straightforward solution
__Note:__ Every directed acyclic graph has a sink vertex
__Reason:__ If not, can keep following outgoing arcs to produce a directed cycle
__To compute topological ordering:__
* Let v be a sink vertex of G
* Set f(v) = n
* Recurse on G from v
__Why does it work?:__ When v is assigned to position i, all outgoing arcs already deleted --> all lead to later vertices in the ordering

## Topological ordering via DFS
__DFS (graph G, start vertex S)__
* Mark s explored
* For every edge (s, v):
    * If v not yet explored, DFS(G, v)

__DFS Loop for topologicl ordering(graph G)__
* Mark all nodes unexplored
* current_label = n [to keep track of ordering]
* For each vertex v ∈ G:
    * If v not yet explored in a previous DFS call:
        * DFS(G, v)
* Set F(s) = current_label
* Decrement: `current_label--`

__Running time:__ O(m + n)
__Reason:__ O(1) per node, O(1) per edge
__Correctness:__ Need to show that if (u, v) is an edge, then f(u) < f(v)
* __Case 1:__ u visited by DFS before v --> recursive call corresponding to v finishes before that of u (since DFS)
* __Case 2:__ v visited by DFS before u --> v's recursive call finishes before u's even starts --> f(v) = f(u)