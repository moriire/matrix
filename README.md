# matrix
### _Light weight Python package for solving matrix/vector_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://www.facebook.com/AgesXpat)
## Overview
Python alternative to numpy package.

### _Converts from:_   
- Light weight 
- fast
- Limited to simple matrix/vector operations.

## Requirements
Python 3.x+

## Installation

```sh
pip install matrix
```

#### Sample Code

Basic usage:

```sh
>>> from matrix import Matrix
>>> row_1 = [i for i in range(3)]
>>> row_2 = [i for i in range(3, 6)]
>>> row_3 = [i for i in range(6, 9)]
>>> matrix = Matrix(row_1, row_2, row_3)
>>> print(matrix)
```
>>> Matrix([[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])

```sh
print(matrix.size())
```

>>> (3, 3)

## License
MIT
