# Prim's Minimum Spanning Tree Algorithm

**Informal goal:** Connect a bunch of points together as cheaply as possible

**Applications:** clustering, networking

**Blazingly fast greedy algorithms:**

- Prim's MST algorithm
- Kruskal's Algorithm
- O(mlogn) time --> using suitable data structures (m=num edges, n=num nodes)

## Formal problem definition

**Input:** undirected graph G=(V, E) and a cost c_e for each edge e ∈ E

- Assume adjacency list representation
- Ok if ledge costs are negative

**Output:** minimum cost (sum of edge costs) tree T <= E that spans all vertices, i.e.:

1. T has no cycles
2. The subgraph (V, T) is connected (i.e., contains path between each pair of vertices)

A couple of assumptions to make things easier:

- Assumption 1: input graph G is itself connected
  - If this weren't true, there is no minimum spanning tree
  - Easy to check in preprocessing (e.g. depth-first search)
  - The more general problem with the possibility of a disconnected graph is called "minimum spanning forest"
- Assumption 2: edge costs are distinct
  - Prim + Krustkal remain correct with ties (which can be broken arbitrarily)
  - Correctness proof a bit more annoying

## The algorithm

- Initialize x = [s] [s is randomly chosen from v]
- T (minimum spanning tree) does not exist yet [invariant: X = vertices spanned by tree-so-far T]
- While X != V:
  - Let e = (u, v) be the cheapest edge of F with u ∈ X, v ∉ X
  - Add e to T
  - Add v to X

i.e., increase # of spanned vertices in cheapest way possible

## Correctness of Prim's algorithm

**Theorem:** Prim's algorithm always computes a MST
**Part 1:** Computes a spanning tree T\*

- will use basic properties of graphs and spanning trees
  **Part 2:** T\* is an MST [will use the "cut property"]
  **Later:** Fast [O(mlogn) implementation using heaps]

### Correctness part 1

#### Cuts

**Claim:** Prim's algorithm outputs a spanning tree
**Definition:** a cut of a graph G=(V, E) is a partition of V into 2 non-empty sets
**Question:** Roughly how many cuts does a graph with n vertices have? --> roughly 2\*\*n (each of the n vertices can go into one group or the other) (actually 2\*\*(n - 1), since there can't be any empty groups for a cut to be a cut)

**Empty cut lemma:** a graph is not connected <--> there is a cut (A, B) with no crossing edges
**Proof:** (assume RHS, prove LHS of proof): pick any v ∈ A and v ∈ B. Since no edges cross (A, B), there is no u-v path in G --> therefore, G is not connected
(assume LHS, prove, RHS of proof): Assume the LHS. Suppose G has no u-v path. Define A={vertices reachable from u in G (i.e., u's connected components)} B={all other vertices (i.e., all other connected components)}
Note: no edges cross the cut (A, B) (otherwise, A would be bigger.)

**Double-crossing lemma:** suppose the cycle C <=E has an edge crossing the cut (A, B) --> then so does some other edge of C

**Lonely cut corollary:** If e is the only edge crossing some cut (A, B), then it is not in any cycle (otherwise the cut would cross more than one edge)

#### Proof of Part 1

**Claim:** Prim's algorithm outputs a spanning tree (not claiming MST yet)
Note: a spanning tree: must span all of the vertices and must have no cycles
**Proof:**

1. Algorithm maintain's invariant that tree T spans vertex set X
2. (A spanning tree must span all vertices, so) Can't get stuck with X != V (if we stopped with X < V, we'd have the cut (X, V-X), which must be empty... so by empty cut lemma, G would have to be disconnected, which we know is not true by definition)
3. No cycles ever get created in T. Why? Consider any iteration with current sets X and T. Suppose e gets added. Recall, prims only searches edges that cross cut (X, V-X), so e is the first edge to cross (X, V-X) that gets added to T --> its addition cannot create a cycle in T by the lonely cut corollary

### Proof of Part 2

**Theorem:** Prim's algorithm always outputs a minimum-cost spanning tree

**Key question:** When is it "safe" to includ an edge in the tree-so-far?

#### The cut property

Consider an edge e of G. Suppose there is a cut (A, B) such that e is the cheapest edge of G that crosses it.

Then, e belongs to the MST of the graph.

**Note:** This does not imply that other edges for a given cut are NOT part of the the MST, as those might be the cheapest of other cuts!

**Claim:** cut property implies Prim's algorithm is correct

**Proof:** Prim's algorithm outputs a spanning tree T\*

**Key point**: every edge e we add to T\* is explicitly justified by the cut property

- T\* is a subset of the MST
- since t\* is already a spanning tree, it must be the MST

## Implementation

### Simple implementation

- Initialize x = [s] [s is randomly chosen from v]
- T (minimum spanning tree) does not exist yet [invariant: X = vertices spanned by tree-so-far T]
- While X != V:
  - Let e = (u, v) be the cheapest edge of F with u ∈ X, v ∉ X
  - Add e to T
  - Add v to X

i.e., increase # of spanned vertices in cheapest way possible

Running time of straightforward implementation

- O(n) iterations [where n = # of vertices]
- O(m) time per iteration [where m = # of edges]
  --> O(mn) time

Like with Dijkstra's, we can speed up the algorithm with heaps, which are good at minimum computations

Specifically: a heap supports insert, extract-min, and delete in O(logn) time [where n=# objects in the loop]

**Natural idea:** use heaps to store edges, with keys = edge costs --> leads to an O(mlogn) implementation of Prim's algorithm

**But:** using heaps to store vertices results in the same O(mlogn) running time, but with smaller constants, so we'll do that

### Prim's algorithm with heaps

**Invariant #1:** elements in heap = vertices of V - X
**Invariant #2:** for v ∈ V-X, key[v] = cheapest edge (u, v) with v ∈ X [or + infinity if no such edges exist]

We can initialize heap with O(m + nlogn) = O(mlogn) preprocessing -> It's O(m) to compute keys and O(nlogn) for n-1 inserts

Note: extract-min yields next vertex v ∉ X and edge (u, v) crossing (X, V-X) to add to X and T, respectively

How do we maintain invariant #2?
**Issue:** when we add a new vertex to the MST, we might need to recompute some keys to maintain invariant #2 after each extract-min

**Pseudocode:**
When v is added to X:
_ For each edge (v, w) ∈ E:
_ If w ∈ V - X:
_ Delete w from heap
_ Recompute key[w] := min[key[w], (v, w)] \* Re-insert w into heap

**Running time with heaps:**

- Dominated by time required for heap operations
- (n-1) inserts during preprocessing
- (n-1) extract-mins come per iteration of while loop
- Each edge (v, 1) triggers one delete/insert combo [when its first endpoint gets sucked into X]
  --> O(m) heap operations per iteration
  --> O(mlogn) time
