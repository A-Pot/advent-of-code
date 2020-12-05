#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import
import re

# List of valid codes to look out for
CODES = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

# ------------ Part 1 ------------ #

# Read data line by line
fo = open('input.txt', 'r')
lines = fo.readlines()
lines += '\n' # to trigger the reading of the last passport

# For each passport, assume all fields are missing (False) and set True when discovered otherwise
new_record = {c:False for c in CODES}
n0 = new_record.copy()
tot_valid = 0
for l in lines:
    for c in CODES:
        if c in l:
            n0[c] = True
    
    # If newline, then count passport as valid or not and set the next passport
    if l == '\n':
        tot_valid += ( (sum(n0.values()) == 8) or (sum(n0.values()) == 7 and n0['cid'] == False) )
        n0 = new_record.copy()
    
print(tot_valid)  

# ------------ Part 2 ------------ # 

# Define functions to check each condition
# This certainly could be more cleanly done with a single function, but... 
# I found this strategy easier to isolate and debug quickly
def check_byr(byr):
    return len(byr) == 4 and (1920 <= int(byr) <= 2002)

def check_iyr(iyr):
    return len(iyr) == 4 and (2010 <= int(iyr) <= 2020)

def check_eyr(eyr):  
    return len(eyr) == 4 and (2020 <= int(eyr) <= 2030)

def check_hgt(hgt):
    if 'cm' in hgt:
        hgt_val = int(hgt.replace('cm',''))
        if 150 <= hgt_val <= 193:
            return True
        else:
            return False
    elif 'in' in hgt:
        hgt_val = int(hgt.replace('in',''))
        if 59 <= hgt_val <= 76:
            return True
        else:
            return False
    else:
        return False

def check_hcl(hcl):
    if hcl[0] == "#":
        if len(hcl) == 7:
            hcl_sub = re.sub('[0-9]|[a-g]|[#]','',hcl)
            if hcl_sub != '':
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
def check_ecl(ecl):
    return (ecl in ['amb','blu','brn','gry','grn','hzl','oth'])

def check_pid(pid):
    return len(pid) == 9

# Same strategy of assuming all False, but this time setting to True based on code details
n0 = new_record.copy()
tot_valid = 0
for l in lines:
    for c in CODES:
        if c in l:
            # Extra iteration to figure out which chunk within the line contains the details... admittedly not ideal
            for it in l.split(' '):
                if c in it:
                    val = it.replace(c+':','').strip()                    
                    if c == 'byr':
                        n0[c] = check_byr(val)
                    elif c == 'iyr':
                        n0[c] = check_iyr(val)
                    elif c == 'eyr':
                        n0[c] = check_eyr(val)
                    elif c == 'hgt':
                        n0[c] = check_hgt(val)
                    elif c == 'hcl':
                        n0[c] = check_hcl(val)
                    elif c == 'ecl':
                        n0[c] = check_ecl(val)
                    elif c == 'pid':
                        n0[c] = check_pid(val)
                    else: # ( == 'cid')
                        n0[c] = True
                        
    # Exactly as before, if newline, then count passport as valid or not and set the next passport
    if l == '\n':
        tot_valid += ( (sum(n0.values()) == 8) or (sum(n0.values()) == 7 and n0['cid'] == False) )
        n0 = new_record.copy()
        
print(tot_valid)
