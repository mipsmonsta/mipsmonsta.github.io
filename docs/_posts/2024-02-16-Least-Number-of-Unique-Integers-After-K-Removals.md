---
layout: post
title: Least Number of Unique Integers After K Removals (Leetcode problem 1481)
date: 2024-02-16 15:31:50 +0800
categories: python, Leetcode, dictionary, counting-sort
---

### Problem Setup

In this problem on [leetcode], we have an array of integers that could be repeating and we can remove K elements  
with the aim to achieve the smallest number of unique characters.

>Given an array of integers arr and an integer k. Find the least number of unique integers  
after removing exactly k elements.  



### Simple method - Sorting

An inituitive solution is based on *sorting*. We use a dictionary or Counter (under the collections python module)  
to count each uniquecharacters. Naturally, the keys of the dictionary represent the unique characters. Then we sort  
the frequencies in ascending order. And at each frequency, we see if k is bigger than the frequency and  
if so, we remove one unique character. If not, we know we cannot remove more unqiue characters since the following  
frequencies will be of even larger magnitude. The algorithm in Python is as follows:

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nCounter = Counter(arr)
        leftCount = len(nCounter.values()) # number of unique characters
        for value in sorted(nCounter.values()):
            if k == 0:
                break # end for-loop when no more k elements to remove
            if k >= value:
                k -= value
                leftCount -= 1 # one less unique character
            else: # value > k
                k = 0


        return leftCount
```
The time complexity due to the sorting of the freqencies of the characters will dominate and be `n log n`. Is there a linear i.e. `O(n) big-O` solution?

### Counting Sort - Frequency of frequencies

Turns out yes. We still use a dictionary or Counter to record the count each unique characters. Then we take things to the second order by counting  
the count or record the frequency of the frequencies.So if there are 3 counts of `1` and 3 counts of `2`, then frequncyCounter[3] = 2. We can  
traverse the frequency from 1 to n (why n - which is the size of the array of input integers? Because worst case is all the integer elements  
in the input array are unique) and decide how many unique character count can be removed. The latter is given by the following formula:

```python
removeCharacterCount = min(k//freq, freqencyCounter[freq])
```

The full python code for the algorithm is

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr) # frequency of characters
        n = len(arr)

        freqencyCounter = [0]*(n+1) # frequencies 1 to n
        for value in counter.values():
            freqencyCounter[value] += 1

        numberOfUniqueCharacters = len(counter)

        for freq in range(1, n+1):
            # we are working up from low frequency to high frequency
            # since low frequency means we can remove more characters
            # through removal of k elements and ensure least amount of unique
            # characters are left. K//freq is maximum characters that can be 
            # removed. Variable frequencyCounter[freq] gives is the number 
            # of characters that can be removed at that frequency.
            removeCharacterCount = min(k//freq, freqencyCounter[freq])
            numberOfUniqueCharacters -= removeCharacterCount
            k -= (freq*removeCharacterCount)

            # can stop since we cannot remove more characters
            if k < freq:
                break

        return numberOfUniqueCharacters

```

Time complexity is now **Linear**. Really learning a lot. Are you?

[leetcode]: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
