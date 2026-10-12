"""Test suite for the Erdős–Straus investigation.

Every test uses exact integer arithmetic (fractions.Fraction / int), never
floating point.  Run with:   python tests/test_theorems.py
or:                         python -m pytest tests/ -q
"""
import os
import sys
from fractions import Fraction
from math import gcd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from es_theory import (es_solution, es_holds, enumerate_solutions,      # noqa: E402
                       pair_from_criterion, is_two_unit_fractions,
                       prime_divisors, divisors, factorise)
from es_sieve import (in_hard_core, es_via_j, es_via_k, minimal_k,      # noqa: E402
                      solution_count, hard_core_values, divisors_of_square,
                      divisors_of_factors, AB_of)


# --------------------------------------------------------------------------
def check_solution(n, x, y, z):
    """Exact verification of 4/n = 1/x + 1/y + 1/z with x <= y <= z."""
    assert x <= y <= z, (n, x, y, z)
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n), \
        (n, x, y, z)
    return True


# --------------------------------------------------------------------------
# Lemma 3 — the two-unit-fraction criterion
# --------------------------------------------------------------------------
def test_lemma3_criterion_matches_brute_force():
    """Criterion vs. direct search, for reduced a/b with b <= 260."""
    for b in range(1, 261):
        for a in range(1, 61):
            if gcd(a, b) != 1:
                continue
            found = None
            for y in range(1, 6 * b * a + 3):
                rem = Fraction(a, b) - Fraction(1, y)
                if rem <= 0:
                    continue          # 1/y must be strictly less than a/b
                if rem.numerator == 1:
                    found = (y, rem.denominator)
                    break
            assert bool(found) == is_two_unit_fractions(a, b), (a, b, found)
            if found:
                assert Fraction(1, found[0]) + Fraction(1, found[1]) == Fraction(a, b)


def test_lemma3_pair_formulas():
    for a in range(1, 40):
        for b in range(1, 60):
            if gcd(a, b) != 1:
                continue
            r = pair_from_criterion(a, b)
            if r is None:
                continue
            y, z = r
            assert y <= z
            assert Fraction(1, y) + Fraction(1, z) == Fraction(a, b), (a, b, r)


# --------------------------------------------------------------------------
# Lemma 1 and the search
# --------------------------------------------------------------------------
def test_window_bound_and_all_solutions_exact():
    for n in range(2, 300):
        for x, y, z in enumerate_solutions(n):
            assert n // 4 < x <= 3 * n // 4, (n, x)
            check_solution(n, x, y, z)


def test_es_holds_up_to_2000():
    missing = [n for n in range(2, 2001) if not es_holds(n)]
    assert missing == [], missing


def test_regression_known_witnesses():
    """n = 5, 13, 17, 25, 29, 37 were falsely reported unsolvable by a buggy
    first implementation of the criterion (see research/research_log.md)."""
    for n, (x, y, z) in {5: (2, 4, 20), 13: (5, 10, 130), 17: (5, 34, 170),
                         25: (7, 60, 2100), 29: (8, 78, 9048),
                         37: (10, 124, 22940)}.items():
        check_solution(n, x, y, z)


# --------------------------------------------------------------------------
# Theorem 7 — the four identities and the reduction to H
# --------------------------------------------------------------------------
def test_identity_I1_even():
    for n in range(2, 400, 2):
        check_solution(n, n // 2, n, n)


def test_identity_I2_three_mod_four():
    for n in range(3, 600, 4):
        check_solution(n, (n + 1) // 4, n * (n + 1) // 2, n * (n + 1) // 2)


def test_identity_I3_five_mod_eight():
    for n in range(5, 600, 8):
        x = (3 * n + 1) // 8
        check_solution(n, x, 2 * x, 2 * n * x)


def test_identity_I4_five_mod_twelve():
    for n in range(5, 600, 12):
        x = (n + 3) // 4
        check_solution(n, x, n * (x + 1) // 3, n * x * (x + 1) // 3)


def test_theorem7_reduction_holds():
    """ES(n) for every n <= 20000 outside the hard core."""
    for n in range(2, 20001):
        if not in_hard_core(n):
            assert es_holds(n), n


def test_hard_core_membership_and_first_values():
    for n in range(2, 2000):
        assert in_hard_core(n) == (
            n % 24 == 1 and all(p % 24 == 1 for p in prime_divisors(n))), n
    assert [n for n in range(2, 400) if in_hard_core(n)] == [
        73, 97, 193, 241, 313, 337]


# --------------------------------------------------------------------------
# Theorem 8 / Corollary 9 — no repeated denominators in H
# --------------------------------------------------------------------------
def test_theorem8_repeated_denominator_classification():
    for n in range(5, 1200, 4):
        has_p3 = any(p % 4 == 3 for p in prime_divisors(n))
        sols = enumerate_solutions(n)
        got_yz = any(y == z for _x, y, z in sols)
        got_xy = any(x == y for x, y, _z in sols)
        assert got_yz == has_p3, (n, has_p3, got_yz)
        assert got_xy == has_p3, (n, has_p3, got_xy)


def test_corollary9_hard_core_solutions_asymmetric():
    for n in hard_core_values(20000):
        for x, y, z in enumerate_solutions(n):
            assert x < y < z, (n, x, y, z)


# --------------------------------------------------------------------------
# Theorem 10 — sharp k = 3 criterion
# --------------------------------------------------------------------------
def test_theorem10_k3_criterion_exact():
    for n in hard_core_values(100000):
        has = any(p % 3 == 2 for p in factorise((n + 3) // 4))
        assert (es_via_k(n, 3) is not None) == has, n


# --------------------------------------------------------------------------
# Theorem 11 — u = 1 can never work
# --------------------------------------------------------------------------
def test_theorem11_no_k_divides_n2_plus_4():
    for n in hard_core_values(100000):
        for k in range(3, 73, 4):
            assert (n * n + 4) % k != 0, (n, k)
    for n in range(25, 600, 24):
        for p in factorise(n * n + 4):
            assert p % 4 == 1, (n, p)


# --------------------------------------------------------------------------
# Theorem 12 / Corollary 13 — closed forms
# --------------------------------------------------------------------------
def test_corollary13_1_divisor_of_n_plus_4():
    for n in range(5, 2500, 4):
        for d in divisors(n + 4):
            if d % 4 != 3 or d < 3 or factorise(n).get(d, 0):
                continue
            x = (n + d) // 4
            check_solution(n, x, n * (x + 1) // d, n * x * (x + 1) // d)


def test_corollary13_2_divisor_of_n_plus_1():
    for n in range(5, 2500, 4):
        for d in divisors(n + 1):
            if d % 4 != 3 or d < 3 or factorise(n).get(d, 0):
                continue
            x = (n + d) // 4
            check_solution(n, x, x * (n + 1) // d, n * x * (n + 1) // d)


def test_theorem12_f1_and_f3_witness_conditions():
    tested = 0
    for n in hard_core_values(20000):
        for d in range(3, 120, 4):
            if factorise(n).get(d, 0) or (n + d) % 4:
                continue
            x = (n + d) // 4
            if not (n // 4 < x <= 3 * n // 4):
                continue
            A, B = AB_of(n, (d + 1) // 4)
            assert A == d and B == n * x
            fx = factorise(x)
            for c in divisors_of_factors(fx):               # c | x, so c | x^2
                if c > x or (n + 4 * c) % d:
                    continue
                u = n * c
                assert (B * B) % u == 0 and u <= B and u % A == (-B) % A, \
                    (n, d, c)
                assert (B * B) // u % A == (-B) % A, (n, d, c)
                tested += 1
            fn = factorise(n)
            for c in divisors_of_factors({p: 2 * e for p, e in fn.items()}):  # c|n^2
                if c > n or (n + c) % d:
                    continue
                u = x * c
                assert (B * B) % u == 0 and u <= B and u % A == (-B) % A, \
                    (n, d, c)
                assert (B * B) // u % A == (-B) % A, (n, d, c)
                tested += 1
    assert tested > 100, tested


# --------------------------------------------------------------------------
# Lemma 5 and the sieve
# --------------------------------------------------------------------------
def test_sieve_agrees_with_generic_search():
    for n in hard_core_values(15000):
        ks = {4 * j - 1 for j in range(1, 41) if es_via_j(n, j) is not None}
        generic = {4 * x - n for x, _y, _z in enumerate_solutions(n)
                   if 4 * x - n <= 159}
        assert ks == generic, (n, sorted(ks), sorted(generic))


def test_witness_presence_matches_solver():
    for n in hard_core_values(8000):
        for j in range(1, 30):
            k = 4 * j - 1
            x = 6 * ((n - 1) // 24) + j
            if not (n // 4 < x <= 3 * n // 4):
                continue
            A, B = AB_of(n, j)
            wit = any(u <= B and u % A == (-B) % A
                      for u in divisors_of_square(factorise(B)))
            assert wit == (es_via_j(n, j) is not None), (n, k)


# --------------------------------------------------------------------------
# Specific instances quoted in main_results.md
# --------------------------------------------------------------------------
def test_resistant_instance_118801():
    n = 118801
    assert in_hard_core(n)
    assert minimal_k(n) == 59
    for k in range(3, 59, 4):
        assert es_via_k(n, k) is None, (n, k)
    check_solution(n, 29715, 59875704, 84724121160)     # k = 59
    check_solution(n, 29748, 18503256, 2198205316056)    # Corollary 13, d = 191


def test_resistant_instance_806521():
    n = 806521
    assert in_hard_core(n)
    assert minimal_k(n) == 59


def test_resistant_instance_246241():
    n = 246241
    assert in_hard_core(n)
    assert minimal_k(n) == 39
    for k in range(3, 39, 4):
        assert es_via_k(n, k) is None, (n, k)


def test_composite_hard_core_are_easier():
    for n in hard_core_values(60000):
        if len(factorise(n)) == 1:
            continue
        k = minimal_k(n, 16)
        assert k is not None and k <= 15, (n, factorise(n), k)


def test_minimum_number_of_solutions_in_hard_core():
    counts = {n: solution_count(n, 40) for n in hard_core_values(6000)}
    assert min(counts.values()) == 3
    assert [n for n, c in counts.items() if c == 3][:5] == [73, 193]


# --------------------------------------------------------------------------
def _run_all():
    fns = [(k, v) for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    failed = 0
    for name, fn in fns:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {name}: {e}")
        except Exception as e:                                    # noqa: BLE001
            failed += 1
            print(f"  ERROR {name}: {type(e).__name__}: {e}")
    print(f"\n{len(fns) - failed}/{len(fns)} tests passed")
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run_all() else 0)
