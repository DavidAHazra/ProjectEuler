import helpers


def get_rotations(n):
    rotations = []
    for rotation_amount in range(len(n)):
        rotation = ["0"] * len(n)
        for start_place in range(len(n)):
            rotation[(start_place + rotation_amount) % len(n)] = n[start_place]

        rotations.append(int("".join(rotation)))

    return rotations


print(len(list(number for number in range(2, 1000000) if helpers.is_prime(number) and all(
    [helpers.is_prime(rotation) for rotation in get_rotations(str(number))]))))
