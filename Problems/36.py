import helpers
print(sum(n for n in range(1000000) if helpers.is_palindrome(str(n)) and helpers.is_palindrome("{0:b}".format(n))))
