"""
Module for Minimum Operations
"""

def minOperations(n):
    """
    execute only two operations in this file: Copy All and Paste
    
    Args
        n (int): number of paste character

    Return
        0 if n character is not archievable, the number of copy and paste
        operation if successful
    """
    count = 0
    paste = "H"

    while len(paste) < n:
        copy = paste
        count += 1
        for i in range(2):
            if len(paste) >= n:
                break
            count += 1
            paste += copy
    return count if len(paste) == n else 0
