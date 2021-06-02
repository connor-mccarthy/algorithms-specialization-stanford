# Randomized Selection

## The problem

- Input: array A with n distinct numbers and a number i ∈ {1, 2, ..., n}
- Output: ith order statistic (i.e., the ith smalleset element of the input array)

The fact that the numbers are distinct is not a very large assumption

## Sorting as a solution

Problem reduces easily to a sorting algorithm O(n logn):

1. Apply mergesort
2. Return the ith element of the sorted array

But, we can do a little better. We can get an O(n) time (randomized), by modifying quicksort.

## Randomized selection solution

Randomized selection for array A of length n for statistic i (j below is pivot element):

1. if n = 1, return A[1]
2. choose pivot p from A uniformly at random
3. partition A around p let j = new index of p
4. if j = i, return p
5. if j > i, return randomized_selection(first part of A, j -1, i)
6. if j < i, return randomized_selection(second part of A, n-j, i-j)

## Runtime

- Depends on which pivots get chosen --> could be as bad as O(n\*\*2)
- Key: find pivots giving "balanced" split
- Best pivot: the median! 0< would get recurrence T(n) <= T(n/2) + O(n) --> case 2 of master method [T(n) = O(n)]

> For every input array of length n, the average running time of randomized selection is O(n). The average is over random pivot choices by the algorithm, not the data. This average runtime holds for every input and makes no assumptions about data.
