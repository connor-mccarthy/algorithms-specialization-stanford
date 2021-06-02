# Random contraction algorithm

- Input: an undirected graph G=(V, E); parallel edges (two edges that connect to the same p air of vertices)
- Goal: compute a cut with the fewest number of crossing edges (a min cut)

## Algorithm high-level

While there are more than two vertices:

- pick a remaining edge (u, v) uniformly at random
- merge (or "contract") u and v into a single vertex
- remove self-loops
  return cut represented by two final vertices

Sometimes returns a min cut, sometimes does not. Depends on which vertices are contracted

## How often does it return the min cut?

Pr[min cut is identified] = Pr[never contract an edge of F], where F is the set of edges comprising the min cut

Pr[success] = 2 / (n(n-1)) or >= 1/(n\*\*2)

On its own, it's not very good. But, we can run it lots of times and return the best min cut.

We successfully find the min cut if event _one_ of the trial succeeds. We don't don't find the min cut if _all_ trials fail.

So, Pr[all N trials fail] <= (1 - (1/(n**2))**n

If we take N = (n**2)ln(n) trials, Pr[all fail] <= (1/e)**(ln(n)) = 1/n

## Running time

Polynomial in n and m, but slow Omega(n\*\*2)(m)
