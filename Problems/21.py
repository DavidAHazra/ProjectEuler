import helpers


def d(n): return sum(d for d in helpers.get_divisors(n) if d < n)


print(sum(n for n in range(10000) if d(d(n)) == n and d(n) != n))
