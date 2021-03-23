# Applications of this Week's Algorithms

## Graphs and the internet
__Claim:__ the internet is a graph, where vertices = end hosts + routers, directed edges = directed phyisical or wireless connections

Other graphs related to the internet
- Web graph [vertices = web pages, edges = hyperlinks]
- Social media networks (friends (undirected) on Facebook, following (directed) on Twitter)

__Question:__ What is the shortest path between my host are yours?

__Recall from Part I:__ Dijkstra's algorithm does this (with non-negative edge-lengths)

__Issue:__ To use Dijkstra's your host would need to know the entire internet

Need a shortest-path algorithm that can be distributed where each host only does local computation

__Solution:__ The Bellman-Ford algorithm

## Sequence alignment
This is a fundamental problem in computational genomics.

__Input:__ two strings over the alphabet [A, C, G, T] --> these are portions of one or more genomes

Example strings
"AGGGCT"
"AGGCA"

Example applications:
1. Extrapolate function of genome substrings
2. Similar genomes can reflect proximity in evolutionary tree

### Measuring similarity
__Question:__ What does similar mean?
__Intuition:__ AGGGCT, AGGCA are similar because they can be "nicely aligned": AGGGCT AGG_CA
__Idea:__ measure similarity via quality of best alignment
__Assumption:__ we have experimentally determined penalties for caps and the possible matches

### Problem statement
__Input:__
* 2 strings over {A, C, G, T}
* penalty pen_gap >= 0 for each gap
* penalty pen_a_t >=0 for mismatching A & T
* etc

__Output:__ alignment of the strings that minimize the total penalty --> called the Needleman-Wunsch score

__Note:__ this measure of genome similarity would be useless without an efficient algorithm for finding the best alignment

__Brute-force search:__ try all possible alignments and remember the next one --> This would take 2**500 (exponential in n), so we still need a fast algorithm

__Solution:__ Dynamic programming