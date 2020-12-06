#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
from string import ascii_lowercase

# Load data
fo = open('/Users/apot/projects/AdventOfCode/2020/day_6/input.txt', 'r')
line = fo.readlines()
line += '\n'

# ------------ Part 1 ------------ #

# New questionnaire
questions = {x:0 for x in ascii_lowercase}

# Flip 0's to 1's if anyone answered and add up for each group
cnt_p1 = 0
q0 = questions.copy()
for l in line:
    l = l.strip()
    for c in l:
        q0[c] = 1
    if l == '':
        cnt_p1 += sum(q0.values())
        q0 = questions.copy()
    
print(cnt_p1)

# ------------ Part 2 ------------ #

# This time, keep track of group number and accumulate responses
cnt_p2, group_num = 0,0
q0 = questions.copy()
for l in line:
    l = l.strip()
    group_num += 1
    for c in l:
        q0[c] = q0[c] + 1
    if l == '':
        cnt_p2 += sum([1 if x == group_num - 1 else 0 for x in q0.values()])
        q0 = questions.copy()
        group_num = 0
    
print(cnt_p2)
