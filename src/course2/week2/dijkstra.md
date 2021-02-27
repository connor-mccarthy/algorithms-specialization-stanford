# Dijkstra's Shortest Path Algorithm
__Input:__ Directed graph F=(V, E).  (m = |E|, n = |V|)
* Each edge has a non-negative length (could be length of "road" or expected travel time)
__Output:__ for each v ∈ V, compute L(v) := lenght of a shortest s-v path in G (sum of path edge lengths)
__Assumptions:__
* For convenience: for all v in V, there exists a path from s to v (small assumption, cause we could use DFS to check this easily as a preprocessing step)
* Important: l_e (edge length) >= 0 for all e in E.

## Why another shortest-path algorithm?
__Question:__ Doesn't BFS already compute shortest paths in linear time?
__Answer:__ Yes, IF l_e (edge length) = 1 for every edge e

__Question:__ Why no just replace each edge e by directed path of le unit edge length edges, then use BFS. e.g. Does one edge with length 3 == three edges with length 1?
__Answer:__ Yes! But this blows up the graph too much if the edge lengths are too large --> so works in linear time, but on a MUCH larger graph potentially
__Solution:__ Dijkstra's

## Dijkstra's psuedocode
Close cousin of BFS, but with edge lengths >= 1

__Initialize:__
* X = [s] -> array of vertices processed so far
* A[s] = 0 -> computed shortest path distances
* B[s] = empty path -> computed shortest path (the actual path, not the distance) (would not include in actual implementation, this is to help with the explanation)

Goal: grow array X to cover the whole graph, with all nodes V

__Main loop:__
* While X != V (doesn't contain all nodes):
    (Note: interested in vertices that start in the nodes we've seen and end in the ones we haven't)
    * Among all edges (v, w) ∈ E with v ∈ X, w ∉ X, pick the one that minimizes: A[v] + l_(vw) (Dijkstra's greedy criterion)
    * Add node belonging to this edge (w*) to X
    * Set A[w*] = A[v*] + l_(v\*w*)
    * Set B[w*] = B[v*] U (v*, w*) (append edge)

## Non-example
__Question:__ Why not reduce computing shortest paths with negative edge lengths to the same problem with non-negative edge lengths by adding a large constant to all edge lengths?
__Problem:__ Doesn't preserve shortest path because there are a different number of edges between nodes. Two nodes with 5 edges between would go up by 50 if we add 10 to each edge, but two nodes with 3 edges between would only go up by 30 if we add 10 to each edge.

## Using a heap datastructure
A heap helps speed up this algorithm a lot

The hint that we might need a better datastructure is that we are computing minimums over and over again

The heap is good at computing minimums over an dover again

Reason for using a heat: perform insert, extract-min in O(logn) time

__Heaps:__
* Conceptually, a perfectly balanced binary tree --> height ~= log_2(n)
* Heap property: at ever node, key <= childrens keys
* Can extract-min by swapping up last leaf and bubbling down
* Insert via bubbling up
* Also: will need the ability to delete from middle of heap (and bubble up or down as needed)

### Two invariants
__Invariant #1:__ Elements in heap = vertices of V-X (unseen vertices)
__Invariant #2:__ For v ∉ X (every unseen vertex), key[v] = smallest Dijkstra greedy score of an edge (?, v) ∈ E with v ∈ X (or +inf if no edge exists)

__Point:__ By invariants, extract-min yields correct vertex w* to add to X next (and we set A[w*] to key[w*])

__To maintain invariant #2:__ When w is extracted from the head (i.e. added to X):
    * If v ∈ V-x (i.e., in heap)
        * Delete v from heap
        * Recompute key[v] = min[A[w] + l_wv]

### Running time analysis
__You check:__ Dominated by heap operations (O(logn) each)
* (n-1) extract mins
* each edge (v, w) triggers at most one delete/insert combo (if v added to X first)

__So:__ # of heap operations is O(n + m) = O(m), since graph is weakly connected (m is always at least as big as n)
--> Running time is O(mlogn) (like sorting)
