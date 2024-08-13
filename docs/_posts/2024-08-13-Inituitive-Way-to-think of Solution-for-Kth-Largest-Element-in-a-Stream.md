---
layout: post
title: Intuitive Way to think of solution for Kth Largest Element in a Stream (Leetcode problem 704)
date: 2024-08-13 08:00:00 +0800
categories: python, Leetcode, Re-Root-Technique
---

## Intiutive Way to think about Solution

Take the example of the initial stream of 4, 5, 8, 2. and to find the third largest element. If we sort the initial elements from smallest to largest, it will be

````
2 4 5 8
  ^
  |
  3rd largest
````

Another way to see it is to put an array of size 3 (same as the kth parameter) around the top 3 (k) elements.

````
2 [4 5 8] <- array of size 3
   ^
   |
   3rd largest
````

Now if we add a smaller number into the stream e.g. 1 and still sort it.

```
1 2 [4 5 8] <- array of size 3
   ^
   |
   3rd largest

```

We immediately see that if we maintained the array at size 3, the first element of the array is still the kth largest element.

If we add a bigger number, e.g. 5.

```
1 2 [4 5 5 8] <- array of size 3
   ^
   |
   3rd largest

```

This time, we sort and put the bigger number into the array in the order. The first element of the array, which is now size 4, is now wrong and is not pointing to the 3rd largest number in the stream. To point correctly, we just shrink the array back to size 3.

```
1 2 4 [5 5 8] <- array of size 3
       ^
       |
       3rd largest

```

With this understanding, you can now have an inituitive understanding of the algorithm.

1. Sort the initial stream by putting into a minheap.

2. Pop the smallest elements until the minheap has k elements. The first element in the minheap would be the kth largest element.

3. If new elements are added into minheap, push and heapify the minheap and again pop out to maintain the size of the minheap. The first element of the minheap would be the kth largest element.

```python

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [num for num in nums] # max heap
        self.k = k
        heapq.heapify(self.minHeap)
       
           
    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            # removed the smallest element

        return self.minHeap[0]
```



