import itertools
print([''.join(perm) for perm in itertools.permutations("0123456789", len("0123456789"))][999999])
