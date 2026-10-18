"""
Exact-arithmetic *k-sieve* for the Erdős–Straus conjecture.

Setting.  A solution is  x <= y <= z  with  4/n = 1/x + 1/y + 1/z.  Put

        k = 4x - n  (> 0, and k <= 2n by Lemma 1).

Then

        1/y + 1/z = (4x - n)/(n x) = 4k / ( n (n + k) ).                   (S)

For n = 1 mod 24 write n = 24m + 1; with k = 4j - 1 we get n + k = 4(6m + j)
and x = 6m + j, so (S) becomes

        1/y + 1/z = (4j - 1) / ( n (6m + j) ).

Let  G = gcd(4j-1, n(6m+j)),  A = (4j-1)/G,  B = n(6m+j)/G  (so gcd(A,B)=1).
Lemma 3 (proofs.md) then gives the exact criterion

        4/n = 1/x + 1/y + 1/z   <=>   exists u | B^2, u <= B, u = -B (mod A).  (T)

Everything here is exact integer arithmetic.
"""

from __future__ import annotations

from math import gcd, isqrt


__all__ = ["sieve_primes", "factorise", "divisors_of_square", "divisors",
           "in_hard_core", "es_via_j", "es_via_k", "minimal_k",
           "solution_count", "hard_core_values", "AB_of", "is_prime",
           "is_prime_power"]


def sieve_primes(limit: int) -> list[int]:
    """All primes <= limit (bytearray Eratosthenes, exact)."""
    s = bytearray([1]) * (limit + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if s[i]:
            s[i * i:: i] = bytearray(len(s[i * i:: i]))
    return [i for i in range(limit + 1) if s[i]]


def factorise(n: int) -> dict[int, int]:
    """Prime factorisation {p: e} of n.  Exact trial division."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return {}
    f: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_of_square(f: dict[int, int]) -> list[int]:
    """All divisors of b^2 given the factorisation f of b."""
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(2 * e + 1)]
    return ds


def divisors_of_factors(f: dict[int, int]) -> list[int]:
    """All divisors of the integer whose factorisation is f."""
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)


def divisors(m: int) -> list[int]:
    """All positive divisors of the integer m."""
    return divisors_of_factors(factorise(m))


def in_hard_core(n: int) -> bool:
    """n = 1 mod 24 and every prime divisor of n is = 1 mod 24."""
    if n < 2 or n % 24 != 1:
        return False
    return all(p % 24 == 1 for p in factorise(n))


def is_prime(n: int) -> bool:
    """n is prime.

    Do NOT write ``len(factorise(n)) == 1``: that is true for every prime
    *power* p^e with e >= 2 as well, and misclassifying those silently
    corrupted a reported statistic in an earlier version of exp05 (see
    research/proof_attempts.md, A9).
    """
    if n < 2:
        return False
    f = factorise(n)
    return len(f) == 1 and n in f


def is_prime_power(n: int) -> bool:
    """n = p^e with p prime and e >= 2 (so: composite, one distinct prime)."""
    if n < 4:
        return False
    f = factorise(n)
    return len(f) == 1 and n not in f


def AB_of(n: int, j: int) -> tuple[int, int]:
    """(A, B) of Definition D.4 for k = 4j - 1 and n = 24m + 1."""
    m = (n - 1) // 24
    k = 4 * j - 1
    G = gcd(k, n * (6 * m + j))
    return k // G, n * (6 * m + j) // G


def es_via_j(n: int, j: int):
    """Exact test of (T) for k = 4j-1.  Returns (y, z) or None."""
    if n % 24 != 1:
        return None
    m = (n - 1) // 24
    x = 6 * m + j
    if not (n // 4 < x <= 3 * n // 4):
        return None
    A, B = AB_of(n, j)
    if A == 1:
        return (2 * B, 2 * B)
    B2 = B * B
    tgt = (-B) % A
    for u in divisors_of_square(factorise(B)):
        if u <= B and u % A == tgt:
            v = B2 // u
            return ((B + u) // A, (B + v) // A)
    return None


def es_via_k(n: int, k: int):
    """Exact test of (T) for k = 4j - 1 (k must be = 3 mod 4)."""
    if (k + 1) % 4 != 0:
        raise ValueError("k must be congruent to 3 mod 4")
    return es_via_j(n, (k + 1) // 4)


def minimal_k(n: int, kmax: int = 64):
    """Smallest k = 3 mod 4 admitting a solution, or None below 4*kmax-1."""
    for j in range(1, kmax):
        if es_via_j(n, j) is not None:
            return 4 * j - 1
    return None


def solution_count(n: int, kmax: int = 64) -> int:
    """Number of distinct x-values yielding a solution with x <= y <= z."""
    c = 0
    m = (n - 1) // 24
    for j in range(1, kmax):
        r = es_via_j(n, j)
        if r is not None and r[0] >= 6 * m + j:
            c += 1
    return c


def hard_core_values(limit: int) -> list[int]:
    """All hard-core integers <= limit."""
    return [n for n in range(25, limit + 1, 24) if in_hard_core(n)]
