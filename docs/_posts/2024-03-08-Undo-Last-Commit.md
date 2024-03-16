---
layout: post
title: Git Undo Last Commit
date: 2024-03-08 09:56 +0800
categories: git
---

### In trouble with Git 

Often, I forget to pull in commits from the remote respository and went ahead to commit my local work. Then when pulling in, you will have conflicts.

To solve you can undo the last commit. There are two types though.

The type where you get to keep your local work, these will appear in the staging as uncommitted.   

```
git reset --soft HEAD~1
```

And the hard type: where you lose your local work that was last commited.

```
git reset --hard HEAD~1
```

Now you can pull your remote commits before creating a new local commit. And the sky will be blue again.

