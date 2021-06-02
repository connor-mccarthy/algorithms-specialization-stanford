# Lecture 2: Karatsuba multiplication

`x = 5678`  
`y = 1234`

Problem: multiply `x` and `y`

## Implementation (single pass of recursive algorithm)

Split `x` into `a` and `b` and `y` into `c` and `d`

`a = 56`
`b = 78`

`a = 12`
`b = 34`

Steps:

1. Compute `a*c` = 674
2. Compute `b*d` = 2652
3. Compute `(a+b)(c+d)` = 134 \* 46 = 6164
4. Compute `ad + bc` = step 3 - step 2 - step 1 = 2840
5. Then `((10 ** (n)) * ac) + ((10 ** (n/2)) * (ad + bc)) + bd` is result
