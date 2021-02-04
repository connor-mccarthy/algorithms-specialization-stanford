# Strassen's Noncubic Matrix Multiplication Algorithm
## Problem
Multiplication of two `nxn` matrixes X and Y to get a third `nxn` matix z

where $z_{j} = (i^{th} \space row \space of \space x)\cdot{(j^{th} \space column \space of \space y)}$

Input has size n\**2 and output has size n**2, so the best we can hope for is `O(n**2)`

Iterative algorithm time: `theta(n**3)` (think: triple for loop)

## Divide and conquer solution 1
Algorithm:
Recusrisevely compute the 8 necessary products. Then, do the necessary additions (O(n**2)) time.

$$X \cdot Y = 
\begin{pmatrix}
a & b\\ 
c & d\\
\end{pmatrix}
\cdot
\begin{pmatrix}
e & f\\ 
g & h\\
\end{pmatrix}
=
\begin{pmatrix}
ae + dg & af + bh\\ 
ce + dg & cf + dh\\
\end{pmatrix}$$



Runtime: O(n**3) --> not better thatn the iterative approach

## Divide and conquer solution 2
Algorithm:
Recursively compute only 7 cleverly chosen products. Then, do the necessary (clever) additions and subtractions (still O(n**2) time)

$$P_{1} = A(F-H)$$
$$P_{2} = (A+B)H$$
$$P_{3} = (C+D)E$$
$$P_{4} = D(G-E)$$
$$P_{5} = (A+D)(E+H)$$
$$P_{6} = (B-D)(G+H)$$
$$P_{7} = (A-C)(E+F)$$

$$X \cdot Y = 
=
\begin{pmatrix}
ae + dg & af + bh\\ 
ce + dg & cf + dh\\
\end{pmatrix}
=
\begin{pmatrix}
P_{5} + P_{4} - P_{2} + P_{6} & P_{1} + P_{2}\\ 
P_{3} + P_{4} & P_{1} + P_{5} - P_{3} - P_{7}\\
\end{pmatrix}$$

Runtime: Better than cubic time, but have to wait until master method lecture to see
