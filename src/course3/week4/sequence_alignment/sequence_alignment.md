# Sequence Alignment

## Problem definition
__Recall:__ sequence alignment; Needleman-Wunsch score = similarity measure between two strings
__Example:__ AGGGCT v AGGCA

AGGGCT
AGG-CA

__Input:__ strings X=x_1... x_m, Y = y1 ... ym over some alphabet (e.g. {A C G T}) and mis the number of characters in each string

--> penalty is the the gap for matching strings

__Feasible solution:__ goal is to compute among the exponentially many alignments the total penalty

## Dynamic programming approach
__Key step:__ identify subproblems. As usually, will look at structure of an optimal solution for clues [i.e. develop an optinal solution for clues]

__Structure of optimal solution:__ consider an optinal alignment of X, Y aand its final position

How many relevant possibilites for the final position? --> 1) could be a gap in X and not Y, 2) could be a gap in Y and not X, 3) could be a gap on both

## Optimal substructure
__Point:__ narrow optimal solution down to 3 candidates
__Optinal substructure:__ Let X'=X-X_m_1; Y' = Y-y_n

**Cases**
1) X_m and Y_n
2) X_m and gap
3) Y_n and gap

If case (1) holds, then induced alignment of X' and Y' is optimal
If case (2) holds, then induced alignment of X' and Y is optimal
If case (3) holds, then induced alignment of X and Y' is optimal