# Week 1: Graph Search and Connectivity

## Motivation for graph search
1. Check if a network is connected (phone line, degrees of Kevin Bacon)
2. Driving directions
3. Formulate a plan (get from one state to another state)
    * e.g. how to fill in a sudoku puzzle
        * nodes = a partially completed puzzle
        * arcs = filling in one new square

4. Compute the "pieces" (or "components") of a graph
    * clustering, structure of the web graph, etc.

## Generic graph search
Goals:
1. Find everything findable from a given start vertex
2. Don't compare anything twice (Goal: O(m + n))

Generic algorithm (given graph G, vertex s starting point) (high level)
* Initially s exploreed, all other vertices unexplored
* While possible:
    * Choose an edge (u, v) with u explored and v unexplored (if none, halt)
    * Mark v explored

Claim: At end of the algorithm, v explored --> G has a path from s to v

## Breadth first v depth first search
How to choose among the many possible frontier edges

* Breadth first search (BFS)
    * Explore nodes in "layers"
    * Can compute shortest paths
    * Can compute connected components of an undirected graph
    * O(m + n) time using a queue (FIFO)

* Depth first search (DFS)
    * Explore aggressively (like a maze) back tracking only when necessary
    * Compute topological ordering of a directed acycling graph
    * Compute connected components in directed graphs
    * O(m + n) time using a stack (LIFO) (or via recursion)
