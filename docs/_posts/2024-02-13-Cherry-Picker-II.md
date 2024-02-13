---
layout: post
title: Solving Cherry Picker II (Leetcode problem 1463)
date: 2024-02-13 17:40:50 +0800
categories: python, Leetcode, Dynamic-Programming
---

### Problem problem problem

In [Cherry Picker II], we are given a grid of rows and columns for two robots to go down row by row, with the starting position of the robotos at row 0 and column 0 and row 0 and column n-1 (given n columns). The question is asking to pick up the *maximum* number of cherry that can be picked up until and inclusive of the cherry at row m - 1 (given m rows).

![Two Robots as Cherry Pickers](/assets/images/two_robots.png "Image from Leetcode.com. TWo robotos cherry pickers.")

### Analysis of constraints

From the problem's constraints, you can that the two robots will always not start from a same position given that there are always more than 2 columns. There are also always more than or equal to 2 rows, so that robotos cannot end when they haven't already started.  

Given the low number of rows / columns at a upper bound of 70, this problem likely can be solved through dynamic programming.

### Things to watch

The question was clear that if two robotos are in the same grid space, only one set of cherries at that space can be picked up. Also the robotos can terminate when they are at row n which is outside the grid, with no further cherries being picked.

### Solution formulation - State Representation

We can represent the state of the robots as they go down row by row. Three variables would be sufficient.

```
dp(i, j, k) where i is the row index, j is the column index of robot 1, and k is the column index 
of roboto 2
```

### Solution formulation - Parent problem to subproblem

At a row, the parent problem is to collect the cherries from the grid that the robots are situated on. Let the cherries be collected in `ans` variable. Notice below that we just a condition i != j. If i == j, then the condition will evaluate to zero under Python and the cherries in `grid[j]` will not be collected twice.

```
    ans = grid[i] + grid[j] * (i != j) 
```

However, we also need to transfer to the next state and the ans should include the returns from the next states. Each robot could moved three position:
1. Row directly, same column i.e. j
2. Row below, but column j - 1
3. Row below, but column j + 1


We represent that in the below transfer function. The `max` function ensure we choose the future states that gives us most cherries.
```
    ans += max([dp(i+1, x, y) for x in range(j-1, j+2) for y in range(k-1, k+2)])
```

### Solution formulation - Terminating base cases

In dynamic programming, we need to know when to terminate. We should stop when the next state is outside the last row, and important when the robots are outside the columns. In such states, we should just return zero cherries.

This is a hard problem, but once you understand the overlapping sub-problem, the state function and use memoization, you can easily solve the problem.

## Python code

```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        @cache # memoization
        def dp(i, j, k) -> int: # maximum cherries both robots take 
                                # starting on the ith row and column j and k
            # base conditions
            # out of bound or complete picking
            if i == m or j < 0 or j >= n or k < 0 or k >= n:
                return 0
            
            # robots reached same grid?
            ans = grid[i][j] + grid[i][k] if j != k else grid[i][j]
            
            # next grid based on path with largest taking of cherry
            ans += max([dp(i+1, x, y) for x in range(j-1, j+2) for y in range(k-1, k+2)])
            
            return ans
            
        return dp(0, 0, n-1)

```


[Cherry Picker II]: https://leetcode.com/problems/cherry-pickup-ii/?envType=daily-question&envId=2024-02-11