#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Load and prepare data
fo = open('input.txt', 'r')
line = fo.readlines()
line = [x.strip() for x in line]

# ------------ Part 1 ------------ #

# Assume the ship starts at the origin and faces east
ship = {'x':0,'y':0,'dir':'E'}

# Define left/right turn group
turn_group = ['N','E','S','W']

# Function that, given an instruction, updates the ship position or direction
def processInstruction(inst):
    action, magnitude = inst[0], int(inst[1:])
    
    # For forward movement, treat the action as the current direction
    if action == 'F':
        action = ship['dir']
    
    # Otherwise, move accordingly
    if action == 'N':
        ship['y'] = ship['y'] + magnitude
    elif action == 'S':
        ship['y'] = ship['y'] - magnitude
    elif action == 'E':
        ship['x'] = ship['x'] + magnitude
    elif action == 'W':
        ship['x'] = ship['x'] - magnitude
    elif action == 'L':
        ship['dir'] = turn_group[(turn_group.index(ship['dir']) - magnitude//90) % 4]
    elif action == 'R':
        ship['dir'] = turn_group[(turn_group.index(ship['dir']) + magnitude//90) % 4]
    else:
        raise ValueError(action, magnitude)

# Move ship for all instructions
for l in line:
    processInstruction(l)

# Manhattan Distance
print(abs(ship['x']) + abs(ship['y']))

# ------------ Part 2 ------------ #

# Given a rotation action, return the coordinates of the waypoint rotated about the ship
def processRotation(action, magnitude):
        
    # Aliases
    sx, sy = ship['x'], ship['y']
    wx, wy = waypoint['x'], waypoint['y']
    
    # R90 or L270
    if (action == 'R' and magnitude == 90) or (action == 'L' and magnitude == 270):
        # Swap x and y, change sign of y, and adjust for origin translation
        return ((wy-sy) + sx, -(wx-sx) + sy)
    # R270 or L90
    elif (action == 'R' and magnitude == 270) or (action == 'L' and magnitude == 90):
        # Swap x and y, change sign of x, and adjust for origin translation
        return (-(wy-sy) + sx, (wx-sx) + sy)
    # R/L 180
    elif magnitude == 180:
        # Change signs and adjust for origin translation
        return (-(wx-sx) + sx, -(wy-sy) + sy)
    else:
        raise ValueError(action, magnitude)
    
# Given a forward motion magnitude, move the ship and waypoint in the ship-to-waypoint direction
def processForwardMotion(magnitude):
    
    # Aliases
    sx, sy = ship['x'], ship['y']
    wx, wy = waypoint['x'], waypoint['y']
    
    # How far to move both the ship and the waypoint
    move_x, move_y = abs(wx-sx)*magnitude, abs(wy-sy)*magnitude
    
    # Move X in direction of waypoint
    if sx < wx:
        ship['x'] = ship['x'] + move_x
        waypoint['x'] = waypoint['x'] + move_x
    else:
        ship['x'] = ship['x'] - move_x
        waypoint['x'] = waypoint['x'] - move_x
        
    # Move Y in direction of waypoint
    if sy < wy:
        ship['y'] = ship['y'] + move_y
        waypoint['y'] = waypoint['y'] + move_y
    else:
        ship['y'] = ship['y'] - move_y
        waypoint['y'] = waypoint['y'] - move_y
    
# Process the movements under the new waypoint method
def processWaypointInstruction(inst):
    action, magnitude = inst[0], int(inst[1:])
    
    # Actions
    if action == 'N':
        waypoint['y'] = waypoint['y'] + magnitude
    elif action == 'S':
        waypoint['y'] = waypoint['y'] - magnitude
    elif action == 'E':
        waypoint['x'] = waypoint['x'] + magnitude
    elif action == 'W':
        waypoint['x'] = waypoint['x'] - magnitude
    elif action in ['L','R']:
        waypoint['x'], waypoint['y'] = processRotation(action, magnitude)
    elif action == 'F':
        processForwardMotion(magnitude)
    else:
        raise ValueError(action, magnitude)
        
# Reinitialize the ship and initialize a new waypoint
ship = {'x':0,'y':0}
waypoint = {'x':10,'y':1}

# Move ship for all instructions
for l in line:
    processWaypointInstruction(l)

# Manhattan Distance
print(abs(ship['x']) + abs(ship['y']))
