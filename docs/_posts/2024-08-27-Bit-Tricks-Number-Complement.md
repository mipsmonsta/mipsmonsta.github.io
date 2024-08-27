---
layout: post
title: Finding the Number Complement (Leetcode 476)
date: 2024-08-27 08:18:00 +0800
categories: leetcode, python
---

# Bit trick to Quickly Find Number Complement

Given a number, as a programmer we are asked to come up with an efficient manner to find the number's complement.

A number's complement is defined as the *flipping* of all the 0's to 1's and vice versa in its binary representation.

## Two ideas to use

Both ideas made use of the toggle property of modulus 1. 

```
0 ^ 1 == 1
Zero is toggled to become 1
```

```
1 ^ 1 == 0
One is toggled to become 0
```

Armed with the power of how to toggle the bits, the first idea is to toggle all the bits of the number with 1's simulataneously.

The other is to do so bit by bit. 

For the former, the python code is as below.

```python
class Solution:
    def findComplement(self, num: int) -> int:
        length = len(f"{num:b}")
        toggleNum = (1 << (length)) - 1
        convert = toggleNum ^ num
        return convert
```

The downside of this solution is the need to find the length of the number in its binary representation.

Let's look at the *bit-by-bit* way.

```python
class Solution:
    def findComplement(self, num: int) -> int:
        b = 1
        # note that num by the constraints
        # set the problem cannot be 0
        a = num
        while num >= b: # b will be left shifted until it's larger than 
                        # num
            a ^= b # post shift, we mod a with a to toggle the bit
            b <<= 1
        
        return a
```

Not surprisingly, the method is much faster. 

