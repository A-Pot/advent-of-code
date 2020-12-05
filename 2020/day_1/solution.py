#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
from pandas import read_csv

# Load data
dat = read_csv('input.txt', header = None).values.flatten()

# ------------ Part 1 ------------ #

# Create set from input vector
s = set(dat)

# Iterate over set combiantions until answer is found
def getAnswerPart1(s):
    for x in s:
        for y in s - {x}:
            if x + y == 2020:
                return x * y

print(getAnswerPart1(s))

# ------------ Part 2 ------------ #

# Same idea, but with an extra layer of iteration
def getAnswerPart2(s):
    for x in s:
        for y in s - {x}:
            for z in s - {x} - {y}:
                if x + y + z == 2020:
                    return x * y * z

print(getAnswerPart2(s))
