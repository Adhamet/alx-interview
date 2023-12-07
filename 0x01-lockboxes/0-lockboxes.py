#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Solution of the problem:
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxesChecked = False
        for idx in range(len(boxes)):
            boxesChecked = k in boxes[idx] and k != idx
            if boxesChecked:
                break
        if boxesChecked == False:
            return boxesChecked
    return True
