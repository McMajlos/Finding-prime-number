"""
main.py

This script provides three different implementations for checking if a number is prime, each with increasing levels of optimization:
- Level 1: Basic trial division
- Level 2: Optimized trial division (skips even and multiples of 3)
- Level 3: Highly optimized using 6k ± 1 rule and integer square root

Example big primes:
    50002952501
    98467039289
    928467051221
"""

# print(is_prime(97))
# print(is_prime_l2(50002952501))
# print(is_prime_l3(98467039289))


### LEVEL 1
def is_prime_l1(num):
    """
    Check if a number is prime using basic trial division.
    Args:
        num (int): Number to check.
    Returns:
        bool: True if prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True




### LEVEL 2
def is_prime_l2(num):
    """
    Check if a number is prime using optimized trial division.
    Skips even numbers and multiples of 3.
    Args:
        num (int): Number to check.
    Returns:
        bool: True if prime, False otherwise.
    """
    if num < 2:
        return False
    if num % 2 == 0:
        return True if num == 2 else False
    if num % 3 == 0:
        return True if num == 3 else False
    for i in range(2, (round(num ** (1 / 2))) + 1):
        if i % 2 == 0 or i % 3 == 0:
            continue
        if num % i == 0:
            return False
    return True



### LEVEL 3
import math


def is_prime_l3(n: int) -> bool:
    """
    Check if a number is prime using the 6k ± 1 optimization and integer square root.
    This is the most efficient method in this script.
    Args:
        n (int): Number to check.
    Returns:
        bool: True if prime, False otherwise.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    limit = math.isqrt(n)
    # print(limit)  # integer sqrt(n) without rounding up
    i = 5

    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:  # test 6k-1 and 6k+1
            return False
        i += 6
    return True

if __name__ == "__main__":
    print(is_prime_l1(101))
    print(is_prime_l2(50002952501))
    print(is_prime_l3(50002952501))
