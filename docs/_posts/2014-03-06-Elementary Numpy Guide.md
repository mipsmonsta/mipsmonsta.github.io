---
layout: post
title: Elementary Numpy Guide
date: 2024-03-06 11:59 +0800
categories: python, numpy, framework
---

## Everyone needs a numpy guide, especially me

### Slicing
Slicing is all about extracting contiguous segments from an array, especially a multidimensional array.  

Use `:' to select all the elements in the axis.

```python
a = np.array([[0,1,2,3],
             [4,5,6,7],
             [8,9,10,11],
             [12,13,14, 15]])

# select every row of column 2
print(a[:, 2])
# output [2, 6, 10, 14]

# select row 2
print(a[2, :])
# output [8, 9, 10, 11]
```

Use '-1' to mean last elements for range indexing.  
```python
# select all rows but skip last column
print(a[:, :-1])

```

### Create array with homogenous datatype

Know the available datatypes in creating your array.

``` 
int
float
complex
np.int8
np.int16
np.int32
np.int64
np.float16
np.float32
np.float64
```

Creation...

```python
c = np.array([1,2,3,4], dtype=np.int16)
print(c.dtype)
# output int16

```

Indicating datatype for non-homogenous array before operations.  


```python

inst = np.array(
    [[232, '@instagram'],
    [133, '@selenagomez'],
    [59, '@vistoriasecret'],
    [120, '@cristiano'],
    [111, '@beyonce'],
    [76, '@nike']]
) # inst is a non-homogenous array

superstars = inst[inst[:, 0].astype(float) > 100, 1]

```

### Broadcasting

You may have to do operations on arrays that may have different dimensions.
Broadcasting is about the right operand taking on the shape of the left array
and for element-wise operations to take place between the two arrays/operands.   

```python

# salary of employees in 2021, 2022, 2023 in ($1000)
dataAnalyst = [130, 111, 234]
projectManager = [122, 90, 71]
engineer = [120, 100, 91]
administrator = [21, 32, 45]

employees = np.array([dataAnalyst, projectManager, engineer, administrator])

# with bonus of 10% for every other year for data-scientists
employees[0, ::2] = employees[0, ::2] * 1.1
print(employees)

# only add $50k for adminstrator for 2021
employees[3, 0:1] = employees[3, 0:1] + 50
print(employees)

```

### Boonlean indexing 

We can create a True/False array from one by using conditions on the elements.
Then with that T/F array, we use it to filter and get only the elements 
that are associated with "True". This is boolean indexing. See two examples.

```python
X = np.array(
    [[42, 40, 41, 43, 44, 34], # Hong Kong
     [30, 31, 29, 29, 29, 30], # New York
     [11, 11, 12, 13, 11, 12], # Montreal
     [8, 13, 31, 11, 11, 9]]) # Berlin

cities = np.array(["Hong Kong", "New York", "Montreal", "Berlin"])
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

print(polluted)

# Multi-dimensional Boolean indexing
a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
indices = np.array([[False, True, True],
                   [False, False, False],
                   [True, True , False]])

print(a[indices])
```

### Reshaping - change the shape of an array into another

In the example below, we reshape the linear array into 7 columns. The `-1` indicates to numpy library to fill in the number of rows based on the allocated columne. Since there are 21 days, reshaped into 7 days of the week, 3 (weeks) rows will be formed. 

```python
# temperature for three weeks in a linear array for the seven days 
tmp = np.array([1,2,3,4,3,4,4,
                5,3,3,4,3,4,6,
                6,5,5,5,4,5,5])
print(tmp)

tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)
print(tmp)


```

Here we also learn about axis. This parameter indicates the direction of carrying out the operations. Below illustrate the two axes and direction for a 2D numpy array. 

```
        axis 1 ---- >
axis 0  [[1, 2, 3],
   |     [4, 5, 6],
   |    [7, 8, 9]]
   V

```

For `tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)`, it means we take the average across the column with `axis=1`

> Note that `axis=-1` refers to the last dimension in a multi-dimensional array. So it equates to `axis=1` > in a 2D numpy array.  

In the example, below we are sorting using along columns, and then sorting across rows.

```python
a = np.array([
    [7, 8, 9],
    [6, 5, 4],
    [3, 2, 1]
])

# no axes - default is axis 1 (along columns)
print(np.sort(a))

print(np.sort(a, axis=0))

```

### Argsort vs sort

In sort, we are sorting the elements and get a re-arranged array. With `np.argsort` we get an array
of indices (of the elements) as if its sorted.   


```python
a = np.array([10, 1, 2, 3], dtype="float")
print(np.sort(a))
# output: [ 1.  2.  3. 10.]


print(np.argsort(a))
# output: [ 1 2 3 0]
```
