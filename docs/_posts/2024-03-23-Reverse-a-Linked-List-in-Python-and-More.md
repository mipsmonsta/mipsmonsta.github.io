---
layout: post
title: Basic Linked List Operations to Know
date: 2024-03-23 13:58:00 +0800
categories: python, Leetcode, linkedlist
---

## Introduction

To effectively solved Linked List related questions on Leetcode, you need to know basic operations on a Linked List. With practise and learning this post, you will become proficent. 

### How do you reverse nodes of a Linked List?
Given a Linked List made of `ListNode` (structure below) in the form of the head node, how do you easily reverse the nodes of the list?

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```


You need to do it fast with one-pass. This requirement would be a essential and basic skill you need to have to solve LinkedList questions on leetcode. Example: you could use it in [Palindrome Linked List], 



### Idea - Have None/Empty Node that is the prev node to point to from the current node

```python
prevNode = None
curr = head
        
while curr:
    nextNode = curr.next # remember original next node as this will be repointed in next line
    curr.next = prevNode # reverse (next) arrow to point to prevNode
    prevNode = curr # curr node becomes prevNode to prepare for next iteration
    curr = nextNode
head = prevNode # the head of the reversed list2
```

Traverse node by node. For each node, remember the next node. Then set the next pointer of the current node to the previous node which is None at first. Then in set the previous node to point to the current node. At the end of the reversal of all the nodes, previous node would become the new head node.

### How do you find the mid node of a Linked List?

Pre-requisite is there there are at least two nodes or more in the Linked List. If so you use two variables to hold the nodes as they are iterated - `fast` and `slow` pointers. How it works is that for every iteration, you advance `fast` pointer twice as fast by iterating to next pointer and then the next of the next pointer.

See the python code and digests it:

```python
midNode = None

fast = head
slow = head
while fast:
    fast = fast.next
    slow = slow.next
    if fast:
        fast = fast.next #2x
        
midNode = slow # mid of linked list and head
```

[Palindrome Linked List]: https://leetcode.com/problems/palindrome-linked-list/description/

[Reorder List]: https://leetcode.com/problems/reorder-list/description/

