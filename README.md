# matrix
### _Light weight Python package for solving matrix/vector_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://www.facebook.com/AgesXpat)
## Overview
Python alternative to numpy package.

### _Features:_   
- Light weight 
- fast
- Limited to simple matrix/vector operations.

## Requirements
Python 3+

## Installation

```sh
pip install matrix
```
#### Sample Code
Basic usage:

```sh
>>> import matrix
>>> row_1 = [i for i in range(3)]
>>> row_2 = [i for i in range(3, 6)]
>>> row_3 = [i for i in range(6, 9)]
>>> mat = Matrix(row_1, row_2, row_3)
```
OR
```sh

>>> matrix = matrix.Matrix(([0, 1, 2], [3, 4, 5], [6, 7, 8]))
```
Result
```sh
>>> print(mat)
```
>>> Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

```sh
>>> print(mat.size())

>>> (3, 3)
```
[wikipedia](https://en.wikipedia.org/wiki/Matrix_(mathematics)#Size)
## Operation
#### Matrix Addition
```sh
>>> add_matrices = matrix + matrix
>>> print(add_matrices)
```
>>> Matrix([[0, 2, 4], [6, 8, 10], [12, 14, 16]])

#### Subtraction
```sh
>>> sub_matrices = mat - mat
>>> print(sub_matices)
```
>>> Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

#### Multiplication (element-wise)
```sh
>>> mul_matrices = mat * mat
>>> print(mul_matices)
```
>>> Matrix([[0, 1, 4], [9, 16, 25], [36, 49, 64]])

#### Ones
```sh
>>> ones = matrix.ones(3)
>>> print(ones)
```
>>> Matrix(([1, 1, 1], [1, 1, 1], [1, 1, 1]))

#### Zeros
```sh
>>> ones = matrix.zeros(3)
>>> print(zeros)
```
>>> Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

#### Cofactors
```sh
>>> cof = mat.cofactors()
>>> print(tuple(cof))
```
>>> (0, 1, -2)

#### Dot Product
```sh
>>> dot = mat.dot([0, 1, 2], [3, 4, 5], [2, 4, 6])
>>> print(dot)
```
>>> [0, 3, 4]
## Links
[wikipedia](https://en.wikipedia.org/wiki/Matrix_(mathematics))

## License
MIT
