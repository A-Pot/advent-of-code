#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import
from itertools import product

# Load and prepare data
fo = open('input.txt', 'r')
line = fo.readlines()
line = [x.strip() for x in line]

# ------------ Part 1 ------------ #

# Init memory addresses
memory = {}

# Process each line
for l in line:
    
    # If mask, then set it as such
    if l.startswith('mask'):
        mask = l.split(' = ')[1]

    # Else it contains a memory address and value
    else:
        # Derive memory value and address
        mem_split = l.split(' = ')
        mem_val = int(mem_split[1])
        mem_address = ''.join(x for x in mem_split[0] if x.isdigit())
        
        # Convert value to binary
        mem_val_bin = format(mem_val, '036b')

        # Apply mask to bit string
        masked_bin = ''.join([mask[i] if mask[i] != 'X' else mem_val_bin[i] for i in range(len(mem_val_bin))])

        # Convert binary to value
        masked_int = int(masked_bin, 2)

        # Write value to address
        memory[mem_address] = masked_int

# Answer
print(sum(memory.values()))

# ------------ Part 2 ------------ #

# Init memory addresses
memory = {}

# Process each line
for l in line:
    
    # If mask, then set it as such
    if l.startswith('mask'):
        mask = l.split(' = ')[1]

    # Else it contains a memory address and value
    else:
        # Derive memory value and address
        mem_split = l.split(' = ')
        mem_val = int(mem_split[1])
        mem_address = ''.join(x for x in mem_split[0] if x.isdigit())
        
        # Convert the address to binary
        mem_address_bin = format(int(mem_address), '036b')

        # Apply mask to address bit string
        masked_addr_bin = ''.join([mask[i] if mask[i] in ('X', '1') else mem_address_bin[i] for i in range(len(mem_val_bin))])

        # Determine total number of floating bits
        num_X = sum([1 if x == 'X' else 0 for x in masked_addr_bin])
        
        # Enumerate all combinations of floating bits substitutions to consider
        combos = list(product([0, 1], repeat = num_X))

        # Write values to addresses
        for c in combos:
            c = list(c)
            addr = ''
            for j in masked_addr_bin:
                if j == 'X':
                    addr += str(c.pop(0))
                else:
                    addr += j

            # Convert binary to value
            masked_int = int(addr, 2)

            memory.update({masked_int:mem_val})

# Answer
print(sum(memory.values()))