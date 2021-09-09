#!/usr/bin/env python

import math
import numpy as np
import sys

debug = lambda *args: print(*args, file=sys.stderr, flush=True)

grid = np.array([np.array([int(x) for x in list(input())]) for _ in range(9)])

class Sudoku:
    def __init__(self, grid, possible_moves=None):
        self.grid = grid
        if possible_moves is None:
            self.setup_possible_moves()
        else:
            self.possible_moves = possible_moves


    def is_valid_move(self, i, j, value):
        self.grid[i, j] = value
        ret = self.valid()
        self.grid[i, j] = 0
        return ret


    def set_square(self, i, j, value):
        self.possible_moves[i,j,:] = False
        self.grid[i,j] = value
        self.possible_moves[i,:,value-1] = False
        self.possible_moves[:,j,value-1] = False

        ibox = math.floor(i / 3) * 3
        jbox = math.floor(j / 3) * 3
        self.possible_moves[ibox:ibox+3,jbox:jbox+3,value-1] = False


    def setup_possible_moves(self):
        self.possible_moves = np.full((9, 9, 9), True)
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.set_square(i, j, self.grid[i,j])


    def copy(self):
        return Sudoku(np.copy(self.grid), np.copy(self.possible_moves))


    def complete(self):
        return not np.any(self.grid == 0)


    def do_forced_moves(self):
        changed = True

        while changed:
            changed = False
            forced_moves = np.count_nonzero(self.possible_moves, axis=2) == 1

            while np.count_nonzero(forced_moves) > 0:
                changed = True
                for move in np.transpose(np.nonero(self.possible_moves)):
                    if forced_moves[move[0],move[1]]:
                        self.set_square(move[0], move[1], move[2] + 1)

                forced_moves = np.count_nonzero(self.possible_moves, axis=2) == 1


    def valid(self):
        if np.count_nonzero(
                (self.grid == 0) & 
                (np.count_nonzero(self.possible_moves,axis=2) == 0)):
            return False

        for i in range(9):
            line = np.unique(self.grid[i,:],return_counts=True)
            if not all(line[1][0 in line[0]:] == 1):
                return False

            line = np.unique(self.grid[:,i],return_counts=True)
            if not all(line[1][0 in line[0]:] == 1):
                return False

        for i in range(3):
            for j in range(3):
                box = np.unique(
                        self.grid[i*3:3+(i*3),j*3:3+(j*3)],
                        return_counts=True
                )
                if not all(box[1][0 in box[0]:] == 1):
                    return False

        return True


def run(sudoku):
    if not sudoku.valid():
        return False

    if sudoku.complete():
        return sudoku

    for i in range(9):
        for j in range(9):
            if sudoku.grid[i,j] == 0:
                for val in range(1, 10):
                    if sudoku.possible_moves[i,j,val-1]:
                        sudoku_copy = sudoku.copy()
                        sudoku_copy.set_square(i, j, val)
                        sudoku_copy.do_forced_moves()

                        if run(sudoku_copy):
                            return sudoku_copy


sudo = Sudoku(grid)
sudo.do_forced_moves()
print('\n'.join(''.join(str(x) for x in l) for l in run(sudo).grid))


