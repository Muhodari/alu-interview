# Minimum Operations

## Description
This project contains a Python module that calculates the minimum number of operations required to reach a given number of characters `n` starting from a single character. The allowed operations are copying all characters and pasting them. The goal is to determine the minimum number of these operations needed to achieve exactly `n` characters.

## Files
- `0-minoperations.py`: Contains the `minOperations` function which performs the calculation.
- `0-main.py`: Main file for testing the `minOperations` function.

## Function
### minOperations
```python
def minOperations(n):
    """
    Calculates the minimum operations to reach n characters

    Args:
        n (int): The number of characters to reach

    Returns:
        int: The minimum operations to reach n characters
    """