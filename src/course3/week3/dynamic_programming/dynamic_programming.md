# Dynamic Programm

## Max-weight independent set problem

Start with a problem, then go on to what dynamic programming is

**Input:** a path graph G=(V, E) with non-negative weights on vertices

```
1     4     5     4
X --> X --> X --> X
```

**Desired output:** subset of non-adjacent vertices --> an independent set of maximum total weight

For the graph above, this would be 8 (4 and 4)

Let's take a look at some of our current algorithm design paradigms and see how how they do with this problem...

**Greedy approach:** iterative choose the max-weight vertex not adjacent to any previously chosen vertex --> would choose 5, then choose 1

**Divide and conquer approach:** recursivelyt compute the max-weight IS of 1st half, ditto for 2nd half, then combine the solutions --> would choose 4 on left, 5 on right, but they are adjacent

## What is dynamic programming?

The key approach is to start by reasonoing about the structure of an optimal solution
**Critical step:** reason about structure of an optimal solution in terms of optimal solutions of smaller subproblems

**Motivation:** this thougth experiment narrows down the set of candidates for the optimal solution; can search through the small set using brute-force search

**Note:** it's not circular to reason about the object you're trying to compute

We're doing a thought experiment, reasoning as _if_ we've already computed it

**Notation:** Let S ⊆ V be a max-weight independent set (IS); Let V_n=last vertex of path (input graph)

## A case analysis

V_n is either in S or it is not

**Case 1:** suppose V_n ∉ S. Let G' = G with V_n deleted.

- Note: S also an IS of G'
- Node: S must be a max-weight IS of G'; if S\* was better, it would also be better than S in G (which is a contradiction)

**Case 2:** suppose V*n ∈ S.
Note: previous vertex V*(n-1) ∉ S. Let G'' = G with V\_(n-1), V_n deleted
Note: S - {V_n} is an IS of G''
Note: Must in fact be a max-weight IS of G'' -- if S* is better than S in G'', then S* union {V_n} is better than S in G (which is a contraction)

## Toward an algorithm

**Upshot:** a max-weight IS must be either 1) a max-weight IS of G' or 2) v_n + a max-weight IS of G''
**Corollary:** If we knew whether or not V_n was in the max-weight IS, we could recursively compute the max-weight IS of G' or G'' and be done
**Idea:** try both possibilities and return the better solution

**Proposed algorithm:**

- recursively compute S1 = max-weight IS of G'
- recursively compute S2 = max-weight IS of G''
- return S_1 or S_2 union {V_n}, whichever is better

**Good news:** this would be correct
**Bad news:** it is exponential time

**Question:** in both recursive calls, how many distinct subproblems ever get solved by this algorithm? --> we only every solve a linear number of distinct subproblems O(n) --> only 1 for each "prefix" of the graph! [recursion only plucks vertices off from the right]

## Eliminating redundancy

**Obvious-fix:** the first time you solve a subproblem, cache its solution in a global table for O(1) --> time lookup later on ["memoization"]

**Even better:** reformulate as a bottom-up iterative algorithm. Let G_i = 1st i of vertices of G

**Plan:** populate array A left to right with A[i] = value of max-wt IS of G_i

**Initialization:** A[0] = 0 (empty set); A[1] = W_i

**Main loop:**

- For i=1, 2, 3, 4, ..., n:
  - A[i] = MAX { A[i-1], A[i-2] + w_i}

**Running time:** obviously O(n)

**Correctness:** same as recursive brute-force solution, but doesn't waste any time

## A better solution (reconstruction algorithm)

The algorithm above computes the value of the max weight IS, but not the IS itself

**Correct but not ideal:** store optimal IS of each G_i in the array in addition to its value

**Better:** trace back through filled in array to reconstruct optimal solution

**Key point:** we know that a vertex v_i belongs to a max weight IS of G_i <--> W_i + max-weight IS of B_i-2 >= max-weight IS of G_i-1
