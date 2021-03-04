#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Load data
fo = open('input.txt', 'r')
line = fo.readlines()

# ------------ Part 1 ------------ #

# Create a dictionary to flag whether each line has been run before
line_run = {x:0 for x in range(len(line))}

# Initialize accumulator and cursor
accumulator, cursor = 0, 0

while True:
        
    # If the line has been seen before, print accumulator value and halt
    if line_run[cursor]:
        print('Current line ({}) has been seen before. Accumulator value is {}.'.format(cursor, accumulator))
        break
    # Else, proceed to process the line
    else:
        line_run[cursor] = 1
        l = line[cursor].strip()
        
        command = l[:3]
        polarity = l[4]
        magnitude = int(l[5:])
        
        # Process command
        if command == 'acc':
            cursor += 1
            if polarity == '+':
                accumulator += magnitude
            else:
                accumulator -= magnitude
        elif command == 'jmp':
            if polarity == '+':
                cursor += magnitude
            else:
                cursor -= magnitude   
        else:
            cursor += 1
        
# ------------ Part 2 ------------ #

# Given a line number, attempt to flip the given line, and return 1 if the program terminates; 0 otherwise
def testFlip(line_number):
    
    # We are given that acc lines are not to be modified
    if 'acc' in line[line_number]:
        return 0
    
    else:
        # Create a dictionary to flag whether each line has been run before
        line_run = {x:0 for x in range(len(line))}
        
        # Initialize accumulator and cursor
        accumulator, cursor = 0, 0
        
        while True:
            
            # If the line has been seen before, return 0, as it indicates an infinite loop
            if line_run[cursor]:
                return 0
             
            # Else, proceed to process the line
            else:
                line_run[cursor] = 1
                l = line[cursor].strip()
                
                command = l[:3]
                polarity = l[4]
                magnitude = int(l[5:])
                
                # Flip command if this line corresponds to the flip line
                if cursor == line_number:
                    if command == 'jmp':
                        command = 'nop'
                    else:
                        command = 'jmp'
                
                # Process command accordingly
                if command == 'acc':
                    cursor += 1
                    if polarity == '+':
                        accumulator += magnitude
                    else:
                        accumulator -= magnitude
                elif command == 'jmp':
                    if polarity == '+':
                        cursor += magnitude
                    else:
                        cursor -= magnitude   
                else:
                    cursor += 1
                    
            # If the cursor is at the last line, we have terminated
            if cursor == len(line):
                print('We have successfully terminated by flipping line number {}, and the accumulator is {}.'.format(line_number, accumulator))
                return 1

# Try flipping sequentially until we've discovered the right line to flip
for x in range(len(line)):
    testFlip(x)
