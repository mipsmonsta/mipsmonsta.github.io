---
layout: post
title: Basic Linked List Operations to Know
date: 2024-03-23 13:58:00 +0800
categories: python, Leetcode, linkedlist
---

## Introduction

To effectively solve Linked List related questions on Leetcode, you need to know basic operations on a Linked List. With practise, you will become proficent. But reading this post will help to provide you the knowledge. You could use try what you learn in questions such as [Palindrome Linked List] and [Reorder List].


### How do you reverse nodes of a Linked List?
Given a Linked List made of `ListNode` (structure below) and the the head node, how do you easily reverse the nodes of the list?

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```


The preamble is that you need to do it fast with one-pass. 


### Idea - Start off with a `None` node as a Previous Node

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

Traverse node by node. For each node, remember the next node pointed by the `next` pointer. Then set the `next` pointer of the current node to the `previous` node which is `None` at first. After which, set the `previous` node to point to the current node. At the end of the traversal of all the nodes, the `previous` node would become the new head node.

### How do you find the mid node of a Linked List?

Pre-requisite of the input Linked List is there there are at least two nodes or more in the list. If so you use two variables to point to the nodes as they are iterated - `fast` and `slow` pointers. How it works is that for every iteration, you advance `fast` pointer twice as fast by iterating to next pointer and then the next of the next pointer.

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

