---
layout: post
title: Sieve of Eratosthenes
date: 2024-03-04 12:31:50 +0800
categories: python, algorithm
---

### What is a Prime Number?

In number theory, primer numbers are integers that can only be divided with remaineders by 1 and itself. That means if `n` is a prime number, only 1 and `n` are the factors. There is no number smaller `i` than `n` that is a factor or conversely no multiples of `i` that is equal to `n`.

> For a prime number n, there is no number smaller `i` (than `n`) whose multiples are equal to `n`.

### Ancient Algorithm to find prime numbers

*Sieve of Erathosthenes* is was invented to efficiently find prime numbers from 2 to m, where m is a number you defined as the upper limit. You start off with an array from 2 to m and initially, all numbers in the array are prime candidates. The algorithm then works to 'rule'/'sieve' out candidates that cannot be prime.  

These are the steps of the algorithm:  

1. Start with number 2 in the array and step up unitl you find a prime number `x`. You know that `x` is a prime number if it's not 'sieved' out because of the fact that x being present means that there is no smaller number than `x` that is a divisor of `x`.

2. Sieve out all multiples s of `x` because they are not prime: `x` is a divisor or factor of alll these mutiples.

3. In step 2, only start sieving out mutiples from number `x` x `x` onwards as an optimisation. All numbers between `2x` and `x` x `x` were aleady sieved out.

### Example for visualising - 2 to 100

Initially 2 to 100 are in the table.   

Starting with 2, it is a prime number by definition. There are no number smaller than 2 in the sieve that is a factor (note that 1 is already not include in the sieve).

|  ~~1~~ |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |
| --- | ---  | ---  |  ---  |  --- | ---  | ---  | ---  | ---  | --- |
| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
| 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |
| 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
| 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |
| 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |
| 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 |

Sieve out all multiples of 2. Staring with `2 x 2`.

|  ~~1~~ |  2 |  3 |  ~~4~~ |  5 |  ~~6~~ |  7 |  ~~8~~ |  9 | ~~10~~ |
| --- | ---  | ---  |  ---  |  --- | ---  | ---  | ---  | ---  | --- |
| 11 | ~~12~~ | 13 | ~~14~~ | 15 | ~~16~~ | 17 | ~~18~~ | 19 | ~~20~~ |
| 21 | ~~22~~ | 23 | ~~24~~ | 25 | ~~26~~ | 27 | ~~28~~ | 29 | ~~30~~ |
| 31 | ~~32~~ | 33 | ~~34~~ | 35 | ~~36~~ | 37 | ~~38~~ | 39 | ~~40~~ |
| 41 | ~~42~~ | 43 | ~~44~~ | 45 | ~~46~~ | 47 | ~~48~~ | 49 | ~~50~~ |
| 51 | ~~52~~ | 53 | ~~54~~ | 55 | ~~56~~ | 57 | ~~58~~ | 59 | ~~60~~ |
| 61 | ~~62~~ | 63 | ~~64~~ | 65 | ~~66~~ | 67 | ~~68~~ | 69 | ~~70~~ |
| 71 | ~~72~~ | 73 | ~~74~~ | 75 | ~~76~~ | 77 | ~~78~~ | 79 | ~~80~~ |
| 81 | ~~82~~ | 83 | ~~84~~ | 85 | ~~86~~ | 87 | ~~88~~ | 89 | ~~90~~ |
| 91 | ~~92~~ | 93 | ~~94~~ | 95 | ~~96~~ | 97 | ~~98~~ | 99 | ~~100~~ |

Next, 3 is a prime number, since it's not sieved out. Sieve out multiples of `3` from `3 x 3` onwards.

|  ~~1~~ |  2 |  3 |  ~~4~~ |  5 |  ~~6~~ |  7 |  ~~8~~ | ~~9~~ | ~~10~~ |
| --- | ---  | ---  |  ---  |  --- | ---  | ---  | ---  | ---  | --- |
| 11 | ~~12~~ | 13 | ~~14~~ | ~~15~~ | ~~16~~ | 17 | ~~18~~ | 19 | ~~20~~ |
| ~~21~~ | ~~22~~ | 23 | ~~24~~ | 25 | ~~26~~ | ~~27~~ | ~~28~~ | 29 | ~~30~~ |
| 31 | ~~32~~ | ~~33~~ | ~~34~~ | 35 | ~~36~~ | 37 | ~~38~~ | ~~39~~ | ~~40~~ |
| 41 | ~~42~~ | 43 | ~~44~~ | ~~45~~ | ~~46~~ | 47 | ~~48~~ | 49 | ~~50~~ |
| ~~51~~ | ~~52~~ | 53 | ~~54~~ | 55 | ~~56~~ | ~~57~~ | ~~58~~ | 59 | ~~60~~ |
| 61 | ~~62~~ | ~~63~~ | ~~64~~ | 65 | ~~66~~ | 67 | ~~68~~ | ~~69~~ | ~~70~~ |
| 71 | ~~72~~ | 73 | ~~74~~ | ~~75~~ | ~~76~~ | 77 | ~~78~~ | 79 | ~~80~~ |
| ~~81~~ | ~~82~~ | 83 | ~~84~~ | 85 | ~~86~~ | ~~87~~ | ~~88~~ | 89 | ~~90~~ |
| 91 | ~~92~~ | ~~93~~ | ~~94~~ | 95 | ~~96~~ | 97 | ~~98~~ | ~~99~~ | ~~100~~ |


Next, 5 is a prime number, since it's not sieved out. Sieve out multiples of `5` from `5 x 5` onwards.

|  ~~1~~ |  2 |  3 |  ~~4~~ |  5 |  ~~6~~ |  7 |  ~~8~~ | ~~9~~ | ~~10~~ |
| --- | ---  | ---  |  ---  |  --- | ---  | ---  | ---  | ---  | --- |
| 11 | ~~12~~ | 13 | ~~14~~ | ~~15~~ | ~~16~~ | 17 | ~~18~~ | 19 | ~~20~~ |
| ~~21~~ | ~~22~~ | 23 | ~~24~~ | ~~25~~ | ~~26~~ | ~~27~~ | ~~28~~ | 29 | ~~30~~ |
| 31 | ~~32~~ | ~~33~~ | ~~34~~ | ~~35~~ | ~~36~~ | 37 | ~~38~~ | ~~39~~ | ~~40~~ |
| 41 | ~~42~~ | 43 | ~~44~~ | ~~45~~ | ~~46~~ | 47 | ~~48~~ | 49 | ~~50~~ |
| ~~51~~ | ~~52~~ | 53 | ~~54~~ | ~~55~~ | ~~56~~ | ~~57~~ | ~~58~~ | 59 | ~~60~~ |
| 61 | ~~62~~ | ~~63~~ | ~~64~~ | ~~65~~ | ~~66~~ | 67 | ~~68~~ | ~~69~~ | ~~70~~ |
| 71 | ~~72~~ | 73 | ~~74~~ | ~~75~~ | ~~76~~ | 77 | ~~78~~ | 79 | ~~80~~ |
| ~~81~~ | ~~82~~ | 83 | ~~84~~ | ~~85~~ | ~~86~~ | ~~87~~ | ~~88~~ | 89 | ~~90~~ |
| 91 | ~~92~~ | ~~93~~ | ~~94~~ | ~~95~~ | ~~96~~ | 97 | ~~98~~ | ~~99~~ | ~~100~~ |

Next, 7 is a prime number, since it's not sieved out. Sieve out multiples of `7` from `7 x 7` onwards.

|  ~~1~~ |  2 |  3 |  ~~4~~ |  5 |  ~~6~~ |  7 |  ~~8~~ | ~~9~~ | ~~10~~ |
| --- | ---  | ---  |  ---  |  --- | ---  | ---  | ---  | ---  | --- |
| 11 | ~~12~~ | 13 | ~~14~~ | ~~15~~ | ~~16~~ | 17 | ~~18~~ | 19 | ~~20~~ |
| ~~21~~ | ~~22~~ | 23 | ~~24~~ | ~~25~~ | ~~26~~ | ~~27~~ | ~~28~~ | 29 | ~~30~~ |
| 31 | ~~32~~ | ~~33~~ | ~~34~~ | ~~35~~ | ~~36~~ | 37 | ~~38~~ | ~~39~~ | ~~40~~ |
| 41 | ~~42~~ | 43 | ~~44~~ | ~~45~~ | ~~46~~ | 47 | ~~48~~ | ~~49~~ | ~~50~~ |
| ~~51~~ | ~~52~~ | 53 | ~~54~~ | ~~55~~ | ~~56~~ | ~~57~~ | ~~58~~ | 59 | ~~60~~ |
| 61 | ~~62~~ | ~~63~~ | ~~64~~ | ~~65~~ | ~~66~~ | 67 | ~~68~~ | ~~69~~ | ~~70~~ |
| 71 | ~~72~~ | 73 | ~~74~~ | ~~75~~ | ~~76~~ | ~~77~~ | ~~78~~ | 79 | ~~80~~ |
| ~~81~~ | ~~82~~ | 83 | ~~84~~ | ~~85~~ | ~~86~~ | ~~87~~ | ~~88~~ | 89 | ~~90~~ |
| ~~91~~ | ~~92~~ | ~~93~~ | ~~94~~ | ~~95~~ | ~~96~~ | 97 | ~~98~~ | ~~99~~ | ~~100~~ |

Next, 11 is a prime number, since it's not sieved out. Sieve out multiples of `11` from `11 x 11` onwards. *But* `121` already exceeds `m = 100`. So we stopped.

The prime number from 2 to 100 are (sieved number removed for ease of reference):

|  |  2 |  3 |   |  5 |   |  7 |  |  |  |
| --- | ---  | ---  |  ---  |  --- | ---  | ---  | ---  | ---  | --- |
| 11 | | 13 | | |  | 17 |  | 19 |  |
| | | 23 | | | | | | 29 | |
| 31 |  | | | | | 37 | | | |
| 41 | | 43 | | | | 47 | | |  |
| | | 53 | | | | | | 59 | |
| 61 | | | | | | 67 | | | |
| 71 | | 73 | | | | | | 79 | |
| | | 83 | | | | | | 89 | |
| |  | | | | | 97 | | | |


### Python Code Implementation

Now for some code demonstration of the algorithm.

```python

class Solution():
    def primeNumbersUpTo(self, n): # inclusive of n
        primeCandidates = set([i for i in range(2, n+1)])

        for i in range(2, n+1):

            # i is not prime
            if i not in primeCandidates:
                continue

            for multiple in range(i*i, n+1, i):
                if multiple in primeCandidates:
                    # sieved out
                    primeCandidates.remove(multiple)
        
        return list(primeCandidates)

```