#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ------------ Part 1 ------------ #

# init speak sequence and history
def init():
    speak_sequence = [1,20,11,6,12,0]
    speak_history = {}
    for i, j in enumerate(speak_sequence, start = 1):
        speak_history[j] = [0,i]
    return speak_sequence, speak_history, len(speak_sequence) + 1

def get_num_to_speak(num):
    if num not in speak_history or speak_history[num][0] == 0:
        return 0
    else:
        speak_diff = speak_history[num][1] - speak_history[num][0]
        return speak_diff

def speak_num(num, turn):
    if num in speak_history:
        speak_history[num].append(turn)
        speak_history[num] = speak_history[num][1:]
    else:
        speak_history[num] = [0, turn]
    speak_sequence.append(num)

speak_sequence, speak_history, turn_start = init()
for turn in range(turn_start, 2021):
    num = speak_sequence[-1]
    num_to_speak = get_num_to_speak(num)
    speak_num(num_to_speak, turn)

# Answer
print(speak_sequence[-1])

# ------------ Part 2 ------------ #

speak_sequence, speak_history, turn_start = init()
for turn in range(turn_start, 30000001):
    num = speak_sequence[-1]
    num_to_speak = get_num_to_speak(num)
    speak_num(num_to_speak, turn)

# Answer
print(speak_sequence[-1])
