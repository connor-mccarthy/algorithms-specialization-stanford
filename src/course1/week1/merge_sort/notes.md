# Merge Sort
Why merge sort?
* Good intro to divide and conquer
* Improves over Selection
  * Pass repeatedly passing over whole array to find the next minimum
* Insertion
  * Repeatedly moving the next unsorted item to it's place in front (sorted) part of the array
* Bubble sorts
  * Identify adjacent pairs of elements that are out of order and do repeated swaps

These worse options complete in quadratic time (`n^2`). Merge Sort does better.

We're going to do worst-case and asymptotic analysis on Merge Sort.