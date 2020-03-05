import helpers


abundant_numbers = [n for n in range(28123) if sum(d for d in helpers.get_divisors(n) if d < n) > n]
print(sum(set(range(28123)).difference(set(i + j for i in abundant_numbers for j in abundant_numbers))))
