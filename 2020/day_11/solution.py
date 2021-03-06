#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
import numpy as np
import collections

# Load and prepare data as matrix of chars
fo = open('input.txt', 'r')
line = fo.readlines()
df = np.vstack([np.array([x for x in line[y].strip()]) for y in range(len(line))])
max_x, max_y = df.shape

# ------------ Part 1 ------------ #

# Given an (x,y) coordinate, enforce the rules as described
def adjustSeat(x,y,df):
    
    # Get the current seat value
    seatVal = df[x,y]
    
    # Get a list of adjacent seat statuses (3x3 window slice, with middle coordinate value removed)
    adjacent_seats = df[max((x-1),0):min((x+2),max_x),max((y-1),0):min((y+2),max_y)].flatten().tolist()
    adjacent_seats.remove(seatVal)
        
    #If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if seatVal == 'L' and '#' not in adjacent_seats:
        return '#'
            
    #If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    num_hash = dict(collections.Counter(adjacent_seats)).get('#')
    if seatVal == '#' and num_hash is not None and num_hash >= 4:
        return 'L'
    
    # Otherwise, the seat's state does not change.
    return seatVal

# Apply seat adjustments until convergence; then report back the number of occupied seats
def getSteadyStateSeats(df, adjustSeat):
    
    # Initialize two states
    df_current = df.copy()
    df_next = df.copy()

    # Until convergence, apply seat adjustments to every element
    while True:
        for i in range(max_x):
            for j in range(max_y):
                df_next[i,j] = adjustSeat(i,j,df_current)
                
        # If converged, return the number of occupied seats
        if np.all(df_current == df_next):
            return collections.Counter(df_current.flatten())['#']
        
        # Else, update the seats and adjust again
        else:
            df_current = df_next.copy()

# Answer
print(getSteadyStateSeats(df, adjustSeat))

# ------------ Part 2 ------------ #

# Given a direction, check to see if an occupied seat is ever encountered
def checkDirection(x, y, x_direction, y_direction, df):
    
    # First proposed direction check
    new_x_coord = x + x_direction
    new_y_coord = y + y_direction
    
    # While we haven't hit a boundary, keep checking for an empty or full seat
    while (0 <= new_x_coord <= max_x-1) and (0 <= new_y_coord <= max_y-1):
        
        val = df[new_x_coord, new_y_coord]
        
        if val in ['L','#']:
            return val
        else:
            new_x_coord += x_direction
            new_y_coord += y_direction
        
    # If we haven't returned yet, then nothing was found in the path
    return '.'
    
# Given an (x,y) coordinate, enforce the (updated) rules as described
def adjustSeat2(x,y,df):

    # Get the current seat value
    seatVal = df[x,y]
    
    # Identify and count the observed seats in all directions
    adjacent_seats = [checkDirection(x,y,i,j,df) for i in [-1,0,1] for j in [-1,0,1] if i|j]
    
    #If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if seatVal == 'L' and '#' not in adjacent_seats:
        return '#'
            
    #If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
    num_hash = dict(collections.Counter(adjacent_seats)).get('#')
    if seatVal == '#' and num_hash is not None and num_hash >= 5:
        return 'L'
    
    # Otherwise, the seat's state does not change.
    return seatVal

# Answer
print(getSteadyStateSeats(df, adjustSeat2))
