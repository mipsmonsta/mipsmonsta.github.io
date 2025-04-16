---
layout: post
title: An Easy Way to track number of pairs of equal valued elements in an Array 
date: 2025-04-16 14:24 +0800
categories: foundation, python
---

# Foundation Technique: Method to find numbers of pairs of equal valued Elements

## Set-up

Suppose you have an array of numbers `[2,2,3,4,4,4,3,3]`, how many equal valued pairs are there where their indices i and j are in follows the condition of `i < j`.

We know there are are 1 pairs of `2`, 2 pairs of `3` and 2 pairs of `4`. But how to quickly find them in a linear time complexity scan?

## Fast enumeration and using a frequency counter

Let's try to keep track of the frequency count of each numbers as we encounters them.

Initally, the counter is zeros for all number elements and let's start our linear enumeration of the array.

```
current element: 2
counter[2] == 0 --------- means there is zero pair of 2s
global number of pairs == 0
add current element 2 to counter
move to next element

current element: 2
counter[2] == 1 --------- means that there is one pair of 2s
global number of pairs == 1
add current element 2 to counter
move to next element

current element: 3
counter[3] == 0 --------- means there is zero pairs of 3s
global number of pairs == 1
add current element 3 to counter
move to next element

current element: 4
counter[4] == 0 --------- means there is zero pairs of 4s
global number of pairs == 1
add current element 4 to counter
move to next element

current element: 4
counter[4] == 1 --------- means there is one pair of 4s
global number of pairs == 2
add current element 4 to counter
move to next element

current element: 4
counter[4] == 2 --------- means there are two pairs of 4s
global number of pairs == 3
add current element 4 to counter
move to next element

current element: 3
counter[3] == 1 --------- means there is one pair of 4s
global number of pairs == 4
add current element 3 to counter
move to next element

current element: 3
counter[3] == 2 --------- means there are two pairs of 3s
global number of pairs == 5
add current element 4 to counter
end of array

```
## Analysis of the enumeration - Importance of the frequency

Notice that before we add the current element into its frequency bucket/counter, the __frequency is equivalent to the number of pairs__. A python code for the numeration would be as below.

```python
n = len(numbersArray)
pairs = 0 # pairs of equal valued elements
counter = Counter() # frequency counter
for i in range(n):
    curr_num = numbersArray[i]
    pairs += counter[curr_num]
    counter[curr_num] += 1

# pairs variables hold the answer

```
You will see this idea used in Leetcode question [2537 Count of the Number of Good Subarrays].

[2537 Count of the Number of Good Subarrays]: https://leetcode.com/problems/count-the-number-of-good-subarrays/description/?envType=daily-question&envId=2025-04-16
