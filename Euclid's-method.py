"""
This module implements Euclid's algorithm for computing the greatest common divisor (GCD) of two integers.
"""

def gcd(m,  n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

# Test the gcd function

results =gcd(48, 18)

print(f"The GCD of 48 and 18 is: {results}")
    # Output: The GCD of 48 and 18 is: 6