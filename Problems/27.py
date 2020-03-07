import helpers


def get_highest_consecutive(a, b):
    n = 0
    while helpers.is_prime(n ** 2 + a * n + b):
        n += 1

    return n


print((lambda y: y[1] * y[2])(max([max([(get_highest_consecutive(a, b), a, b) for b in range(-1000, 1001)],
                                       key=lambda x: x[0]) for a in range(-999, 1000)], key=lambda x: x[0])))
