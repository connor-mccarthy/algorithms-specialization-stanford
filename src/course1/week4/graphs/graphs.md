# Graphs

Two ingredients:

* vertices (aka nodes) (v)
* edges (E) = pairs of vertices
  * can be undirected (an unordered pair)
  * or can be directed (ordered pair)

## Examples

* road networks
* the web
* social networks
* precedence constraints (must take class x before yout take class y)

## Cut of a graph

Definition: a __cut__ of a graph (V, E) is a partition of V into two non-empty sets A and B

Definition: the __crossing edges__ of a cut (A, B) are those with:

* one endpoint in each of (A, B) [undirected]
* tail in A, head in B [directed]

## The minimum cut

* Input: an undirected graph G=(V, E); parallel edges (two edges that connect to the same pair of vertices)
* Goal: compute a cut with the fewest number of crossing edges (a min cut)

## Graph partitioning problem applications

* Identify weaknesses/bottlenecks in a network
* Community detection in social networks
* Image segmentation for primary object detection

## Min and max edges for n vertices
n vertices, no parallel edges, and is connected ("in one piece")
Min edges: `n - 1`
Max edges: `n(n-1)/2`
## Sparse v. Dense Graphs

Let n = # vertices, m = # edges

In most (but not all) applications, m is Omega(n) and O(n**2)

Has to do with the number of edges:

* In a "sparse graph", m is O(n) or close to it
* In a "dense graph", m is closer to O(n**2)

## Representations

### The adjacency matrix

Represent edges of a graph with a nxn O-1 (binary) matrix A, where A_ij iff there is an edge between i and j in the graph

Variants:

* A_ij = # i-j edges if parallel edges
* A_ij = weight of i-j edges (if any)
* A_ij = +1 if i->j or -1 if i<-j

Size: Theta(nxn)

In a sparse graph, this is a super wasteful representation 

### Adjacency lists

A less wasteful representation for a sparse matrix

Ingredients:

* Array (list) of vertices
* Array (list) of edges
* Each edge points to its endpoints
* Each vertex points to edges incident on it

Size: Theta(m + n)

### Which representation is better?

Depends on graph density and operations needed. We'll focus on adjacency lists.