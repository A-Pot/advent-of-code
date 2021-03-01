#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
import re

# Load data
fo = open('input.txt', 'r')
line = fo.readlines()

# ------------ Part 1 ------------ #

# Obtain every color
all_colors = [x.split('bags')[0].strip() for x in line]

# For a bag of a given color, return 1 if it eventually contains a shiny gold bag; else return 0
def hasShinyGoldBag(color):
    
    # Retrieve line associated with the given color
    l = list(filter(lambda x: x.startswith(color), line))[0]
    l = l.replace('.','').strip()

    # Split on 'bags contain' and again on 'bag(s)'
    split = l.split('bags contain')    
    containees = split[1].replace('bags','bag').split('bag')
    
    # Clean up the split a bit
    containees = [re.sub('\d|,|\.','',x).strip() for x in containees]
    containees = [x for x in containees if x]

    # Check for shiny gold bag membership
    if 'shiny gold' in containees:
        return 1
    
    # Then check for no nested bag case
    elif 'no other' in containees:
        return 0
    
    # Finally, recurse for each contained bag
    else:
        bag_recurse = [hasShinyGoldBag(c.strip()) for c in containees]
        return 1 in bag_recurse

# Check this for all colors, and add up the total number containing a shiny gold bag
print(sum([hasShinyGoldBag(x) for x in all_colors]))

# ------------ Part 2 ------------ #

# For a given color, return the number of bags contained within it
def countBags(color):
    
    # Retrieve line associated with the given color
    l = list(filter(lambda x: x.startswith(color), line))[0]
    l = l.replace('.','').strip()

    # Split on 'bags contain' and again on 'bag(s)'
    split = l.split('bags contain')    
    containees = split[1].replace('bags','bag').split('bag')
    
    # Clean up the split a bit
    containees = [re.sub('\d|,|\.','',x).strip() for x in containees]
    containees = [x for x in containees if x]
    
    # Check for no nested bag case
    if 'no other' in containees:
        return 0
    
    # Otherwise, return the sum total for the recursed bags
    else:
        coeff = [int(x) for x in l if x.isdigit()]        
        bag_recurse = [coeff[i] + coeff[i] * countBags(containees[i]) for i in range(len(containees))]
        return sum(bag_recurse)
        
# The answer becomes:
print(countBags('shiny gold'))
