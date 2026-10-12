"""exp02 — structure of the hard core H.

Question: where does the difficulty of 4/n = 1/x+1/y+1/z actually live?
Answer measured here: H = {n = 1 mod 24 with all prime divisors = 1 mod 24}.
Also records the repeated-denominator dichotomy (Theorem 8 / Corollary 9).
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_theory import enumerate_solutions, es_holds                   # noqa: E402
from es_sieve import in_hard_core, hard_core_values, factorise        # noqa: E402

LIMIT = 20_000

print("=== residue classes mod 24 without a solution (exact criterion) ===")
bad = {}
for r in range(24):
    miss = [n for n in range(max(2, r), LIMIT + 1, 24) if not es_holds(n)]
    bad[r] = miss
print("  ", {r: v[:6] for r, v in bad.items() if v} or "none")

print("\n=== reduction (Theorem 7) ===")
outside = [n for n in range(2, LIMIT + 1) if not in_hard_core(n)]
fail_outside = [n for n in outside if not es_holds(n)]
print(f"   {len(outside)} values outside H; failures: {fail_outside}")

H = hard_core_values(LIMIT)
print(f"\n=== hard core H up to {LIMIT}: {len(H)} values ===")
print("   first 30:", H[:30])

print("\n=== repeated denominators (Corollary 9) ===")
viol = []
for n in H:
    for x, y, z in enumerate_solutions(n):
        if not (x < y < z):
            viol.append((n, x, y, z))
print(f"   solutions in H that are NOT strictly increasing: {viol[:10]} (count {len(viol)})")

print("\n=== how many distinct solutions per hard-core n? ===")
c = Counter(len(enumerate_solutions(n)) for n in H)
print("   distribution:", dict(sorted(c.items())))
worst = min((len(enumerate_solutions(n)), n) for n in H)
print(f"   minimum: {worst[0]} solutions, attained at n = {worst[1]}")

print("\n=== prime vs composite in H ===")
pr = [n for n in H if len(factorise(n)) == 1]
co = [n for n in H if len(factorise(n)) > 1]
print(f"   primes {len(pr)}, composite {len(co)}")
