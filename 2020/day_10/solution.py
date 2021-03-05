#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pandas as pd
from collections import Counter
from numpy import prod

# Load and prepare data
fo = open('input.txt', 'r')
line = fo.readlines()
line = sorted([int(x.strip()) for x in line])

# Append the device as the last entry
line.append(max(line) + 3)

# ------------ Part 1 ------------ #

# Take diff of vector with its shifted self to get consecutive adapter differences
diffs = pd.Series(line) - pd.Series(line).shift(1).fillna(0)

# Multiply the counts together for the answer
print(prod(list(Counter(diffs).values())))

# ------------ Part 2 ------------ #

# Add the starting position to the line
line.insert(0,0)

# Since the recursion ends up producing repetitive paths, we'll employ a memoization technique
# i.e. If we've computed countPaths(x) already, then we can recall it rather than recompute it
segmentMemo = {}

# Given a joltage value (cursor), check the number of adaptor choices within its vicinity
indices = list(range(line[-1]+1))
def countPaths(cursor):

    # Check for memo - if we've seen this before, then return immediately
    if segmentMemo.get(cursor) is not None:
        return segmentMemo[cursor]
                    
    # If the end has been reached, then return 1
    if cursor + 3 == max(line):
        return 1
    
    # Else recurse over possible adaptors
    else:
        # Cast a 3-window net ahead of the current joltage and calculate possibilities for that window
        idx = indices[(cursor+1):(cursor+4)]
        val = sum([countPaths(x) for x in idx if x in line])
        
        # Note value at this cursor value for future computations and return
        segmentMemo[cursor] = val
        return val

# The answer is the number of possibilities starting at 0
print(countPaths(0))
