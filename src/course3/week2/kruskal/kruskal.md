# Kruskal's minimum spanning tree algorithm

Unlike in Prim's, Kruskal's algorithm is okay with not incrementally building a connected tree

In Kruskals, we look for the cheapest edge we haven't looked at yet while preventing cycles

## The algorithm
* Sort edges in order of increasing cost (1, 2, 3, ..., m so that c1< c2 < ... < cm)
* T  = {}
* For i = 1 to m:
    * If adding i to T doesn't create a cycle:
        * Add i to T
return T

## The union-find data structure
* It allows us to check for cycles in constant time
* This data structure maintains a partition of a set of objects

It supports operations:
* Find(x) -> return name of graph that x belongs to
* Union(C_i, C_j) -> fuse groups C_i and C_j into a single group

Why useful for Kruskal's algorithm? Every time it adds a new edge, it fuses conneced components

## Union-find basics
__Idea #1:__
* Maintain one linked structure per connected component of (V, T)
* Each component has an arbitrary leader vertex

__Invariant:__ Each vertex points to the leader of its copmonent ["name" of a compnent inherited from leader vertex]

__Motivation:__ O(1)-time cycle checks

__Key point:__ given edge (u, v), can check if u & v already in same component in O(1) time [if find(u) == find(v); i.e. u and v have same leader components]

## Maintaining the invariant
__Note:__ When new edge (u, v) added to T, connected components of u and v merge

__Idea #2:__ When two components merge, have the smaller one inherit the leader of the larger one --> you can check size in constant time by maintaining a size field in each component

How many times does a single vertex have its leader pointer updated over the course of the Kruskal algorithm? O(logn)

Why? Every time v's leader pointer gets updated, population of its component at least doubles --> can only happen <= log_2(n) times!

# Running time of fast implementation
__Scorecard:__
O(m logn) time for sorting
O(m) time for cycle checks [O(1) per iteration]
O(m logn) time overall for leader pointer updates

Total: O(m logn)