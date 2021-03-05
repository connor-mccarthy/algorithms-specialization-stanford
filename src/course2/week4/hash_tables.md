# Hash Tables
Best to think of a has table as an array. Arrays are really good at is immediate random access.

__Purpose__: To maintain a possible evolving set of stuff (transactions, people + associated data, IP addresses, etc.)

## Operations
__Insert__: add new record
__Delete__: delete existing record
__Look up__: check for a particular record

All three operations use a "key".

All three operations run in constant time.

Sometimes referred to as a "dictionary", but this is somewhat misleading because a hash table does not maintain an ordering of the elements it supports.


## Application: De-duplication
__Given__: a "stream" of objects
* e.g. linear scan through a huge file
* e.g. objects arriving in real time

__Goal__: remove duplicates (i.e. keep track of unqiue objects)
* e.g., report unique visitors to website
* avoid duplicates in search results

__Solution__: when new object x arrives: 1) look up x in hash table H, 2) if not found, insert x into H

## Application: 2-SUM problem
__Input__: unsorted array of n integers and a target sum t
__Goal__: determine whether or not there are two numbers x, y in A with x+y=t
__Naive solution__: Theta(n**2) time via exhaustive search
__Better__: 1) sort A (Theta(nlogn) time), 2) for each x in A, look for t-x in A via binary search (Theta(nlogn)) --> total running time: O(nlogn)
__Amazing__: 1) insert elements into hash table H (O(n) time), 2) for each x in A, look up t-x in H (O(n)) --> O(n) time

## Further immediate applications
* Historical applications: symbol tables in compilers
* Block network traffic (looking up packet senders)
* Search algorithms (e.g., game tree exploration)
    * Use has table to avoid exploring any configuration (e.g., arrangement of chess pieces) more than once

## Two caveats:
1) You need to implement it correctly (it's easy to mess up)
2) The data must be non-pathological (to be discussed)

## Implementation
__Setup__: universe U (e.g., all IP addresses, all names, all chess board configurations, etc.) [generally, REALLY big]
__Goal__: want to maintain evolving set S <= U [generally, of reasonable size]
__Naive solutions__:
1) array-based solution [indexed by u]
* O(1) operations, but O(|u|) space
2) list-based solution
* O(|s|) space, but O(|s|) lookup
__Solution__:
1) Pick n=# of "buckets", with n~=|s| (for simplicity, assume |s| doesn't vary too much, even if its content does)
2) Choose a hash function h: u->{0, 1, 2, ..., n-1} (takes in an element from the universe and maps to a bucket)
3) Using array A of length n, store x (belonging to u) in A[h(x)]

## Resolving collisions
__Collision__: distinct x, y, ∈ such that h(x)=h(y)
__Solution #1__: (separate) chaining
* keep linked list in each bucket with an unbounded number of elements
* given a key/object x, perform Insert/Delete/Lookup in the list in A[h(x)] -> bucket is a linked list [[Alice], [None], [Bob, Daniel]]
__Solution #2__: open addressing (only one object per bucket)
* hash function now specifies probe sequence
* preferred over chaining if space is at a premium
* examples:
    * linear probing --> keep trying subsequent buckets until you find an open slot
    * double hashing --> use two hash functions

## What makes a good hash function?
__Note__: in has table with chaining, insert is O(1)

O(probe sequence) for insert/delete -> could be anywhere from m/n to m for m objects

Performance depends on choice of hash function
* If hash function spreads data out evenly, not so bad
* If hash function puts all the elements in the same bucket, that would be bad

__Properties of a "good" hash function__
1. Should lead to good performance --> i.e., should "spread data out" (gold standard: completely random hashing)
2. Should be easy to store/very fast to evaluate

## Bad hash functions
Example: keys=phone numbers (10-digits)
* |u| = 10**10
* terrible hash function: h(x) = first three digits (area code) --> you have a very slow lookup time for everyone in Stanford
* mediocre hash functino: h(x) = last 3 digits of x --> still somewhat vulnerable to patterns in last 3 digits

Example: keys=memory locations (will be multiples of a power of 2)
* bad hash function: h(x) = x % 1000 --> all odd buckets guaranteed to be empty

## Quick-and-dirty hash function
Objects  --"hash code"-->  integers  --"compression function-->  buckets {0, 1, 2, ..., n-1}

* Hash code --> e.g. subroutine to convert string to integers
* Compression function like the mod function w.r.t. number of buckets

__How to choose n (# of buckets)__
If elements share a common factor with number of buckets, modulus will lead to some buckets remaining empty

E.g. if all data elements are multiples of two and # buckets is even, you have a common factor of 2 which will leave odd buckets empty

1) Choose n to be a prime (within small constant factor of # of objects in table) --> has few common factors
2) Not too close to a power of 2
3) Not too close to a power of 10

## The load of a hash table
__Definition__: the load factor of a hash table is

α := (# objects in hash table) / (# buckets of hash table)

Open addressing does not support α > 1. Chaining does.

__Note__
Will only have constant time lookups if you keep a constant load.
1) α < 1 is necessary condition for operations to run in constant time
2) with open addressing, need α < 1

__Upshot__: for good hash table performance, need to control load

## Pathological datasets
__Upshot #2__: For good hash table performance, you need a food hash function (spreads out data evenly across buckets)

A super clever hashing function that always spreads out every data set evenly does not exist --> for every hash function, there is a pathological data set

__Reason__: fix a hash function h:u -> {0, 1, 2, ..., n-1} (assume |u| >= n) -> a la Pigeonhole Principle, there exists a bucket i such that at least |u| / n elements of u hash to i under h

## Pathological data in the real world
A pathalogical dataset can be used in a DOS attack, for example. You can paralyze several real-world systems (e.g., network intrusion detection) by exploiting badly designed hash functions.

Risky aspects of a hash function:
* open source
* overly simplistic hash function

Can make it easy to reverse engineer a pathological data set.

## Solutions to making secure hash functions
1) Use a cryptographic hash functions (e.g., SHA-2)
* Infeasible to reverse-engineer a pathological data set
2) Use randomization
* Design a family of hash functions such that almost all functions spread out the dataset pretty evenly