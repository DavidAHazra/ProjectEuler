import math
import functools
import operator
import itertools
import collections


def is_divisible(x, y):
    return x % y == 0


def get_nth_fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")

    return _fib(n)[0]


def _fib(n):
    if n == 0:
        return 0, 1

    a, b = _fib(n // 2)
    c = a * (b * 2 - a)
    d = a * a + b * b
    if is_divisible(n, 2):
        return c, d

    return d, c + d


def get_n_fibonacci(n):
    return [get_nth_fibonacci(index) for index in range(n)]


def is_prime(n):
    if n <= 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i * i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def primes(n):
    if n == 2:
        return [2]

    elif n < 2:
        return []

    result = list(range(3, n + 1, 2))
    half = (n + 1) // 2 - 1

    i = 0
    m = 3
    while m <= math.sqrt(n):
        if result[i]:
            j = (m * m - 3) // 2
            result[j] = 0

            while j < half:
                result[j] = 0
                j += m

        i += 1
        m = 2 * i + 3

    return [2] + [x for x in result if x]


def get_nth_prime(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break

        else:
            prime_list.append(num)

        num += 2

    return prime_list[-1]


def get_unique_prime_factors(n):
    return [test for test in range(2, math.floor(math.sqrt(n))) if is_prime(test) and n % test == 0]


def full_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors


def infinity():
    while True:
        yield


def get_divisors(n):
    pf = get_unique_prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def get_divisor_count(n):
    prime_f = full_prime_factors(n)
    return prod(prime_f.count(unique_factor) + 1 for unique_factor in set(prime_f))


def is_palindrome(n):
    if type(n) == str:
        return n[::-1] == n
    else:
        return str(n)[::-1] == str(n)


def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)
