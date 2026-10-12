# Known results

A compact statement of the strongest prior results relevant to this project,
with pointers to where they are used. Full bibliographic detail and the
limitations of our search are in `literature_review.md`.

---

## K1 The Erdős–Straus conjecture

> For every `n ≥ 2`, `4/n` is a sum of three positive unit fractions.

Erdős & Straus (1948). **Open**, confirmed 2026-10-12.

Standard surrounding facts, all classical:

* The case `n` even: `4/n = 1/(n/2) + 1/n + 1/n`.
* If `d | n` and `ES(d)` then `ES(n)` — so it suffices to consider primes.
* The cases `n ≡ 3 (mod 4)` and `n ≡ 2 (mod 3)` are immediate.
* It suffices to consider `n ≡ 1 (mod 24)`. Our Theorem 7 sharpens the
  statement to: it suffices to consider `n ∈ H`, i.e. `n ≡ 1 (mod 24)` with
  all prime divisors `≡ 1 (mod 24)`.
* Computer verification up to `n ≤ 10^17` is reported in the literature; we do
  not reproduce it and do not rely on it.

## K2 The shape of the surviving difficulty

Prior work is concentrated on the *structure* of solutions:

* **Elsholtz & Tao (2011)** — asymptotics for `Σ_{p≤N} f(p)`, where `f(n)` is
  the number of solutions; introduce the Type I / Type II classification.
* **Lopez (2024)** — a congruence system conjectured to cover all primes; new
  solution types.
* **Bello-Hernández (2026)** — a divisor-based parametrisation, explicitly
  compared with Type I/II.
* **Jiang (2026)** — an exact counting identity expressing the counts as sums
  over divisors of `n²` in a single residue class modulo `e_n = 4n − p`;
  concentration results; `f_I = f_II = 0` for odd perfect squares.

**Impact on our claims.** Our Lemma 3 criterion is the same mathematical object
as the "divisors of `n²` in a residue class modulo `e_n`" appearing in Jiang's
identity, stated in a self-contained form. We therefore label Lemma 3 as
*known in substance, proved and formally verified here*, and we do not claim
to have introduced the divisor-criterion viewpoint.

## K3 Facts we use inside our own proofs

These are standard elementary number theory, stated here so the proofs are
self-contained:

* Every positive divisor of an odd integer whose prime divisors are all
  `≡ 1 (mod 4)` is `≡ 1 (mod 4)`.
* If `p` is an odd prime and `p | n² + 4`, then `p ≡ 1 (mod 4)`: `n² ≡ −4`
  makes `−1` a square mod `p` after dividing by `4`.
* `−1` is a quadratic residue mod an odd prime `p` iff `p ≡ 1 (mod 4)`.

## K4 What the literature does *not* appear to contain

Stated conservatively — this is an observation from a limited search, not a
proof of absence:

* A treatment of the hard core `H` defined by *all* prime divisors being
  `≡ 1 (mod 24)` (as opposed to only `n ≡ 1 (mod 24)`), together with the
  corollary that no solution in `H` has a repeated denominator.
* An explicit statement that the trivial witness `u = 1` in the divisor
  criterion can never apply (Theorem 11).
* A catalogue of "most resistant" instances of `H`, i.e. the integers of `H`
  for which the smallest admissible `k = 4x − n` is largest. We report
  `μ(118801) = μ(806521) = 59` as the record on `H ∩ [1, 3·10^6]`.

These may well be known to someone; we could not verify otherwise
(`literature_review.md`, LR-6).
