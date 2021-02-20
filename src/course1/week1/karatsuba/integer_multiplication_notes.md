# Integer multiplication
## Basics
As for all algorithms, define the computational problem (define input and say what the desired output is):
* Input: two n-digit numbers `x` and `y`
* Output: the product `x * y`

e.g. `5678 * 1234` (n=4)

Assess the performance through the number of "primitive operations" (basic operations) required to complete the algorithm


Long multiplication is the typical approach to this.

The algorithm is "correct" --> no matter what integers `x` and `y` you start with, you always end up with the correct product

The amount of "time", or number of primitive operations, needed to complete the algorithm can be viewed as a function of input length `n`

## Performance
Performance as a function of input length `n`

**First partial product** Multiply 4 by 5, 6, 7, and 8 (4 other numbers) and possibly add the carries

* 4 operations for the multiplcation
* At most 4 operations for the addition in the carries
Subtotal: `<=2n` operations

**All partial products thereafter**  
Look the same.
There are n partial products, so that's  `<=2n^2` operations so far.

**Adding it all up**  
Adding the partial product costs about about an additional `2n^2` operations

**Total**  
`<=2n^2 + 2n^2` is `4n^2` operations in the worst case


## Takeaway
The number of operations that the algorithm performs grows at a rate of `constant * n^2` where `constant` is about `4` in this case

So, if you double `n`, the number of operations goes up by about a factor of 4

If you quadruple `n`, the number of operations goes up about about 16
