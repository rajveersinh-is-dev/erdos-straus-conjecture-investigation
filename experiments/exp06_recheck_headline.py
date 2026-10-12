"""Independent re-verification of the headline numbers quoted in
FINAL_REPORT.md. This script deliberately shares no code with src/: it is a
second opinion, not a restatement.
"""
from fractions import Fraction
from math import isqrt

N = 3_000_000

# ---- 1. The two unit fractions for n = 118801 --------------------------
n = 118801
lhs = Fraction(4, n)
rhs1 = Fraction(1, 29715) + Fraction(1, 59875704) + Fraction(1, 84724121160)
rhs2 = Fraction(1, 29748) + Fraction(1, 18503256) + Fraction(1, 2198205316056)
print("identity 1 (k=59)  :", lhs == rhs1, lhs)
print("identity 2 (d=191) :", lhs == rhs2)
print("  k = 4*29715 - n  =", 4 * 29715 - n)
print("  d = 4*29748 - n  =", 4 * 29748 - n, "; d | n+1:", (n + 1) % (4 * 29748 - n) == 0)
print("  n / 191 =", n // 191, "; (n+1)/191 =", (n + 1) // 191)
print()

# ---- 2. Size of the hard core up to 3e6 --------------------------------
spf = [0] * (N + 1)
for p in range(2, isqrt(N) + 1):
    if spf[p] == 0:
        for j in range(p * p, N + 1, p):
            if spf[j] == 0:
                spf[j] = p
for j in range(2, N + 1):
    if spf[j] == 0:
        spf[j] = j


def in_hard_core(m):
    if m < 24 or m % 24 != 1:
        return False
    t = m
    while t > 1:
        p = spf[t]
        if p % 24 != 1:
            return False
        while t % p == 0:
            t //= p
    return True


count_congruent = sum(1 for m in range(1, N + 1, 24))
members = [m for m in range(1, N + 1, 24) if in_hard_core(m)]

print("|{n <= 3e6 : n = 1 mod 24}|      =", count_congruent)
print("|H cap [1, 3e6]|               =", len(members))
print("  share of the 1 mod 24 class   = %.2f %%" % (100 * len(members) / count_congruent))
print("  share of all integers         = %.2f %%" % (100 * len(members) / N))
print("  min member, max member        =", members[0], members[-1])
print("  73 in H:", 73 in members, "; 193 in H:", 193 in members)
print("  composites in H:", sum(1 for m in members if spf[m] != m))
print("  primes in H    :", sum(1 for m in members if spf[m] == m))