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