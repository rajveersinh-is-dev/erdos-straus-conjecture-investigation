"""exp05 — the obstruction theorem (Theorem 14) and the resistant instances.

Measures how much of the hard core survives the proved necessary conditions
(O1)-(O3) for being a counterexample, and locates the instances of H with the
largest minimal admissible k (mu).
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_sieve import (hard_core_values, factorise, divisors, minimal_k,  # noqa: E402
                      es_via_k, is_prime, is_prime_power)

OBSTR = 600_000
REC = 3_000_000

print("### Theorem 14 — obstruction strength")
H = hard_core_values(OBSTR)
print(f"   hard-core values <= {OBSTR}: {len(H)}")


def o1(n):
    """O1.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return not any(p % 3 == 2 for p in factorise((n + 3) // 4))


def o2(n):
    """O2.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return not any(p % 4 == 3 for p in factorise(n + 1))


def o3(n):
    """O3.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
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
# NB: `len(factorise(n)) == 1` is NOT the same as "n is prime" -- it also holds
# for every prime power p^e, e >= 2.  See research/proof_attempts.md, A9.
pr = [n for n in H2 if is_prime(n)]
pw = [n for n in H2 if is_prime_power(n)]
co = [n for n in H2 if not is_prime(n)]
co2 = [n for n in H2 if len(factorise(n)) > 1]      # >= 2 distinct prime factors
print(f"   primes {len(pr)}  (of which prime p: {len(pr)})")
print(f"   prime powers p^e, e>=2: {len(pw)}   first few: {pw[:8]}")
print(f"   composites total {len(co)}  (= {len(co2)} with >= 2 distinct prime factors"
      f" + {len(pw)} prime powers)")
assert len(pr) + len(co) == len(H2), "partition failed"
assert len(pw) + len(co2) == len(co), "sub-partition failed"
mus_pr = {n: minimal_k(n, 64) for n in pr}
mus_co = {n: minimal_k(n, 64) for n in co}
mx_pr = max(v or 10**9 for v in mus_pr.values())
mx_co = max(v or 10**9 for v in mus_co.values())
print(f"   max mu among primes    : {mx_pr}  at "
      f"{sorted(n for n, v in mus_pr.items() if v == mx_pr)}")
print(f"   max mu among composites: {mx_co}  at "
      f"{sorted(n for n, v in mus_co.items() if v == mx_co)}")
mx_pw = max(mus_co[n] or 10**9 for n in pw)
print(f"   max mu among the {len(pw)} prime powers: {mx_pw}")

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
    "primes_at_record_limit": len(pr),
    "prime_powers_at_record_limit": len(pw),
    "composites_at_record_limit": len(co),
    "max_mu_among_primes": mx_pr,
    "max_mu_among_composites": mx_co,
    "mu_distribution": {str(k): v for k, v in sorted(dist.items())},
    "max_mu": recs[0][0],
    "max_mu_attained_at": [n for k, n in recs if k == recs[0][0]],
    "no_solution_below_k255": len(never),
}
os.makedirs("results", exist_ok=True)
with open("results/sieve_summary.json", "w") as fh:
    json.dump(summary, fh, indent=2)
print("\nwrote results/sieve_summary.json")
