#!/usr/bin/python3
"""
Module for calculating minimum operations
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to get exactly n 'H' characters
    using only Copy All and Paste operations.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required to reach n.
             Returns 0 if n is less than or equal to 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Reduce n by dividing with smallest possible divisor
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

