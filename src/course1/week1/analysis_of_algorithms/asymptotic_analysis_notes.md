# Asymptotic analysis

## High level idea
> suppress constant facors and lower-order terms

Constant factors --> too system/language dependent to be useful to consider
Lower-order terms --> irrelevant for large inputs

# Big-Oh formal definition
* let T(n) = function on n, where n is input size (n=1, 2, 3, ...)
* When is T(n) = O(f(n))? For example, you can ask for a given algorithm, is T(n) = O(nlogn)? Or, is T(n) = O(n^2)?
  * If eventually (for all sufficiently large n), T(n) is bounded above y a constant multiple of f(n)
  * In other words, if you plot T(n) and f(n), then multiple f(n) by any constant, if you go far enough right on the graph, T(n) will never cross that constant * f(n)
* Formal definition:
> T(n) = O(f(n)) if and only if there exists constant c, n0 (n-naught) > 0 such that T(n) <= f(n) for all n >= n0.

Note: c, n0 but be __cannot__ depend on n.