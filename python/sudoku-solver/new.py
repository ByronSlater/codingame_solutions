import math
from typing import List, overload
import numpy as np
import sys

U = [1, 2, 3, 4, 5, 6, 7]

rows = np.full((6, 1), 'A')
for i in range(len('ABCDEF')):
    rows[i] = 'ABCDEF'[i]

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


class State:
    def __init__(self, header=None, rows=None, grid=None, chosen_rows = []):
        self.header:      np.ndarray = header
        self.rows:        np.ndarray = rows
        self.grid:        np.ndarray = grid
        self.chosen_rows: List[str]  = chosen_rows 


    def copy(self):
        return State(np.copy(self.header), 
                     np.copy(self.rows), 
                     np.copy(self.grid))

    
    def choose_row(self, idx):
        self.chosen_rows.append(self.grid[idx])
        rows_to_delete = np.nonzero(np.any(np.logical_and(matrix[idx], matrix), axis=1))[0]
        headers_to_delete = np.nonzero(self.grid[idx])
        
        self.grid = np.delete(self.grid, rows_to_delete, 0)
        self.rows = np.delete(self.rows, rows_to_delete)

        self.grid = np.delete(self.grid, headers_to_delete, 1)
        self.header = np.delete(self.header, headers_to_delete)

    def __str__(self):
        if np.size(self.grid) == 0:
            return np.array([]).__str__()


        top_row = np.resize(np.append('', self.header), (1, np.size(self.header) + 1))
        bottom_rows = np.append(self.rows, self.grid, axis=1)

        return np.append(top_row, bottom_rows, axis=0).__str__()


s1 = State(U, rows, matrix, [])

print(s1)

s1.choose_row(2)

print(s1)