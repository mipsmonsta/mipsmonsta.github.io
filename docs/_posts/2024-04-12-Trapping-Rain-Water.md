---
layout: post
title: Trapping Rain Water
date: 2024-04-12 21:59 +0800
categories: leetcode, python
---

### Leetcode 42 Hard

This question involves a land basin where rain water may be collected across the mountainous terrain. A list of the heights of the terrain is given where at position i, the height of zero to higher is given. At the sides of the basin i.e. outside, you can assume the height is zero. You are tasked to return the amount of water trapped in the basin.

### Key insight

Imagine you are at position i, the water level is determined by the minimum of the highest walls to the left and right *and* the height itself at i. Imagine if the height is higher than the water level computed from the wall heights, then we just subtract the height[i] to get the resultant water level at i. Conversely if the height[i] is higher, then result water level should be zero.

The one math equation as aforementioned can be conceived: 

```
water height at i = max(min(max_wall_left, max_wall_right) - height[i], 0)

```

Now what is left is finding the max wall height to the left and to the right.

### Code 

```python

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n # maximum wall height to left not including position i
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])

        max_right = [0]*n # maxmum wall height to right not including position i
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        totalWater = 0
        for i in range(n):
            waterheightAtI = max(min(max_left[i], max_right[i]) - height[i], 0)
            totalWater += waterheightAtI

        return totalWater
```

The hard problem is not that tough once you have the insights.