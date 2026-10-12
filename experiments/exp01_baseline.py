"""exp01 — baseline: does the exact criterion find a solution for every n?

Tests Lemma 1 + Lemma 3 end-to-end and prints witnesses for the small values
that a buggy first implementation of the criterion misreported as unsolvable.
"""
import os
import sys

from es_theory import es_solution, es_holds, enumerate_solutions  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

LIMIT = 2000
missing = [n for n in range(2, LIMIT + 1) if not es_holds(n)]
print(f"n in [2, {LIMIT}] with no solution found: {missing}")

print("\nFirst 40 values:")
for n in range(2, 42):
    s = es_solution(n)
    print(f"  n={n:>3}  4/n = 1/{s[0]} + 1/{s[1]} + 1/{s[2]}" if s else f"  n={n:>3}  NONE")

print("\nRegression values (first buggy implementation reported NONE):")
for n in [5, 13, 17, 25, 29, 37]:
    sols = enumerate_solutions(n)
    print(f"  n={n}: {len(sols)} solutions, smallest-x one = {sols[0]}")

print("\nTotal number of solutions for n <= 200:",
      sum(len(enumerate_solutions(n)) for n in range(2, 201)))
