# Changelog

All notable changes to this repository. Entries record *what was actually done*.

## [Unreleased] — session 1–2

### Mathematics
- **math**: derived the exact two-unit-fraction criterion (Lemma 3) and proved
  it in both directions.
- **math**: proved the reduction of the Erdős–Straus conjecture to the hard core
  `H = {n ≡ 1 (mod 24) : all prime divisors ≡ 1 (mod 24)}` (Theorem 6/7),
  from four explicit identities plus a descent lemma.
- **math**: proved the complete classification of solutions with a repeated
  denominator (Theorem 8), and deduced that every solution in `H` is
  asymmetric (Corollary 9).
- **math**: proved the sharp `k = 3` criterion for `n ∈ H` (Theorem 10).
- **math**: proved that the trivial witness `u = 1` never works (Theorem 11).
- **math**: proved two closed-form solution families `F1'`/`F3'` and their
  `c = 1` instances (Theorem 12, Corollary 13).
- **math**: proved an obstruction theorem giving four necessary conditions on a
  counterexample in `H` (Theorem 14).

### Implementation
- **src**: `es_theory.py` — search window (Lemma 1) and the divisor criterion
  (Lemma 3), exact integer arithmetic.
- **src**: `es_sieve.py` — the `k`-parametrisation, exact sieve, hard-core
  predicates.
- Fixed an `O(τ(b)²)` divisor enumeration to `O(τ(b²))` after the first test
  run became unusably slow.

### Tests
- **test**: 25 tests, all passing, all exact-rational.
- Includes a regression test for six values (`n = 5, 13, 17, 25, 29, 37`) that a
  buggy early implementation of the criterion falsely reported as
  counterexamples.
- Cross-checks each computational routine against an independently written one
  (criterion vs. brute force; sieve vs. generic search; closed forms vs.
  criterion).

### Experiments
- **experiment**: `exp01` baseline; `exp02` structure and the reduction;
  `exp03` `k`-census plus checks of Theorems 10 and 11; `exp04` closed forms;
  `exp05` obstruction strength and `μ` records up to `3·10^6`.
- Headline computed results: no hard-core integer up to `3·10^6` lacks a
  solution with `k ≤ 255`; `μ` reaches 59 (at `n = 118801, 806521`); composite
  members of `H` never exceed `μ = 15`.

### Documentation
- **research**: problem selection with stated criteria; literature review with
  verified citations and an explicit statement of what could not be verified;
  research journal; proof attempts and dead ends; known results;
  counterexamples and near-misses; evidence-label definitions.
- **research**: `incident.md` — record of the loss of the first working
  directory to an external workspace reset, and of the rebuild.
- **docs**: reproducibility instructions with expected outputs.
- **paper**: `paper/main.md` and `paper/main.tex`.

### Formalisation
- **lean**: `ESCriterion.lean` formalising Lemma 3. Build status recorded in
  `lean/BUILD_STATUS.md`.

### Known not-done
- The Erdős–Straus conjecture is **not** proved or disproved.
- `paper/main.tex` was **not** compiled (no LaTeX toolchain available).
- No bound on `μ(n)` proved.
