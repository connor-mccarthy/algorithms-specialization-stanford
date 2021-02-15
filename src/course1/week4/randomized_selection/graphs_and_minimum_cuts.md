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
