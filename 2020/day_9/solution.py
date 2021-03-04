#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
from itertools import combinations

# Load and format data
fo = open('input.txt', 'r')
line = fo.readlines()
line = [int(x.strip()) for x in line]

# ------------ Part 1 ------------ #

# Given a list of numbers, return the set of viable sums
def viableSums(l):
    tuples = list(combinations(l,2))
    return set([sum(x) for x in tuples])

# Progressively check that successive numbers belong to the windowed set of viable sums
cursor = 25
while cursor < (len(line) - 1) + 25:
    if line[cursor] in viableSums(line[cursor-25:cursor]):
        cursor += 1
    else:
        print('Violation detected with number {}.'.format(bad_number := line[cursor]))
        break

# ------------ Part 2 ------------ #

# Check a contiguous range of numbers for whether it adds up to the bad number. If so, return the computed answer.
def checkSum(window, target):
    for cursor in range(len(line) - window):
        contiguous_block = line[cursor:(cursor + window)]
        if sum(contiguous_block) == target:
            return min(contiguous_block) + max(contiguous_block)
    return 0

# Define a reasonable window search space
window_start, window_end = 5, 50

# Search these windows for the target sum
for x in range(window_start, window_end):  
    val = checkSum(x, bad_number)
    if val:
        print('The answer is {}.'.format(val))
        break
