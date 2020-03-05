import helpers
print(max([num_1 * num_2 for num_1 in range(100, 1000) for num_2 in range(100, 1000)
           if helpers.is_palindrome(num_1 * num_2)]))
