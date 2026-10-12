"""
Exact-arithmetic core for the Erdős–Straus conjecture.

    4/n = 1/x + 1/y + 1/z        (n >= 2,  x,y,z in Z_{>0})

All routines use exact integer arithmetic.  No floating point enters any
decision procedure.

The mathematical content is the *exact criterion* proved as Lemma 3 in
mathematics/proofs.md, together with the search-window bound n/4 < x <= 3n/4
(Lemma 1 there).
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Optional

Triple = tuple[int, int, int]


# ---------------------------------------------------------------------------
# Factorisation helpers (exact)
# ---------------------------------------------------------------------------

def factorise(m: int) -> dict[int, int]:
    """Prime factorisation {p: e} of m.  Exact trial division."""
    if m < 1:
        raise ValueError("m must be >= 1")
    f: dict[int, int] = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors(m: int) -> list[int]:
    """All positive divisors of m (sorted).  Exact."""
    ds = [1]
    for p, e in factorise(m).items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)


def divisors_of_square(b: int) -> list[int]:
    """All positive divisors of b^2.  Exact, via the factorisation of b."""
    ds = [1]
    for p, e in factorise(b).items():
        ds = [d * p ** i for d in ds for i in range(2 * e + 1)]
    return ds


def prime_divisors(n: int) -> list[int]:
    """Distinct prime divisors of n (sorted)."""
    return sorted(factorise(n))


# ---------------------------------------------------------------------------
# The exact criterion (Lemma 3)
# ---------------------------------------------------------------------------

def is_two_unit_fractions(a: int, b: int) -> bool:
    """Can the reduced fraction a/b be written as 1/y + 1/z?

    Criterion (mathematics/proofs.md, Lemma 3): for gcd(a,b) = 1,
        a/b = 1/y + 1/z   <=>   exists u | b^2 with u <= b and u = -b (mod a).
    """
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    if gcd(a, b) != 1:
        raise ValueError("a/b must be in lowest terms")
    if a == 1:
        return True
    target = (-b) % a
    for u in divisors_of_square(b):
        if u <= b and u % a == target:
            return True
    return False


def pair_from_criterion(a: int, b: int) -> Optional[tuple[int, int]]:
    """Return (y, z) with y <= z and 1/y + 1/z = a/b, or None.

    a/b must already be in lowest terms.
    """
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    if gcd(a, b) != 1:
        raise ValueError("a/b must be in lowest terms")
    if a == 1:
        return (2 * b, 2 * b)
    target = (-b) % a
    B2 = b * b
    for u in divisors_of_square(b):
        if u <= b and u % a == target:
            v = B2 // u
            y = (b + u) // a
            z = (b + v) // a
            assert a * y - b == u and a * z - b == v
            assert Fraction(1, y) + Fraction(1, z) == Fraction(a, b)
            return (y, z)
    return None


# ---------------------------------------------------------------------------
# Search for a witness of the Erdős–Straus conjecture
# ---------------------------------------------------------------------------

def candidates_x(n: int) -> range:
    """Admissible values of the smallest denominator x.

    Lemma 1: if 4/n = 1/x+1/y+1/z with x <= y <= z then n/4 < x <= 3n/4.
    """
    return range(n // 4 + 1, (3 * n) // 4 + 1)


def es_solution(n: int) -> Optional[Triple]:
    """Smallest-x witness for 4/n = 1/x+1/y+1/z with x <= y <= z, or None.

    By Lemma 1 the window scanned is complete, so None really means
    "no solution".
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    for x in candidates_x(n):
        num, den = 4 * x - n, n * x
        g = gcd(num, den)
        a, b = num // g, den // g
        if a <= 0:
            continue
        r = pair_from_criterion(a, b)
        if r is not None and r[0] >= x:
            x_, y_, z_ = x, r[0], r[1]
            assert 4 * x_ * y_ * z_ == n * (y_ * z_ + x_ * z_ + x_ * y_)
            return (x_, y_, z_)
    return None


def es_holds(n: int) -> bool:
    return es_solution(n) is not None


def enumerate_solutions(n: int) -> list[Triple]:
    """All (x, y, z) with x <= y <= z, 4/n = 1/x+1/y+1/z, x in the window."""
    out: list[Triple] = []
    for x in candidates_x(n):
        num, den = 4 * x - n, n * x
        g = gcd(num, den)
        a, b = num // g, den // g
        if a <= 0:
            continue
        target = (-b) % a
        B2 = b * b
        seen = set()
        for u in divisors_of_square(b):
            if u > b or u % a != target:
                continue
            v = B2 // u
            y, z = (b + u) // a, (b + v) // a
            if y < x or (y, z) in seen:
                continue
            seen.add((y, z))
            out.append((x, y, z))
    out.sort()
    return out
