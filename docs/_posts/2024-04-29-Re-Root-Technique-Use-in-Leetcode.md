---
layout: post
title: Re-Root Technique and its use (Leetcode problem 834)
date: 2024-04-29 08:00:00 +0800
categories: python, Leetcode, Re-Root-Technique
---

## Problem 834 and its ask

In problem [Sum of Distances in Tree], a un-directed graph is given. As there are only one bi-directional edge between each pair of nodes, the graph is also a tree. 

There are a total of n nodes in the graph. We are asked to find out for each node, if it is the root node, to compute and store the sum of the distances to each of the child nodes. The output of the question is hence a result of n elements in an array.

A brute force approach could be the really iterate to each of the n nodes and do a DFS to find out the sum of distances to each of the child nodes. The  DFS function would look like below. Since the dfs for each node would take O(n) time complexity, if we do so for each nodes of n (using the for loop no less), the total time complexity to solve this problem would be a good O(n^2) time complexity. I am sure that when you run the submission, the problem will be TLE i.e. Time Limit Exceeded. 

```python
ans = [0] * n # store the sum of distances if root is rooted at i
visited = set()

def dfs(currNode, pathLength: int):
    nonlocal ans, i
    ans[i] += pathLength
    visited.add(currNode)

    for nextNode in graph[currNode]:
        if nextNode not in visited:
            dfs(nextNode, pathLength + 1)

for i in range(n):
    dfs(i, 0)

```

## Is there a better way for time complexity - Re-Rooting to the rescue

Given the graph below. If the original root is at node 0, re-root means to move the nodes to its adjacent child node.  

![Re root in action](/assets/images/Leetcode_834.jpg)

In the diagram, what you see is the orginal root at node 0. For this root, the sum of distances would be 1 length to node 2, 1 length to node 3, 2 length to node 4, 2 length to node 5 and 2 length to node 6, which equates to 8. Can we make use of the computed `base` answer of 8 and the current root to compute if node 1 is now the root? Thus, we need a concept of the `Re-rooting technique`.

From the graph above, we re-root from the first node 0 to its adjacent node 1. Once done, the re-rooted node (node 1) and its sub-tree in blue will be part of the `closer nodes`. What are they? These are the nodes that will decrease in path length by 1. If all things being equal, then there must be nodes that are further in length by 1. These `further nodes` are the original node and the red highlighted sub-tree nodes. Note that the numbers of `further nodes` can be counted from the `closer nodes`. In fact, the formulae is:

> count of further nodes = n - count of closer nodes

The sum of distances for the re-root node 1 would be given by

> base answer - numbers of `closer nodes` + numbers of `further nodes`.

## Python Code and Time Complexity

The problem can be solved with three DFSes, i.e.:
1. DFS to find the base (sum of distances) for nodes 0.
2. DFS to find the number of `closer nodes` for each of the nodes if each node is the new-root (i.e. re-rooted from adjacent parent node).
3. DFS to compute the sum of distances for each nodes if each node is the new-root.

Since each DFS takes O(n) time complexity. The overall time complexity would still be O(n).

```python
# Approach: Use 3 DFS that is more easily explainable. Still O(n) time complexity.
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # whole idea of Re-Root
        # base_distance - closer_nodes + further_nodes
        # futher_nodes = N - closer_nodes where N is number of nodes in tree 

        # build un-directed graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        ans = [0] * n # store the sum of distances if root is rooted at i
        visited = set()
        # helper to find ans[0] i.e. sum of distances if root is rooted at 0
        def dfs(currNode, pathLength: int):
            nonlocal ans
            ans[0] += pathLength
            visited.add(currNode)

            for nextNode in graph[currNode]:
                if nextNode not in visited:
                    dfs(nextNode, pathLength + 1)

        # fill up ans[0] which is the base
        dfs(0, 0)

        closer_nodes_count = [0]*n # number of closer nodes if root is rooted at i
        visited = set()
        # helper to find out numnber of closer nodes if rooted at currNode
        def dfsCloserRooted(currNode):
            nonlocal closer_nodes_count, visited
            closerNodes = 1 # currNode is its own closerNodes

            visited.add(currNode)

            for nextNode in graph[currNode]:
                if nextNode not in visited:
                    closerNodes += dfsCloserRooted(nextNode)
            
            closer_nodes_count[currNode] = closerNodes

            return closerNodes

        # find closerNodes for each root 
        dfsCloserRooted(0)

        visited = set()
        # helper to compute the ans[i] using re-root formula
        # base - closer_nodes_count + (n - closer_nodes_count)
        def dfsReRoot(currNode):
            nonlocal ans, closer_nodes_count

            visited.add(currNode)

            for nextNode in graph[currNode]:
                if nextNode not in visited:
                    ans[nextNode] = ans[currNode] - closer_nodes_count[nextNode] + \
                        (n - closer_nodes_count[nextNode])
                    dfsReRoot(nextNode)
        
        dfsReRoot(0)

        return ans

```

The timing ranking is merely 30%. We can improve this by combining DFS 1 and 2. See the optimised codes. I personally prefer the former code as it's easier to think through.

```python
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # whole idea of Re-Root
        # base_distance - closer_nodes + further_nodes
        # futher_nodes = N - closer_nodes where N is number of nodes in tree 

        # build un-directed graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        visited = set()
        closer_nodes_count = [0]*n
        ans = [0]*n # store sums of path distances if root is at node i

        # helper function to count closer_nodes for each node if it is re-rooted at each node
        # and also to compute the base that is orginally at ans[0]
        def dfs(currNode) -> int:
            nonlocal visited, closer_nodes_count, ans

            # curreNode count as one closer node
            closer_nodes = 1
            
            visited.add(currNode)

            for childNode in graph[currNode]:
                if childNode in visited:
                    continue
                child_closer_nodes = dfs(childNode)
                closer_nodes += child_closer_nodes
                ans[0] += child_closer_nodes
            
            closer_nodes_count[currNode] = closer_nodes

            return closer_nodes     

        dfs(0) 

        visited = set()
        # helper function to re-root from parent node to child node and to 
        # compute the re-rooted sum of distances
        # using base - closer_nodes_count + (n - closer_nodes_count)
        def dfsReRoot(currNode):
            nonlocal ans, visited
            visited.add(currNode)

            for childNode in graph[currNode]:
                if childNode in visited:
                    continue
                ans[childNode] = ans[currNode] - closer_nodes_count[childNode] + (n - closer_nodes_count[childNode])
                dfsReRoot(childNode)

        dfsReRoot(0)

        return ans
```

Now you are acquinted with the Re-Rooting Technique. Keep coding and have fun. 

[Sum of Distances in Tree]: https://leetcode.com/problems/sum-of-distances-in-tree/description/