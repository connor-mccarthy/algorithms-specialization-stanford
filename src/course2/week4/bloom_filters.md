# Bloom Filters
A variant on hash tables, but more space efficient. There _are_ errors (non-zero false-positive rate).

## Why do they exist?
* Fast inserts and lookups
* Compared to a hash table:
    * Pro: They are more space efficient
    * Con: Can't store an associated object (just make a record that you've seen an object)
    * Con: No deletions
    * Con: Small false-positive rate (might say x has been inserted even thought it hasn't been)

## Applications
Best when space is at a premium and a small chance of a false-positive is not a dealbreaker

Original application: early spellcheckers
Canonical: list of forbidden passwords
Modern: network routers
* need to be fast, limited memory

## How it works
__Ingredients__
1. Array, where each entry in the array is a single bit, for a total of n bits --> space occupied by a bloom filter is the number of objects s inserted into the bloom filter
(so (n / |s|) = # of bits using per entry in the dataset)

2. k hash functions h_1, ..., h_k (k=small constant)

__Insert(x)__
For i=1, 2, ..., k, set A[h_i(x)] = 1 (whether or not bit was already set to 1)

__Lookup(x)__
For i=1, 2, ..., k, if A[h_i(x)] = 1, return True

__Note__
No false negatives --> if x was inserted, lookup(x) is guaranteed to succeed

Some false positives --> it's possible that you will get false positive (lookup(x) succeeds when it says it should not) if all k h_i(x)'s already set to 1 by other insertions

## Heuristic analysis
There is a tradeoff between space and error (false positive) probability.

If we understand the frontier of this tradeoff, we can find the sweet spot.

__Assume__: [not justified] all h_i(x)'s are uniformly random and independent across different i's and x's.

__Setup__: n bits, insert data set S into bloom filter.

__Note__: for each bit of A, the probability it's been set to I is after inserting all off s: P(1 - (1 - (1/n))**k|s|)

Working up to it:
* Because of the way a bloom filter works, we want to start by determining the probability that a given bit remains zero after all hash function "darts" are thrown, flipping buckets to 1
* P(a bucket is hit by one of the hash functions for one object insert) = P(1/n)
* P(a bucket is not hit by one of the hash functions for one object insert) = P(1 - (1/n))
* P(a bucket is not hit by all of the hash functions for *one* object insert) = P(1 - (1/n))**k
* P(a bucket is not hit by all of the hash functions for *all* object inserts) = P(1 - (1/n))**k|s|
* P(a bucket is hit by at least one of the hash functions for *all* object inserts) = P(1 - (1 - (1/n))**k|s|)

Under assumption, for x ∉ S, false positive probability is <= (1-e**(-k/b))**k, where b is the # of bits per object

__How to set k?__: for fixed b, set k to minimize error probability. This ends up being about k~= (ln2)*b.

Plugging that value back in, we get the tradeoff rate between size and error rate: (1/2)**((ln2)b) (error is exponentially small in b)