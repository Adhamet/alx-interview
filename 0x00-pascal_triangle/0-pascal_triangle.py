#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of (n)"""
    if n <= 0:
        return list()

    triangle = [[1]]
    for r in range(1,n):
        row = [1]
        for c in range(1,r):
            row.append(triangle[r-1][c] + triangle[r-1][c-1])
        row.append(1)
        triangle.append(row)
    return triangle
