def is_pandigital(n):
    numbers_in = [str(i) for i in range(1, len(str(n)) + 1)]
    n_str = list(str(n))
    for i in numbers_in:
        if i not in n_str:
            return False

        n_str.remove(i)

    return True

print(is_pandigital(152346))