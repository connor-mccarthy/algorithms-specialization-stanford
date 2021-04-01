# Huffman Codes

## General
__Use:__ for constructing a certain kind of prefix-free binary code

__Binary code:__ maps each character to an alphabet Σ to a binary string

__Example:__ Σ = a - x and various punctuation (size 32 overall, say)

__Obvious encoding:__ use the 32 5-bit binary string to encode this Σ (a fixed length) (2**5 = 32)

__Can we do better?:__ yes, if some characters of Σ are much more frequent than others, usnig a variable-length code

## Ambiguity
An issue arises when you pass fixed-length encodings to variable-length encodings

__Example:__ suppose Σ = {A, B, C, D}. Fixed length encoding would be {00, 01, 10, 11}; if instead we use {0, 01, 10, 1}, how do we decode sequence 001? we can't without more information

The solution is prefix-free codes

## Prefix-free codes
__Problem:__ with variable-length codes, not clear where one character ends + the next one begins

__Solution:__ prefix-free codes -- make sure that for every pair i, j ∈ Σ, neither of the encodings f(i), f(j) is a prefix of the other

__Example:__ alphabet {A, B, C, D} encoded to {0, 10, 110, 111}
![fixed_variable_length_encoding_comparison](fixed_variable_length_encoding_comparison.png)

## Problem definition
### Codes as trees
__Goal:__ best binary prefix-free encoding for a given set of character frequencies

__Useful fact:__ binary codes <--> binary trees

Examples: Σ = {A, B, C, D}

![binary_encodings_as_binary_trees](binary_encodings_as_binary_trees.png)
Left: fixed length encoding
Middle: variable-length encoding that is NOT prefix-free (that's why intermediate nodes are labeled) (labeled non-leaf nodes -> not a complete binary tree)
Right: variable-length PREFIX-FREE encoding with only leaf nodes labeled

### Prefix-free codes as trees
__In general:__
* left child edges <--> 0; right child edges <--> 1
* for each i ∈ Σ, exactly 1 node labeled i
* encoding of i ∈ Σ <--> bits along path from root to the node [since prefixes <--> one node an ancestor of another]

__To decode:__ repeatedly follow path from the root until you hit a leaf [ex: 0110111] [unambiguous, since only leaves are labeled]

__Note:__ encoding length of i ∈ Σ = depth of i in tree

### Problem definition
__Input:__ probability p_i for each character i ∈ Σ
__Notation:__ if T=tree with leaves <--> symbols of Σ, then L(T) = average length encoding = Σ (sum over i ∈ Σ) p_i * [depth of i in T] = average depth of i in T where weights are p_i

__Output:__ a binary tree T minimizing the average encoding length L(i)

## The solution
### Building a tree
__Question:__ whaht's a principled approach for buildin a tree with leaves <--> symbol of Σ
__Natural but suboptimal idea:__ top-down / divide and conquer
* partition  Σ into  Σ, Σ_2 each with ~50% of total frequency
* recursively compute T for  Σ, T_2 for Σ, return the tree

__Huffman's (optimal) idea:__ build tree bottom-up, using successive mergers

__Question:__ which pair of symbols is "safe" to merge?
__Observation:__ final encoding of i ∈ Σ = # of mergers its subtree endures --> we want to merge is from least to most frequency

### How to recurse?
__Suppose:__ 1st iteration of algorithm merges symbols a & b
__Idea:__ replace the symbols a, b by a new meta symbol with p_a + p_b

__Actual recusion:__
* merge together least probable symbols, treat these merged symbols as a meta-symbol with p_meta_symbol = sum(prob of all symbols in meta symbol)
* the tree is built by reversing the bullet above

### Huffman's algorithm
![huffmans_algorithm](huffmans_algorithm.png)
