#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from pandas import read_csv
from numpy import prod

# Load data
dat = read_csv('/Users/apot/projects/AdventOfCode/2020/day_3/input.txt', header = None).values.flatten()

# ------------ Part 1 ------------ #

# Given a configuration, traverse the repeating hill and count trees along the way
def treeCounter(over_right, over_down, puzzle_length = len(dat[0])):
    tree_count, current_row, idx = 0,0,0
    for row in dat:
        current_row += 1
        if current_row % over_down != 0:
            continue
        tree_count += (row[idx] == "#")
        idx = (idx + over_right) % puzzle_length
    return tree_count

# Slope traversal for (Right 3, Down 1)
print(treeCounter(3,1))

# ------------ Part 2 ------------ #

# Product of various slope traversals
print(
      prod([
          treeCounter(1,1),
          treeCounter(3,1),
          treeCounter(5,1),
          treeCounter(7,1),
          treeCounter(1,2)
          ])
      )
