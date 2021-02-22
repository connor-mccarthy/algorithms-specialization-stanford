# Breadth-first Search and Shortest Path

## BFS Basics
* Explore nodes in "layers"
* Can compute shortest path
* Connected components of undirected graph

## Run Time
O(m + n) --> linear time, since m and n jointly constitute the size of the graph

## Pseudocode
Graph G, start vertex s

All nodes are initially unexplored

* Mark s as explored
* Let Q = queue data structure (FIFO), initialized with s
* Whlie Q != 0:
    * Remove the first node of Q, call it v
    * For each edge (v, w):
        * If w unexplored
            * Mark w as explored
            * Add w to Q (at the end)


## Basic BFS properties
__Claim #1:__ At the end of BFS, v explored --> i.e. G has a path from s to v
* Reason: special case of the generic algorithm

__Claim #2:__ Running time of main while loop = O(n_s + m_s), where n_s = # of nodes that can be reached from s and m_s = # of nodes that can be reached from s

## Applications
### Shortest path
Goal: Compute dist(v), the fewest number of edges on a path from s to v

Extra code (on top of psuedocode above):
    * Initialize dist(v) {0 if v = s, +inf if v != s}
    * When considering edge (v, w):
        * If w unexplored, then set dist(w) = dist(v) + 1

Claim: At termination, dist(v) = i, where v is in the ith layer -> shortest s-v path has i edges

Proof idea: Every layer-i node w is added to Q by a layer-(i-1) node v via the edge (v, w)

### Undirected connectivity
Let G = (V, E) be an undirected graph

Goal: Compute all connected components

Connected components: the "pieces" of G --> the connected components in a graph that may not be fully connected
Formal definition: equivalence classes of the relation u~v --> i.e., not u-v in path G
Note: ~ is an equivalence relation

Why? Check if network is disconnected

Answers the questions: Can you get to Kevin Bacon from every other actor/actress? Are there houses I cannot call from my house?

Also provides a quick and dirty heuristic for clustering.

__To compute all components__ (undirected case):
* All nodes (labelled one to n) unexplored
* For i=1 to n:
    * If i not yet explored
        * Invoke BFS on the graph with start node i

Note: finds every connected component

Running time: O(n + m)
