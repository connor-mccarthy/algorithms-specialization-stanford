# Application of Kruskal's MST to Clustering

**Informal goals:** given n "points" [web pages, images, genome fragments, etc.], classify into coherent groups

**Assumptions:**

1. as input, given a (dis)similarity measure --> a distance d(p, q) between each point pair.
2. symmetric [i.e. d(p, q) = d(q, p)]

Examples: Euclidean distance, genome similarity, etc.

Goal: Sam ecluster <--> "nearby"

## Max-spacing k-clustering

**Assume:** we know k := number of clsuters desired [in practice, can experiment]
Call p & k separated if they are assigned to different clusters

**Problem statement:** given a distance measure d and k, compute the k-clustering with maximum spacing

## Pseudocode

- Initially each point in a separate cluster
- Repear until only k clusters:
  - Let p, q = closest pair of separated points (determined by current spacing)
  - Merge the clsuters containing p and q into a single cluster

**Note:** just like kruskal's MST algorithm, but stopped early. Points <--> vertices; distances <--> edge costs; point pairs <--> edges

This is called _single-link_ clustering

## Correctness

### Correctness claim

**Theorem:** single-link clutering finds the max-spacing k-clustering
**Proof:** Let C1, ..., Ck = greedy clustering with spacing s
Let C1_hat, ..., Ck_hat = arbitrary other clustering
**Need to show:** spacing of C1_hat, ..., Ck_hat <=s

**Case 1:** Ci_hats are the same as the Cis --> has the same spacing as s

**Case 2:** otherwise, can find a point pair p, q such that A) p, q in the same greedy clustering Ci, B) p, q in different clusters Ci_hat, Cj_hat

**Property of greedy algorithm:** if two points x, y, "directly merged" at some point, then d(x, y) <=s [distance between merged point pairs only goes up]
