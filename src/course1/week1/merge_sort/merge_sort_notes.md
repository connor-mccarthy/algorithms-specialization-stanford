# Merge Sort

Why merge sort?

- Good intro to divide and conquer
- Improves over:
  - Selection sort
    - Pass repeatedly passing over whole array to find the next minimum
  - Insertion sort
    - Repeatedly moving the next unsorted item to it's place in front (sorted) part of the array
  - Bubble sorts
    - Identify adjacent pairs of elements that are out of order and do repeated swaps

These worse options complete in quadratic time (`n^2`). Merge sort does better.

We're going to do worst-case and asymptotic analysis on merge sort.

Will also look at recursion tree: how many primitive operations are required for an algorithm to finish.

## The algorithm

- Input: array of `n` numbers
- Output: output array of the same `n` numbers, sorted from smallest to largest

It's a recursive, divide and conquer algorithm.

Step 1. Split the array in half.  
Step 2. Sort sub-arrays  
Step 3: Merge the smaller sub-arrays into the resulting array

## Performance

- Can approximate run-time with the # of lines of code executed

Counting operations for merge subroutine:

- Set counters `i` and `j` (2 operations)
- n times (for each element):
  - Compare `a_i` to `b_j`, assign, and increment (3 operations)
  - Increment `k` (1 operation)

Runtime: Given an array of n numbers, it's `O(4n + 2)` (`<= 4n + 2`)

We can collapse `<= 4n + 2` into `<= 6n` (since `n>=1`, so `6n` will always be at least `4n+2`

## Deeper performance investigation

Claim: merge sort never requires more than `6n * log2(n) + 6n` operations to sort `n` numbers `<=6n * log2(n) + 6n`

This is faster than other simpler sorting methods which are quadratic in time, or a constant times `n^2`. Merge sort needs at most a constant times `n * log(n)` --> big win.

## Three biases as guiding principles for performance analysis

1. Use worst cast analysis --> make no domain assumptions, probability of different inputs, etc.
2. Don't focus on constants and lower order terms
3. Focus on rate of growth as `n` gets very large(asymptotic analysis)

Putting the three together...

> Fast algorithms --> an algorithm with a worst-case run time that grows slowly with input size

This definition is a sweet spot for analysis:

- Not keeping track of everything --> it's mathematically tractible to think about algorithms this way
- We still maintain some predictive power over how long algorithms take

> Holy grail: linear run time (algorithm with a run-time that grows linearly with the input)
