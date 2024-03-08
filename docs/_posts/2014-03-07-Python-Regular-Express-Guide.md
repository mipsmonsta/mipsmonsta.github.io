---
layout: post
title: Python Regular Expression Guide in Reverse
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

### Function differences - match, search, findall and fullmatch

Match will only match from the beginning. So if your match to your pattern is embedded not at the beginning, `re.match` will return `None`. Fullmatch is quite similar except match will need to match from begining and end.

You can see how match works in the two examples below. First example pattern will match while the second is a dud.

```python
pattern = 'I saw Mummy'
text = 'I saw Mummy kissing Santa'
print(re.match(pattern, text))
# ouput: <re.Match object; span=(0, 11), match='I saw Mummy'>

pattern = 'saw Mummy'
text = 'I saw Mummy kissing Santa'
print(re.match(pattern, text))
# output: None

```

In contrast, if you are using `re.search`, it will find the first occurence of the pattern.

```python
pattern = 'saw Mummy'
text = 'I saw Mummy kissing Santa'
print(re.search(pattern, text))
# output: <re.Match object; span=(2, 11), match='saw Mummy'>

```

Findall as the name sakes will match all matches. But it returns the matches as list of strings and hence miss out on the span information. So you cannot say use the span to highlight or color the letters.

```python
pattern = '([^\s]+(?P<duplicate>[^\s])(?P=duplicate)[^\s]+)'
text = 'I saw Mummy kissing Santa'
print(re.findall(pattern, text))
# output: [('Mummy', 'm'), ('kissing', 's')]

```

### Reusing patterns in your bigger code base

Unlike named groups that allow reusing patterns within pattern, we want to use same pattern across our codes. We do that we `re.compile`. Just like code compilation, we can reuse.

```python

pattern = re.compile("\w{1,3}coin")
print(pattern.match('dogcoin'))
print(pattern.match('bitcoin'))
print(pattern.match('acoin'))
```

## Basics - The regex primitives

### The Dot

`.` in a pattern means match a character, including whitespaces.

### The Asterix

`*` is used in conjuction as a modifier after a character or dot or whitespace `.`. E.g. `.*` or `4*`.

```python
pattern = "number 4*0?"
text = "<number 44 is ten times less than number 440"
print(re.findall(pattern, text))
#output: ['number 44', 'number 440']

```

### Zero-or-one

`?` is used in conjuction as a modifier after a character or dot or whitespace to mean "zero or one" such character ...

But it has a *special meaning* when used as a component `*?` e.g. `.*?`, it means Python searches for a minimal number of arbitrary characters i.e. **non-greedy*. Notice how greedy pattern 2 is in example below.

```python
pattern = "<.*?>"
pattern2 = "<.*>"
html = "<a href=https://mipsmonsta.github.io>Cave of Mipsmonsta</a>"
print(re.findall(pattern, html))
# output: ['<a href=https://mipsmonsta.github.io>', '</a>']
print(re.findall(pattern2, html))
# output: ['<a href=https://mipsmonsta.github.io>Cave of Mipsmonsta</a>']
```

### Word character

`\w` matches a word character which are `[a-zA-Z_0-9]` from character class perspective.

### Digit character

`\d` matches a digit `[0-9]`.

### Whitespace characters

`\s` matches `[\t\r\n\f]`.

That's all for now. I learn the Python Regular Expression best from the book [Python One-Liners], check it out.

[Python One-Liners]: https://nostarch.com/pythononeliners