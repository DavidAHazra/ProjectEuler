import helpers
print(sum(value for value in helpers.get_n_fibonacci(50) if value < 4000000 and value % 2 == 0))
