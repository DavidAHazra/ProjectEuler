import helpers

n = 1
while True:
    if len(str(helpers.get_nth_fibonacci(n))) >= 1000:
        print(n)
        break

    n += 1
