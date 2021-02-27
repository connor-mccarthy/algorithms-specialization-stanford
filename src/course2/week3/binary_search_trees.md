# Balanced Binary Search Trees
Think of it as a dynamic sorted array

## Sorted array operations (static)
* Search -> O(logn) -> you throw out half each time
* Select (given order statistic i) -> O(1) -> because sorted
* Min/max -> O(1) -> because sorted
* Predecessor/successor (given pointer to a key) -> O(1) -> becaause sorted
* Rank (i.e., # of keys less than or equal to a given value) -> O(logn) -> no harder than search
* Output keys in sorted order (from smallest to largest) -> O(n) -> just need to read through all the items in order

## Balanced binary search tree operations (dynamic)
We give up a little from the sorted arrays, to get a lot of speed on insertion and deletion

So, the reason binary search trees exist is for the insertion and deletion operations -> it's a sorted list, but we can quickly add and delete elements
* Search -> O(logn)
* Select -> O(logn) (up from O(1))
* Min/max -> O(logn) (up from O(1))
* Pred/succ -> O(logn) (up from O(1))
* Rank -> O(logn)
* Output in sorted order O(n)
* Insertions -> O(logn) (new)
* Deletions -> O(logn) (new)

If you only need insertions, deletions, and remembering the smallest, a binary search tree is overkill -> just use a heap! It's faster.

If you just need to be able to do insertions and lookups (don't need ordering), the data structure of choice is a hash table.

Balanced binary search tree has a very rich set of operations for working with data.