---
layout: post
title: Count Element with Maximum Frequency (Leetcode problem 3005)
date: 2024-03-19 21:20:00 +0800
categories: python, Leetcode, dictionary
---

### Problem Ask - Maximum Frequencies

In this [leetcode] question, we are given a list of repeated number elements and asked to find the total frequencies of elements that all have the maximum frequency.

### Insights for breakthrough

The question is categorise as an easy one. But it's harder if you say that you have to reach the solution in a linear one-pass. In the one pass solution, you can use a `freq` dictionary, a `maxFreq` int variable and `totalFreq` variable. At your traverse each of element, you update the frequency of the element and asked if the element's frequency is higher than `maxFreq`. If so, you update `maxFreq` to the element's frequency. And also set `totalFreq` to the `maxFreq`. At this point, `maxFreq` represents the maximum frequency first encountered thus far. 

The next element may be of two cases. First case is that it is having the same frequency as the `maxFreq`. If so, you add the frequency of this element to `totalFreq`. Second case is that next element's frequency exceeds the `maxFreq`. For this your fall back to update `maxFreq` with the algorithm in the preceding paragraph.

### Code to tell all

See the simple Python Code. The O(n) solution is fast and can be used also to solve [Leetcode qn 621] Task Scheduler. A good explanation of Task Scheduler can be found at [Satyendra Mishra's post].

```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0
        totalFreq = 0
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if freq[num] > maxFreq:
                maxFreq = freq[num]
                totalFreq = freq[num] # new max freqency encountered
            elif freq[num] == maxFreq:
                totalFreq += freq[num]
            

        return totalFreq

```


[Leetcode]: https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
[Leetcode qn 621]: https://leetcode.com/problems/task-scheduler/description/
[Satyendra Mishra's post]: https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440