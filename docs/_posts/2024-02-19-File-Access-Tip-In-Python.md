---
layout: post
title: File Access Tip in Python
date: 2024-02-19 06:14:30 +0800
categories: python, 
---

### Using OS.Path and __File__

I have a project with the file structures below:

```
examples
    |_ estats.py
lib
    |_ waveshare_epd
        |_ utility.py
config.json

```

From the module `utility.py`, I have codes that will access the json configuration file in the base directory. So how would you do so? Turns out it's a bit tricky if you are uninitiated.

First, let's understand the dunder (double underscore) constant __file__. It can be used to access the current directory containing `utility.py`. Do so by
```python
PATHDIR = os.path.dirname(os.path.realpath(__file__))
```
## Accessing other file

With the directory, we can access the configuration file that is two parent folders up by

```python
CONFIG_FILE_NAME = config.json
filePath = os.path.join(PATHDIR, "../../",CONFIG_FILE_NAME)
```

The resolving up the parent folers are given by `../../` pattern. 

Hence, when we have complicated file structures and we need to navigate our way around, that's where some os module code, `__File__` and our good old DOS/Bash directory patterns will help.
