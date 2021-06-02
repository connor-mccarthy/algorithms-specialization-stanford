# Algorithm for Counting Inversions

## The Divide and Conquer Paradigm

1. Divide into smaller subproblems
2. Conquer via recursive calls
3. Combing solutions of subproblems into one for the original problem

## The Problem

- Input: array A containing the numbers 1, 2, 3, ..., n in some arbitrary order

- Output: the number of inversions = the number of pairs (i, j) of the array with `i<j` and `A[i] > A[j]` (where earlier (left) entry is bigger than the later (right) entry)

Example:

- Array: [1, 3, 5, 2, 4, 6]
- Inversions: (3, 2), (5, 2), (5, 4)

Motivation: to have a numerical similarity measure that quantifies how similar two ranked lists are

- Think: recommendation engine (collaborative filtering) --> take your friend's list of favorite movies is the ordered list and the fewer inversions in your list, the more similar you are to your friend

Notes:

the largest number of inversions a 6-element array can have is 15 --> largest number is n choose two

$${n \choose 2} == \frac{(n)(n-1)}{2}$$
recall:
$${n \choose k} == \frac{n!}{k!(n-k)!}$$

## High level of divide and conquer approach

Three types of inversions:

1. left if i, j <= n/2 (can compute recursively)
2. right if i, j > n/2 (can compute recursively)
3. split if i <= N/2 < j (need a second subroutine for this)

Steps:
if n=1, return 0
else:
x = count(1st half of A, n/2)
y = count(2nd half of A, n/2)
z = countsplitinv(A, n)
return x + y + z

The crux is implementing `countsplitinv()` in linear (O(n)) time. If we do this, the whole algorithm will run in O(n logn) time because two recursive calls, each of half the size O(logn), then outside the recursive calls doing linear work O(n).
