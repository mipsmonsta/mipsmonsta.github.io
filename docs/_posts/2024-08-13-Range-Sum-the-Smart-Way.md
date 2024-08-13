---
layout: post
title: Range Sum the Smart Way (Leetcode problem 1508)
date: 2024-08-13 08:00:00 +0800
categories: python, Leetcode,
---

# Range Sum Problem

You are given an an array of positive numbers. Continous subarray sums are form from the array. These are sorted and then the sums are added from the left index to the right index.

## Solving the problem - The Clever Algorithm

Take for the input nums array of [1,2,3,4].

The idea is to use a queue. In the queue, create a tuple for each of the original array numbers e.g. (1, 0). The second number is 0 is the index of the original num. Note that it's not important to sort the nums before taking the index.

Create a minheap from the queue.
Pop the smallest tuple. Check the index stored in the tuple. Add the nums[index+1] to the first element of the tuple. Create a new tuple (1+x, 1) from the example of (1, 0) where x = nums[index+1], and add back to the minHeap. Stop this operations if index + 1 == size of the original nums array.

So if there is X numbers in nums originally, we will have X streams of sums. As these sums are popped from the smallest to largest from the minHeap, we start adding to the answer if the popped sum if the 'left' number of sum popped. Conversely, stop the adding after the 'right' number sum is popped. 

## Code 

If you don't get it, some code to open your mind below.

```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        newNums = [] # to hold tuples (sum, i) where sum is the sum up to i
        MOD = 1000000007
        n = len(nums)

        # initialise (nums[0], 0), (nums[1], 1), ... (nums[n-1], n-1)
        for i in range(n):
            heapq.heappush(newNums, (nums[i], i))

        # pull the smallest sum tuple out
        count = 0
        resultSum = 0
        while newNums:
            count += 1
            sumThus, i = heapq.heappop(newNums)
            if left <= count and count <= right:
                resultSum += sumThus
                if count == right:
                    return resultSum % MOD
            if i + 1 < n:
                sumThus += nums[i+1]
                heapq.heappush(newNums, (sumThus, i+1))
```


