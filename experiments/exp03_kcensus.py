"""exp03 — the k-census and the sharp k = 3 criterion (Theorem 10).

For each k = 4j-1 the exact criterion (T) decides whether a solution exists
with 4x - n = k.  This script
  (a) tabulates which small k cover which hard-core values,
  (b) verifies the sharp k = 3 criterion of Theorem 10 in both directions,
  (c) verifies the "u = 1 is impossible" statement of Theorem 11.
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_sieve import (hard_core_values, es_via_k, es_via_j, minimal_k,   # noqa: E402
                      factorise, AB_of)

LIMIT = 300_000
KS = [3, 7, 11, 15, 19, 23, 27, 31]
H = hard_core_values(LIMIT)
print(f"hard-core values <= {LIMIT}: {len(H)}")

cov = {k: sum(es_via_k(n, k) is not None for n in H) for k in KS}
print("\ncoverage by a single k:")
for k in KS:
    print(f"   k={k:>3}: {cov[k]:>5}/{len(H)}  ({cov[k]/len(H):.4f})")

print("\nminimal admissible k, distribution:")
dist = Counter(minimal_k(n, 40) for n in H)
print("  ", dict(sorted(dist.items(), key=lambda kv: (kv[0] is None, kv[0]))))

core = [3, 7, 11, 15, 23]
c = sum(any(es_via_k(n, k) is not None for k in core) for n in H)
print(f"\ncore k-set {core} covers {c}/{len(H)} = {c/len(H):.6f}")

# ---------------------------------------------------------------- Theorem 10
print("\n=== Theorem 10: k = 3  <=>  (n+3)/4 has a prime factor = 2 (mod 3) ===")
mis = 0
for n in H:
    has = any(p % 3 == 2 for p in factorise((n + 3) // 4))
    got = es_via_k(n, 3) is not None
    if has != got:
        mis += 1
        if mis <= 5:
            print("   MISMATCH", n, has, got)
print(f"   mismatches: {mis} of {len(H)}")

# ---------------------------------------------------------------- Theorem 11
print("\n=== Theorem 11: k = 3 mod 4 never divides n^2+4 ===")
viol = [(n, k) for n in H for k in range(3, 73, 4) if (n * n + 4) % k == 0]
print("   violations:", viol[:10], f"(count {len(viol)})")
bad_p = [(n, p) for n in range(25, 4000, 24) for p in factorise(n * n + 4)
         if p % 4 != 1]
print("   prime divisors of n^2+4 that are != 1 (mod 4):", bad_p[:10])
