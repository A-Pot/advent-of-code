#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
from pandas import read_csv

# Load data
input = read_csv('input.txt', header = None)

# ------------ Part 1 ------------ #

# Given a single entry, return whether that entry is valid
def isValidPart1(pw):
    rng, key, password = pw.replace(':','').split(' ')
    rng_min, rng_max = rng.split('-')
    return int(rng_min) <= len(password) - len(password.replace(key,'')) <= int(rng_max)
    
# Apply to all entires and count
print(sum([isValidPart1(x) for x in input.values.flatten()]))

# ------------ Part 2 ------------ #

# Using the new set of rules, we must examine two characters from each password
def isValidPart2(pw):
    rng, key, password = pw.replace(':','').split(' ')
    rng_min, rng_max = rng.split('-')
    first = password[int(rng_min) - 1]
    last = password[int(rng_max) - 1]
    return (key in first or key in last) and (first != last)
        
# Apply to all entires and count
print(sum([isValidPart2(x) for x in input.values.flatten()]))
