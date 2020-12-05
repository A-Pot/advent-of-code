#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from pandas import read_csv
import numpy as np

# Load data
dat = read_csv('input.txt', header = None).values.flatten()

# ------------ Part 1 ------------ #

# Initialize ranges
rng_row = np.arange(0,127,1)
rng_col = np.arange(0,8,1)

# Get the Seat ID for one passenger
def getSeatID(d):

    # Slice into row/col portions
    row_str = d[:7]
    col_str = d[7:]
    
    # Get rows
    r0 = rng_row.copy()
    for x in row_str:
        if x == 'B':
            r0 = r0[((len(r0)+1)//2):]
        elif x == 'F':
            r0 = r0[:(len(r0)+1)//2]
        else:
            raise Exception("Bad char '{}' in row string".format(x))
        
    r1 = rng_col.copy()
    for y in col_str:
        if y == 'R':
            r1 = r1[((len(r1)+1)//2):]
        elif y == 'L':
            r1 = r1[:(len(r1)+1)//2]
        else:
            raise Exception("Bad char '{}' in col string".format(y))
    
    return r0[0] * 8 + r1[0]

# For the answer, get all Seat IDs and take the max
allIDs = [getSeatID(d) for d in dat]
min_id, max_id = min(allIDs), max(allIDs)
print(max_id)

# ------------ Part 2 ------------ #

# Taking the set difference makes this part a 1-liner
print(set(np.arange(min_id,max_id,1)) - set(allIDs))
