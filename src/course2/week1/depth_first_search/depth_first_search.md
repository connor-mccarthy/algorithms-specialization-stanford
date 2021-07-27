# Depth-first Search

## DFS Basics

Explore aggressively and only backtrack when necessary.

## Why bother with DFS when you have BFS?

It has some nice properties:

- Also computes a topological odering of a directed acyclic graph
- Computes strongly connected components of directed graphs

## Runtime

O(m + n)

## Code

Mirror BFS code, but use a stack instead of a queue

## DFS Basic Properties

Claim #1: At end of the algorithm, v is marked as explored
Reason: DFS is a particular instatiation of a generic search procedure

Claim #2: Running time is O(n + m)
Reason: Look at each node in connected components at most one
