---
layout: post
title: Elementary Numpy Guide
date: 2024-03-07 21:52 +0800
categories: python, regular expression, guide
---

### Let's start from the back

A typical guide goes from the basic to the advance. But I have rewritten this guide with the intention of reminding myself of the advance features that are seldom used. So it would be useful to start from the more advance staff to the basic so that I can refresh my learning on the obscure first. 

### Negative Lookahead Regex Pattern

Menancing title, but this regex pattern should be known as the "match only if later pattern does not match afterwards". 


Example


```python

import re

text = "this is not great."
updated_text = re.sub("not (?!good)", 'fabulously ', text) # not<space> is replaced
print(updated_text)
# output: this is fabulously great.
```

What is in the parenthesis are exact what that should not follow `not `. If indeed, then `fabulously ` is subsituted in. Also meet `re.sub` which is a function to replace out matched patterns.

### There are groups and then there are named group

What is you want to store patterns and re-use? No I don't mean `re.compile` which you will learn later. I meant re-using patterns within a pattern. 

**First** step is to define the named group with the syntax:
`(?P<name>...)` where `...` is the pattern.

**Second** step is to use the named group using the syntex:
`(?P=name)`

So back to an example:

```python
pattern = '(?P<quote>[\'"]).*(?P=quote)'
text = 'he hollered "hello"'
print(re.search(pattern, text))
# output <re.Match object; span=(12, 19), match='"hello"'>
```

In the example, and in the charater class, you are escaping the single quote `'` to distinguish against the end of the pattern.

### Character class

You use square brackets to specify an arbitrary range of characters. You can also mix and match!

```
[0-3a-c]+ matches '01110' and '01c22a' but not '445' and '00ce'. 
```

Inverse is also possible, i.e. add a symbol right after the left bracket to mean *not to match*. 

```
[^0-3a-c] will now match with '445' and '44ee'.
```

To continue...