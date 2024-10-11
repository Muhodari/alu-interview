#!/usr/bin/python3
"""
Function to generate Pascal's triangle.
"""

def generate_pascals_triangle(rows):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        rows (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if rows <= 0.
    """
    if rows <= 0:
        return []

    triangle = [[1]]

    for current_row in range(1, rows):
        previous_row = triangle[-1]
        new_row = [1]

        for col in range(1, current_row):
            new_row.append(previous_row[col - 1] + previous_row[col])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
