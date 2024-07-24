#!/usr/bin/python3
"""Module defining isWinner function."""

def isWinner(x, nums):
    """Function to get who has won in prime game"""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins_count = 0
    ben_wins_count = 0

    for num in nums:
        if num < 2:
            ben_wins_count += 1
            continue

        is_maria_turn = True
        rounds_set = list(range(1, num + 1))
        primes_set = [p for p in range(2, num + 1) if primes[p]]

        while primes_set:
            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]
            primes_set = [p for p in primes_set if p in rounds_set]
            is_maria_turn = not is_maria_turn

        if is_maria_turn:
            ben_wins_count += 1
        else:
            maria_wins_count += 1

    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Returns a list where the index is True if it is a prime number."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes


# Test
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
