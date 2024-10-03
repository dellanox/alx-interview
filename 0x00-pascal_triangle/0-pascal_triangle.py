#!/usr/bin/python3
"""
Pascal's Triangle Module
"""

def pascal_triangle(n):
    """
    Returns a list of integers forming Pascal’s triangle of n.
    
    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
