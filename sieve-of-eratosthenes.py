"""
This code implements the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.
"""

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for number in range(2, limit + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    return primes

# Test the sieve_of_eratosthenes function
limit = 100

results = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}: {results}")