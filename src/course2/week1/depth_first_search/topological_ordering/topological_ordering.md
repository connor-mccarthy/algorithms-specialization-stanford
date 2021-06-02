# Application of DFS: Topological sort

**Definition:** A topological ordering of a directed graph G is a labelling f of G's nodes such that:

1. The f(v)'s are the set {1, 2, ..., n}
2. (u, v) ∈ G, where f(u) < f(v)

**Motivation:** Sequence tasks while respecting all precendence constraints

**Note:** If G has directed cycle -> no topological ordering

**Theorem:** If G has no directed cycle, can compute topological ordering in O(n+m) time

## Straightforward solution

**Note:** Every directed acyclic graph has a sink vertex
**Reason:** If not, can keep following outgoing arcs to produce a directed cycle
**To compute topological ordering:**

- Let v be a sink vertex of G
- Set f(v) = n
- Recurse on G from v
  **Why does it work?:** When v is assigned to position i, all outgoing arcs already deleted --> all lead to later vertices in the ordering

## Topological ordering via DFS

**DFS (graph G, start vertex S)**

- Mark s explored
- For every edge (s, v):
  - If v not yet explored, DFS(G, v)

**DFS Loop for topologicl ordering(graph G)**

- Mark all nodes unexplored
- current_label = n [to keep track of ordering]
- For each vertex v ∈ G:
  - If v not yet explored in a previous DFS call:
    - DFS(G, v)
- Set F(s) = current_label
- Decrement: `current_label--`

**Running time:** O(m + n)
**Reason:** O(1) per node, O(1) per edge
**Correctness:** Need to show that if (u, v) is an edge, then f(u) < f(v)

- **Case 1:** u visited by DFS before v --> recursive call corresponding to v finishes before that of u (since DFS)
- **Case 2:** v visited by DFS before u --> v's recursive call finishes before u's even starts --> f(v) = f(u)
