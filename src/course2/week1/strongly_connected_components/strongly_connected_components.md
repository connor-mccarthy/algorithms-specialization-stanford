# Strongly Connected Components
A graph is strongly connected if you can get from any one point to any other point, and vice versa

The strongly connected components are the maximal regions of the graph which are strongly connected

## Kosaraju's two-pass algorithm
__Theorem:__ Can compute SCCs in O(m + n) time
__Algorithm:__ given directed graph G:
1. Let Grev = G with all arcs reversed
2. Run DFS-loop on Grev
    * Goal: Compute "magical ordering" of nodes
    * Let f(v) = "finishing time" of vertex v --> will keep track of each vertex on first pass
3. Run DFS on G
    * Goal: Discover the SCCs one-by-one
    * Will process nodes in decreasing order of finishing times
    * SCCs are nodes with the same "leader"

## DFS-loop
__DFS-Loop(Graph G)__
* Global variable t = 0 -> t tracks how many nodes processed so far -> for finishing time in first pass
* Global variable s = NULL -> current source vertex -> for leaders in 2nd pass
* Assume nodes labelled 1 to n
* For i=n down to 1:
    * If i not yet explored:
        * s := i
        * DFS(G, s)

__DFS(Graph G, node i)__
* Mark i as explored
* Set leader(i) := node s
* For each arc(i, j) in G:
    * If j not yet explored:
        * DFS(G, j)
* t++
* Set f(i) := t, where f(i) is i's finishing time

## Running time
2 * DFS = O(m + n)