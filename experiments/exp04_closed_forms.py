"""exp04 - closed-form families F1'/F3' (Theorem 12, Corollary 13) and their
coverage of the hard core.

F1' : d = 3 mod 4, gcd(d,n)=1, d | n + 4c, c | x^2, 1 <= c <= x,  x=(n+d)/4
F3' : d = 3 mod 4, gcd(d,n)=1, d | n + c,  c | n^2, 1 <= c <= n

The c = 1 instances are the closed-form identities of Corollary 13.
"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from es_sieve import (hard_core_values, factorise, divisors_of_factors)  # noqa: E402

LIMIT = 300_000


def F1(n, d, c):
    """The solution produced by family F1', or None."""
    if (d + 1) % 4 or d < 3 or n % 4 != 1 or factorise(n).get(d, 0):
        return None
    if (n + d) % 4:
        return None
    x = (n + d) // 4
    if c > x or (n + 4 * c) % d:
        return None
    fx = factorise(x)
    if any(fx.get(p, 0) * 2 < e for p, e in factorise(c).items()):
        return None                     # need c | x^2
    y = n * (x + c) // d
    z = (n * x + n * x * x // c) // d
    return (x, y, z)


def F3(n, d, c):
    """The solution produced by family F3', or None."""
    if (d + 1) % 4 or d < 3 or n % 4 != 1 or factorise(n).get(d, 0):
        return None
    if (n + c) % d or c > n:
        return None
    fn = factorise(n)
    if any(fn.get(p, 0) * 2 < e for p, e in factorise(c).items()):
        return None                     # need c | n^2
    x = (n + d) // 4
    y = (n * x + x * c) // d
    z = (n * x + n * n * x // c) // d
    return (x, y, z)


def verify(t, n):
    x, y, z = t
    assert x <= y <= z, (n, t)
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n), (n, t)


print("### 1. exhaustive verification of the closed forms, n = 1 mod 4, n <= 6000")
tested = 0
for n in range(5, 6000, 4):
    for d in divisors_of_factors(factorise(n + 4)):
        if d % 4 != 3 or d < 3 or factorise(n).get(d, 0):
            continue
        verify(F1(n, d, 1), n)
        tested += 1
    for d in divisors_of_factors(factorise(n + 1)):
        if d % 4 != 3 or d < 3 or factorise(n).get(d, 0):
            continue
        verify(F3(n, d, 1), n)
        tested += 1
print(f"   closed-form instances verified exactly: {tested}")

print("\n### 2. worked examples")
for n, d, c, fam in [(5, 3, 1, "F1"), (13, 7, 1, "F3"), (17, 3, 1, "F1"),
                     (241, 7, 1, "F1"), (118801, 191, 1, "F3")]:
    t = F1(n, d, c) if fam == "F1" else F3(n, d, c)
    if t:
        verify(t, n)
        print(f"   n={n:>7}  {fam} with d={d}:  4/n = 1/{t[0]} + 1/{t[1]} + 1/{t[2]}")

print("\n### 3. coverage of the hard core by the closed forms")
H = hard_core_values(LIMIT)


def covered_F1(n):
    for d in divisors_of_factors(factorise(n + 4)):
        if d % 4 == 3 and F1(n, d, 1):
            return True
    if (n + 7) % 4 == 0:
        x1 = (n + 7) // 4
        if x1 % 2 == 0:                       # c = 2 divides x^2
            for d in divisors_of_factors(factorise(n + 8)):
                if d % 4 == 3 and F1(n, d, 2):
                    return True
        if x1 % 3 == 0:                       # c = 3 divides x^2
            for d in divisors_of_factors(factorise(n + 12)):
                if d % 4 == 3 and F1(n, d, 3):
                    return True
    return False


def covered_F3(n):
    fn = factorise(n)
    for c in divisors_of_factors(fn):
        for d in divisors_of_factors(factorise(n + c)):
            if d % 4 == 3 and F3(n, d, c):
                return True
    for c in divisors_of_factors({p: 2 * e for p, e in fn.items()}):
        if c > n:
            continue
        for d in divisors_of_factors(factorise(n + c)):
            if d % 4 == 3 and F3(n, d, c):
                return True
    return False


a = sum(covered_F1(n) for n in H)
b = sum(covered_F3(n) for n in H)
u = sum(covered_F1(n) or covered_F3(n) for n in H)
print(f"   H up to {LIMIT}: {len(H)}")
print(f"   F1' covers {a}/{len(H)} = {a/len(H):.4f}")
print(f"   F3' covers {b}/{len(H)} = {b/len(H):.4f}")
print(f"   union     {u}/{len(H)} = {u/len(H):.4f}")
res = [n for n in H if not (covered_F1(n) or covered_F3(n))]
print(f"   resistant to both: {len(res)};  first 20: {res[:20]}")
