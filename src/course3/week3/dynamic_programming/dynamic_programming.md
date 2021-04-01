# Dynamic Programm

## Max-weight independent set problem
Start with a problem, then go on to what dynamic programming is

__Input:__ a path graph G=(V, E) with non-negative weights on vertices
```
1     4     5     4
X --> X --> X --> X
```
__Desired output:__ subset of non-adjacent vertices --> an independent set of maximum total weight

For the graph above, this would be 8 (4 and 4)

Let's take a look at some of our current algorithm design paradigms and see how how they do with this problem...

__Greedy approach:__ iterative choose the max-weight vertex not adjacent to any previously chosen vertex --> would choose 5, then choose 1

__Divide and conquer approach:__ recursivelyt compute the max-weight IS of 1st half, ditto for 2nd half, then combine the solutions --> would choose 4 on left, 5 on right, but they are adjacent

## What is dynamic programming?
The key approach is to start by reasonoing about the structure of an optimal solution
__Critical step:__ reason about structure of an optimal solution in terms of optimal solutions of smaller subproblems

__Motivation:__ this thougth experiment narrows down the set of candidates for the optimal solution; can search through the small set using brute-force search

__Note:__ it's not circular to reason about the object you're trying to compute

We're doing a thought experiment, reasoning as _if_ we've already computed it

__Notation:__ Let S ⊆ V be a max-weight independent set (IS); Let V_n=last vertex of path (input graph)

## A case analysis
V_n is either in S or it is not

__Case 1:__ suppose V_n ∉ S. Let G' = G with V_n deleted.
* Note: S also an IS of G'
* Node: S must be a max-weight IS of G'; if S* was better, it would also be better than S in G (which is a contradiction)

__Case 2:__ suppose V_n ∈ S.
Note: previous vertex V_(n-1) ∉ S. Let G'' = G with V_(n-1), V_n deleted
Note: S - {V_n} is an IS of G''
Note: Must in fact be a max-weight IS of G'' -- if S* is better than S in G'', then S* union {V_n} is better than S in G (which is a contraction)

## Toward an algorithm
__Upshot:__ a max-weight IS must be either 1) a max-weight IS of G' or 2) v_n + a max-weight IS of G''
__Corollary:__ If we knew whether or not V_n was in the max-weight IS, we could recursively compute the max-weight IS of G' or G'' and be done
__Idea:__ try both possibilities and return the better solution

__Proposed algorithm:__
* recursively compute S1 = max-weight IS of G'
* recursively compute S2 = max-weight IS of G''
* return S_1 or S_2 union {V_n}, whichever is better

__Good news:__ this would be correct
__Bad news:__ it is exponential time

__Question:__ in both recursive calls, how many distinct subproblems ever get solved by this algorithm? --> we only every solve a linear number of distinct subproblems O(n) --> only 1 for each "prefix" of the graph! [recursion only plucks vertices off from the right]

## Eliminating redundancy
__Obvious-fix:__ the first time you solve a subproblem, cache its solution in a global table for O(1) --> time lookup later on ["memoization"]

__Even better:__ reformulate as a bottom-up iterative algorithm. Let G_i = 1st i of vertices of G

__Plan:__ populate array A left to right with A[i] = value of max-wt IS of G_i

__Initialization:__ A[0] = 0 (empty set); A[1] = W_i

__Main loop:__
* For i=1, 2, 3, 4, ..., n:
    * A[i] = MAX { A[i-1], A[i-2] + w_i}

__Running time:__ obviously O(n)

__Correctness:__ same as recursive brute-force solution, but doesn't waste any time

## A better solution (reconstruction algorithm)
The algorithm above computes the value of the max weight IS, but not the IS itself

__Correct but not ideal:__ store optimal IS of each G_i in the array in addition to its value

__Better:__ trace back through filled in array to reconstruct optimal solution

__Key point:__ we know that a vertex v_i belongs to a max weight IS of G_i <--> W_i + max-weight IS of B_i-2 >= max-weight IS of G_i-1