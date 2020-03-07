import helpers


def triangle_number(n):
    return int(n / 2 * (n + 1))


for n, _ in enumerate(helpers.infinity()):
    if helpers.get_divisor_count(triangle_number(n)) > 500:
        print(triangle_number(n))
        break
