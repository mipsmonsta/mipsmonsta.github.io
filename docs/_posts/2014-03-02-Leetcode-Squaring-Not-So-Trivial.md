---
layout: post
title: Leetcode Squaring Not So Trivial
date: 2024-03-02 09:57:00 +0800
categories: python, Leetcode, Two-Pointers
---

### Trivial problem it is not

In this leetcode question 977: [Squares of a Sorted Array], the problem asked that you return a non-decreasing array of squares after squaring the input integer elements that are given as a non-decreasing array. Question is marked as easy since you could just do element-wise squaring and sorted the resultant array. Trivial.

### But the catch is the follow-on

> Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

The trivial solution's time complexity should be O(n log n) since sorting is involved. Can we really do better?

### Non-trivial O(n) thinking

The solution is based on two things, from the right end of the input array, as we go to the left, the answer of the square of the right element *may* be always larger. The *may* is not 'shall' since an element from the left side of the input array could be negative and its square could be hence larger than the said right element. The more far left the element, the more negative and hence the larger the square value. 

Hence, the solution involves iterating from right to left (going backwards so to speak), and checking whether a particular right element's square is smaller than a particular left element's square. The right and left elements are marked by two pointers whose initial positions are at index n-1 and 0 respectively, where n is the number of elements in the input array.

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        ans = [0]*n
        for i in range(n-1, -1, -1): # start from behind to fill ans array
            sl = nums[l] * nums[l] # square left pointer element
            sr = nums[r] * nums[r] # square right pointer element

            if sl > sr:
                ans[i] = sl
                l += 1
            else:
                ans[i] = sr
                r -= 1

        return ans
```

### Plot twist - Python one-liner

While theory says that the solution above is O(n), when comparing on the time for this one-liner solution, it's still slower. Will leave it as an exercise for the you to profile the code. That's how optimised [Python's Tim Sort] is. 

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])
```



[Squares of a Sorted Array]: https://leetcode.com/problems/squares-of-a-sorted-array/description/

[Python's Tim Sort]: https://en.wikipedia.org/wiki/Timsort#:~:text=Timsort%20was%20Python's%20standard%20sorting,sorting%20algorithm%20used%20in%20Rust.