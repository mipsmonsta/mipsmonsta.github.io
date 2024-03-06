import numpy as np

# slicing
a = np.array([[0,1,2,3],
             [4,5,6,7],
             [8,9,10,11],
             [12,13,14, 15]])

# select every row of column 2
print(a[:, 2])

# select row 2
print(a[2, :])

# select all rows but skip last column
print(a[:, :-1])

# broadcasting - act of converting  a low dimensional array into a higher dimensional array 
# to perform element-wise operations.

# shape is a property, not a callable
b = np.array([[2,1,2], [3,2,3], [4, 3, 4]])
print(b.shape)

# homeegnous values - setting datatype
# book
# int
# float
# complex
# np.int8
# np.int16
# np.int32
# np.int64
# np.float16
# np.float32
# np.float64
c = np.array([1,2,3,4], dtype=np.int16)
print(c.dtype)
d = np.array([2,3,4,5], dtype=np.float32)
print(d)
print(d.dtype)
d.dtype = np.int8
print(d.dtype)

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

# Conditional array search, filtering and broadcasting
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

inst = np.array(
    [[232, '@instagram'],
    [133, '@selenagomez'],
    [59, '@vistoriasecret'],
    [120, '@cristiano'],
    [111, '@beyonce'],
    [76, '@nike']]
)

superstars = inst[inst[:, 0].astype(float) > 100, 1]
print(superstars)

# reshaping

#daily stock prices
# [morning, midday, evening]
solar_x  = np.array(
    [[1, 2, 3], # today
     [2, 2, 5]] # yesterday
)

print(np.average(solar_x, axis=0))

tmp = np.array([1,2,3,4,3,4,4,
                5,3,3,4,3,4,6,
                6,5,5,5,4,5,5])
print(tmp)

tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)
print(tmp)

# np.sort

a = np.array([
    [7, 8, 9],
    [6, 5, 4],
    [3, 2, 1]
])

# no axes - default is axis 1 (along columns)
print(np.sort(a))

print(np.sort(a, axis=0))

sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])
top_3 = students[np.argsort(sat_scores)][-1:-4:-1]
print(top_3)

# argsort
a = np.array([10, 1, 2, 3], dtype="float")
print(np.sort(a))
# output: [ 1.  2.  3. 10.]


print(np.argsort(a))
# output: [ 1 2 3 0]
