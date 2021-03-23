# Greedy Algorithms

## Greedy algorithms
__Definition:__ iteratively make "myopic" decisions, hope everything works out at the end
__Example:__ Dijkstra's shortest path algorithm
- processed each destiantion once, irrevocably

Contrast with divide & conquer
1. Easy to propose multiple greedy algorithms for many problems
2. Easy running time analysis (contrast with master method)
3. Hard to establish correctness (contrast with straightforward inductive correctness proofs)

__Danger:__ most greedy algorithms are _not_ correct (even if your intuition says so!)

## Proof of correctness:
Method 1: Proof by induction --> "greedy stays ahead" --> induction made on each of the decisions of the algorithm
Example: Correctness proof for Dijsktra's algorithm

Method 2: Exchange argument
* start by saying the algorithm is not correct, then prove it is

Method 3: Whatever works! Sometimes it's not clear what the best approach is

### Application: scheduling
* Tasks to be completed are called jobs
* Each job j has a known length l_j, which is the amount of time required to process the job
* Each job j has a known weight w_j, with higher weights corresponding to higher priority jobs
* The schedule is the order in which to process the jobs
* In a problem with n jobs, there are n! different schedules
* We need to define an objective function that assigns a numerical score to every schedule

Completion times: The completion time of job j in schedule s is the sum of the lengths of the jobs preceding j in s, plus the length of j itself (the total time elapsed before the job has been processed)

### Objective function
There are tradeoffs: jobs scheduled early have short completion times, while those scheduled later have long completion times

One way to make trade-offs between jobs is to minimize the sum of weighted completion times. The objective function translates to the following, where sigma is the schedule and C_j is the completion time of job j in schedule sigma. (Minimizing the weighted average of completion times, with averaging weights proportional to w_js):

![scheduling_completion_time](scheduling_completion_time.png)

## Two special cases
The first step is to solve two special cases of the general problem, then use those to suggest what a greedy algorithm would look like in the general case.