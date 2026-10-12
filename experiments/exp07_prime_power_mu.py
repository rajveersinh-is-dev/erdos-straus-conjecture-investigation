import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_sieve import (factorise, in_hard_core, is_prime,          # noqa: E402
                       is_prime_power, minimal_k)

pw = [m for m in range(25, 3_000_000, 24) if in_hard_core(m) and is_prime_power(m)]
print("prime powers in H cap [1, 3e6]:", len(pw))
print("first few:", pw[:8])
mus = {m: minimal_k(m, 64) for m in pw}
best = max(v or 10**9 for v in mus.values())
print("max mu among prime powers of H:", best)
print("attained at:", sorted(m for m, v in mus.items() if v == best))
print("sorted mu values:", sorted(set(mus.values())))

for n in (118801, 806521):
    print(n, "factorisation:", factorise(n), "is_prime:", is_prime(n),
          "mu:", minimal_k(n, 64))