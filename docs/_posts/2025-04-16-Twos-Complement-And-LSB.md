---
layout: post
title: Two's Complement and Least Set Bit (LSB)
date: 2025-04-16 17:57 +0800
categories: foundation, python, binary
---

# A Trick to single out the Least Set Bit

## Negative of a positive number - Two's Complement

In binary numeric system, we note that to represent the negative of a number, we would
- First take the positve number in binary form; and
- Invert each bit / toggle each bit; and then
- Add one.

``` 
Example
Take 5, it's binary form is 0101.
We toggle the bits to become 1010.
Add one and the binary form becomes 1011.

``` 
'1011' is the Two's complement and that's a popular form of representing a negative number.

## What is the Least Set Bit?

In `0101`, `0001` is the Least Set Bit or sometimes the Least Significant Set Bit. Quesiton is how given `0101`, how could we easily distilled out `0001`. I.e. given a binary form, how to single out the Least Set Bit (titular).

The answer: Binary And of the number with its Two's Complement form or in more laymanised terms: `number & -number`.

> 0101
> Two's complement: 1011
> __0101 & 1011 = 0001__



