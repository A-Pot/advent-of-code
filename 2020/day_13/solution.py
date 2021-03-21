#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import
from sympy.ntheory.modular import crt

# Load and prepare data
fo = open('input.txt', 'r')
line = fo.readlines()
line = [x.strip() for x in line]

time = int(line[0])
buses = [int(x) for x in line[1].split(',') if x != 'x']

# ------------ Part 1 ------------ #

# Mod time by all bus IDs
mods = [time % x for x in buses]

# The best bus has the highest mod value
best_bus = buses[mods.index(max(mods))]

# The time difference
wait_time = best_bus - (time % best_bus)

# The answer is then the product of these
print(best_bus * wait_time)

# ------------ Part 2 ------------ #

# CRT via sympy

# Reload buses and departure times
buses = [x for x in line[1].split(',')]
departure_times = {int(buses[x]):int(x) for x in range(len(buses)) if buses[x] != 'x'}
buses = [int(x) for x in line[1].split(',') if x != 'x']
departure_times_vals = list(departure_times.values())

# Prepare for CRT input
m, v = buses, [-departure_times_vals[i] % buses[i] for i in range(len(buses))]

# Answer
print(crt(m = m, v = v)[0])
