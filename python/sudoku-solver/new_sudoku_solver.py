#!/usr/bin/env python

import math
from typing import List, overload
import numpy as np
import sys


class DLLNode(object):
    def __init__(self, left = None, right = None,
                 above = None, below = None,
                 header = None, row = None):
        self.left:   DLLNode = left
        self.right:  DLLNode = right
        self.above:  DLLNode = above
        self.below:  DLLNode = below
        self.header: Header  = header
        self.row:    Row     = row

    def remove_self(self):
        self.left.right = self.right
        self.right.left = self.left
        self.above.below = self.below
        self.below.above = self.above

    
    def reinsert_self(self):
        self.left.right = self
        self.right.left = self
        self.above.below = self
        self.below.above = self
    


class DLLList(List):
    def __init__(self):
        return super(DLLList, self).__init__()

    
    def __add__(self, item: DLLNode):
        return super(DLLList, self).__add__(item)


    def __getitem__(self, key) -> DLLNode:
        return super(DLLList, self).__getitem__(key)


class Header(DLLList):
    def __init__(self, row, col, value):
        super(Header, self).__init__()
        self.row:   int = row
        self.col:   int = col
        self.value: int = value
        

class Row(DLLList):
    def __init__(self, row, col, value):
        super(Header, self).__init__()
        self.row:   int = row
        self.col:   int = col
        self.value: int = value
        

U = [1, 2, 3, 4, 5, 6, 7]

A = [1, 4, 7]
B = [1, 4]
C = [4, 5, 7]
D = [3, 5, 6]
E = [2, 3, 6, 7]
F = [2, 7]

S = [A, B, C, D, E, F]

matrix = np.full((len(S), len(U)), 0)

for i in range(len(S)):
    current = S[i]
    for elem in current:
        matrix[i, U.index(elem)] = 1

print(matrix)
