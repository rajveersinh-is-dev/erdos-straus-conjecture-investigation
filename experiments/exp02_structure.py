"""exp02 — structure of the hard core H.

Question: where does the difficulty of 4/n = 1/x+1/y+1/z actually live?
Answer measured here: H = {n = 1 mod 24 with all prime divisors = 1 mod 24}.
Also records the repeated-denominator dichotomy (Theorem 8 / Corollary 9).
"""
import os
import sys
from collections import Counter
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_theory import enumerate_solutions, es_holds  # noqa: E402
from es_sieve import in_hard_core, hard_core_values, factorise  # noqa: E402


def _validate_limit(limit: int) -> None:
    """Ensure limit is a sensible positive integer."""
    if not isinstance(limit, int):
        raise TypeError("LIMIT must be an integer")
    if limit < 2:
        raise ValueError("LIMIT must be at least 2 to examine n >= 2")


def residue_classes_without_solution(limit: int) -> dict[int, List[int]]:
    """Return a dict mapping each residue r (0..23) to the list of n ≡ r (mod 24)
    for which the Erdős–Straus conjecture fails (i.e. es_holds(n) is False)."""
    bad: dict[int, List[int]] = {}
    for r in range(24):
        start = max(2, r)
        miss = [n for n in range(start, limit + 1, 24) if not es_holds(n)]
        bad[r] = miss
    return bad


def outside_hard_core(limit: int) -> Tuple[List[int], List[int]]:
    """Return numbers outside the hard core and those among them that fail the conjecture."""
    outside = [n for n in range(2, limit + 1) if not in_hard_core(n)]
    fail_outside = [n for n in outside if not es_holds(n)]
    return outside, fail_outside


def repeated_denominator_violations(hard_core: List[int]) -> List[Tuple[int, int, int, int]]:
    """Collect (n, x, y, z) for solutions of n in hard core that are NOT strictly increasing."""
    viol: List[Tuple[int, int, int, int]] = []
    for n in hard_core:
        for x, y, z in enumerate_solutions(n):
            if not (x < y < z):
                viol.append((n, x, y, z))
    return viol


def solution_count_distribution(hard_core: List[int]) -> Tuple[dict[int, int], Tuple[int, int]]:
    """Return distribution of solution counts and the (min_count, n) pair."""
    counts = [len(enumerate_solutions(n)) for n in hard_core]
    c = Counter(counts)
    distribution = dict(sorted(c.items()))
    worst = min(zip(counts, hard_core))  # (count, n)
    return distribution, worst


def prime_composite_split(hard_core: List[int]) -> Tuple[List[int], List[int]]:
    """Split hard core numbers into primes and composites based on factorisation length."""
    primes = [n for n in hard_core if len(factorise(n)) == 1]
    composites = [n for n in hard_core if len(factorise(n)) > 1]
    return primes, composites


def main() -> None:
    LIMIT = 20_000
    _validate_limit(LIMIT)

    print("=== residue classes mod 24 without a solution (exact criterion) ===")
    bad = residue_classes_without_solution(LIMIT)
    print("  ", {r: v[:6] for r, v in bad.items() if v} or "none")

    print("\n=== reduction (Theorem 7) ===")
    outside, fail_outside = outside_hard_core(LIMIT)
    print(f"   {len(outside)} values outside H; failures: {fail_outside}")

    H = hard_core_values(LIMIT)
    print(f"\n=== hard core H up to {LIMIT}: {len(H)} values ===")
    print("   first 30:", H[:30])

    print("\n=== repeated denominators (Corollary 9) ===")
    viol = repeated_denominator_violations(H)
    print(f"   solutions in H that are NOT strictly increasing: {viol[:10]} (count {len(viol)})")

    print("\n=== how many distinct solutions per hard-core n? ===")
    distribution, worst = solution_count_distribution(H)
    print("   distribution:", distribution)
    print(f"   minimum: {worst[0]} solutions, attained at n = {worst[1]}")

    print("\n=== prime vs composite in H ===")
    pr, co = prime_composite_split(H)
    print(f"   primes {len(pr)}, composite {len(co)}")


if __name__ == "__main__":
    main()
