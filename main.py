"""
    Recursive function to compute the Fibonacci sequence.
    By using recursion, the performance would be O(n).
"""
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
