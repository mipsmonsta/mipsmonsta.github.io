---
layout: post
title: Line Sweep Alogoritm Showcase (LeetCode 2406)
date: 2024-10-14 08:00:00 +0800
categories: leetcode, python, linesweep
---

## What is the Line Sweep Algorithm

The line sweep algorithm can be imagined as a verticle line that moves from left to right of a 2D plane, stopping at key events. Such key events could be sorted events (e.g. in the form of points or line segments) etc.

In our example for this post, it's used to tracked the number of active intervals at any one point of the plane.

The leetcode question: Divide Intervals Into Minimum Number of Groups, asked that given a array of intervals in 2D, where `intervals[i] = [left_i, right_i]`, find the *minimum* number of groups such that in each groups, the intervals do not overlap. 

### Question Reframed to find the minimum number of overlapping intervals

If we reframe the question's ask. We can see that if there are a maximum `x` number of overlapping intervals at one point in the plane, then a minimum number of groupings required will be `x`.

With this newfound perspective, we could solve the [problem] by:

1. Storing in a map (use the defaultdict in Python), an increment of 1 at the start of an interval and a decrement of 1;

2. Sort the keys of the map in ascending order and iterate through the keys; and 

3. At each key, using a global variable to store the number of active intervals, which is the sum of the values of the map at the key. This is the linesweep algorithm. 

4. Track the maximum value of the store of the number of active intervals. This is the result i.e. the minimum number of groupings of intervals. 

### Python Code

```python
from collections import defaultdict
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        overlapsCount = defaultdict(int) # map tracking points and their overlap counts

        # mark the starting and end points in the dictionary
        for start, end in intervals:
            overlapsCount[start] += 1
            overlapsCount[end + 1] -= 1

        # iterate over the sorted keys of the map
        concurrent_intervals = 0
        max_concurrent_intervals = 0
        for point in sorted(overlapsCount.keys()):
            concurrent_intervals += overlapsCount[point]
            max_concurrent_intervals = max(max_concurrent_intervals, concurrent_intervals)
        
        return max_concurrent_intervals
```

### Analysis

The sweep of the points of `start` and `end` is what consitute the Line Sweep Algorithm, and at each point, we process the information to track the number of active intervals i.e. overlapping intervals. Quite useful.

[problem]: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/