# Greedy Algorithms

## Greedy algorithms

**Definition:** iteratively make "myopic" decisions, hope everything works out at the end
**Example:** Dijkstra's shortest path algorithm

- processed each destiantion once, irrevocably

Contrast with divide & conquer

1. Easy to propose multiple greedy algorithms for many problems
2. Easy running time analysis (contrast with master method)
3. Hard to establish correctness (contrast with straightforward inductive correctness proofs)

**Danger:** most greedy algorithms are _not_ correct (even if your intuition says so!)

## Proof of correctness:

Method 1: Proof by induction --> "greedy stays ahead" --> induction made on each of the decisions of the algorithm
Example: Correctness proof for Dijsktra's algorithm

Method 2: Exchange argument

- start by saying the algorithm is not correct, then prove it is

Method 3: Whatever works! Sometimes it's not clear what the best approach is

## Application: Optimal caching

The caching problem:

- There is a small fast memory (the cache)
- There is big slow memory (the main memory)

The task:

- Process a sequence of "page requests"
- On a "fault" (that is, a cache miss), need to evict something from the cache to make room for the thing that isn't already there

## Example

Cache: a, b, c, d
Request sequence: c, d, e

e isn't in the cache, so maybe we evict a to make room for e (cache: e, b, c, d)... and so on... but then what if a (or something else we evicted comes back in the sequence?)

## The optimal caching algorithm

**Theorem:** the "furthest-in-future" algorithm is **optimal** (i.e., minimizes the number of cache misses)

--> this assumes you know what is coming in the future

**Why is it useful?**

1. Serves as a guideline for practical algorithms (e.g. LRU (least-recently used) cache should do well)

- LRU --> assumes the most recently requested recently will be requested again sooon, and the data referenced furthest in the past will be referenced furthest in the future (does well provided data exhibits locality of reference)

2. Serves as idealized benchmark for caching algorithms (e.g., if you implement LRU, you can cross-validate it with what actually happens, after the future happens)

**Proof:** tricky exchange argument, not covered in this course, however
