#!/usr/bin/env python
# coding: utf-8


# 1. Import numpy as np and print the version number. (5 Points)

import numpy as np

print(np.__version__)



# 2. Create a 1D array of numbers from 0 to 9. 
# Desired output: #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) (10 Points)

import numpy as np
np.arange(10)



# 3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset available from Iris dataset.(20 Points)

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

import numpy as np
iris = np.genfromtxt(url, delimiter=",", dtype=None, encoding=None)

print(iris)



# 4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. Use the iris dataset available from Iris dataset.(20 Points)

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

import numpy as np
iris = np.genfromtxt(url, delimiter=",", dtype=None, encoding=None)

petal_width = iris["f3"]
first_position = np.where(petal_width > 1.0)[0] [0]

print(first_position)



# 5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10. 
# Input: np.random.seed(100) a = np.random.uniform(1,50, 20) (20 Points)

import numpy as np

np.random.seed(100)
a = np.random.uniform(1,50, 20)

a[a > 30] = 30
a[a < 10] = 10

# a = np.where(a > 30, 30, a)
# a = np.where(a < 10, 10, a)

print(a)





