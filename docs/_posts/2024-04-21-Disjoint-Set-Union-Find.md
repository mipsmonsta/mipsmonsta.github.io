---
layout: post
title: Data Structure - Disjoint Set or Union Find
date: 2024-04-21 22:57 +0800
categories: python, data structure
---

# When things belong to one set

Disjoint set is a convenient data structure in computer science to quickly associate two things together. The two things could belong to the same group, the same set or even are part of the same connected component in graphs.   

The data structure is commonly implemented with two functions: 
1. find; and 
2. union.

The `find` function is to find the parent of the item usually represented by an integer.

`Union` function is how we indicate to the structure that item i and j belongs to the same grouping.

## Python Implementation

It's easy to implement with optimisation: Path Compression.

```python
class UnionFind:
    def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.rank = [0]*size

    def find(self, i):
        if self.parent[i] != i:
            # with path compression
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
            
        def union(self, i, j):
            iParent = self.find(i)
            jParent = self.find(j)

            if iParent == jParent: # i and j are of the same set
                return # so we don't have to union one more time
                
            iRank = self.rank[iParent]

            jRank = self.rank[jParent]

            if iRank < jRank: 
                # move i under j 
                self.parent[iParent] = jParent
            elif jRank < iRank:
                # move j under i
                self.parent[jParent] = iParent
            else: # rank are the same
                self.parent[iParent] = jParent
                self.rank[jParent] += 1

```
## Usage

Instatiate the Union-Find structure with the size. Size is the number of possible groupings.

```python
n = 10 # up to 10 groups; usually number of distinct items
uf = UnionFind(n)
```

Associate two items together

```python
uf.union(i, j)
```

Check if two items are of the same group/set/connected together.

```python
def isConnected(u, v):
    ...
    return uf.find(u) == uf.find(v)

```

Now you are ready to tackle DSA questions that oft use DFS/BFS to see if two nodes are connected, and have a speed up using the Union-Find data structure.