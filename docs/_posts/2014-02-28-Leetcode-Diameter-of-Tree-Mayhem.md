---
layout: post
title: Diameter of a Tree Mayhem (Leetcode problem 543)
date: 2024-02-28 15:57:00 +0800
categories: python, Leetcode, Binary tree traversal
---

### Problem Ask - Diameter of a Binary Tree

In this [leetcode] question, we are asked to find the diameter of a binary tree, given the root node.
The definition of diameter is the longest chain of nodes, not neccesarily passing through the root, in terms of the count of edges for such a chain. This is marked as an easy question, but it's clearly not so simple.

### Insights for breakthrough

The key insight is to recognise that at a particular node, we need to know the height of the left sub-tree and the height of the right sub-tree. The node being the parent node will link up and form the chain of edges and the sum of the height of the left and right sub-trees *give* the number of edges (See code segment A).

<img src="/assets/images/height_tree.jpg" width=200/>

Another insight needed is that for the same particular parent node, if the edges are not the longest, the node with the right sub-tree or node with the left sub-tree will form prt of the chain for the parent of the parent node. (See code segment B)

### Code to tell all

Like most binary tree questions we use DFS but modify the DFS function to record the longest chain of edges when processing a particular node. Code shows what I mean.

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        def longest(node)->int:
            nonlocal diameter
            if node.left == None and node.right == None:
                return 1
            
            leftResult, rightResult = 0, 0
            if node.left:
                leftResult = longest(node.left)
            
            if node.right:
                rightResult = longest(node.right)
            diameter = max(diameter, leftResult + rightResult) # code segment A
            return 1 + max(leftResult, rightResult) # code segment B
        
        longest(root)
        return diameter

```


[Leetcode]: https://leetcode.com/problems/diameter-of-binary-tree/