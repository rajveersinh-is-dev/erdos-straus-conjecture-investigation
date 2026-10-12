"""exp05 — the obstruction theorem (Theorem 14) and the resistant instances.

Measures how much of the hard core survives the proved necessary conditions
(O1)-(O3) for being a counterexample, and locates the instances of H with the
largest minimal admissible k (mu).
"""
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_sieve import (hard_core_values, factorise, divisors, minimal_k,  # noqa: E402
                      es_via_k)

OBSTR = 600_000
REC = 3_000_000

print("### Theorem 14 — obstruction strength")
H = hard_core_values(OBSTR)
print(f"   hard-core values <= {OBSTR}: {len(H)}")


def o1(n):   # every prime divisor of (n+3)/4 is 1 mod 3
    return not any(p % 3 == 2 for p in factorise((n + 3) // 4))


def o2(n):   # every odd prime divisor of n+1 is 1 mod 4
    return not any(p % 4 == 3 for p in factorise(n + 1))


def o3(n):   # every prime divisor of n+4 is 1 mod 4
    return not any(p % 4 == 3 for p in factorise(n + 4))


for name, f in (("(O1)", o1), ("(O2)", o2), ("(O3)", o3)):
    print(f"   {name} alone leaves {sum(f(n) for n in H)}/{len(H)}"
          f" = {sum(f(n) for n in H)/len(H):.4f}")
both = sum(o1(n) and o2(n) for n in H)
triple = [n for n in H if o1(n) and o2(n) and o3(n)]
print(f"   (O1)+(O2) leaves {both}/{len(H)} = {both/len(H):.4f}")
print(f"   (O1)+(O2)+(O3) leaves {len(triple)}/{len(H)} = {len(triple)/len(H):.4f}")
print("   first 25 surviving:", triple[:25])

hard = [(minimal_k(n, 32), n) for n in triple]
hard.sort(reverse=True)
print(f"   of those, mu > 23 for {sum(1 for k, _ in hard if k and k > 23)} of them")
print("   the ones needing mu > 23:", [n for k, n in hard if k and k > 23][:20])

print("\n### prime vs composite in H")
H2 = hard_core_values(REC)
print(f"   hard-core values <= {REC}: {len(H2)}")
pr = [n for n in H2 if len(factorise(n)) == 1]
co = [n for n in H2 if len(factorise(n)) > 1]
print(f"   primes {len(pr)}, composite {len(co)}")
mx_pr = max(minimal_k(n, 64) or 10**9 for n in pr)
mx_co = max(minimal_k(n, 64) or 10**9 for n in co)
print(f"   max mu among primes    : {mx_pr}")
print(f"   max mu among composites: {mx_co}")

print("\n### records of mu (mu = smallest k = 3 mod 4 admitting a solution)")
recs = sorted(((minimal_k(n, 64), n) for n in H2), reverse=True)
print("   largest:", recs[:12])
never = [n for n in H2 if minimal_k(n, 64) is None]
print(f"   values of H <= {REC} with no solution for k <= 255: {len(never)}")

dist = Counter(k for k, _ in recs)
summary = {
    "obstruction_limit": OBSTR, "count_H_at_obstruction_limit": len(H),
    "survivors_O1": sum(o1(n) for n in H),
    "survivors_O1_O2": both,
    "survivors_O1_O2_O3": len(triple),
    "record_limit": REC, "count_H_at_record_limit": len(H2),
    "mu_distribution": {str(k): v for k, v in sorted(dist.items())},
    "max_mu": recs[0][0],
    "max_mu_attained_at": [n for k, n in recs if k == recs[0][0]],
    "no_solution_below_k255": len(never),
}
os.makedirs("results", exist_ok=True)
with open("results/sieve_summary.json", "w") as fh:
    json.dump(summary, fh, indent=2)
print("\nwrote results/sieve_summary.json")
