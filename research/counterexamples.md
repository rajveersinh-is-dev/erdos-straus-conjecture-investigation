# Counterexamples and near-misses

A running list of things that *almost* worked, and of the checks that guard
against false counterexamples.

---

## C1 No counterexample to Erdős–Straus was found

On the ranges actually computed here (exact integer arithmetic, criterion of
Lemma 3):

| range | quantity checked | result |
|---|---|---|
| `2 ≤ n ≤ 2000` | full search over `n/4 < x ≤ 3n/4` | no counterexample |
| `2 ≤ n ≤ 20000` | all `n ∉ H` | no counterexample (Theorem 7) |
| `H ∩ [1, 20000]` (273 values) | full search; asymmetry | no counterexample |
| `H ∩ [1, 300000]` (3380 values) | sieve for `k ≤ 31`; Theorems 10, 11 | no counterexample |
| `H ∩ [1, 600000]` (6467 values) | obstruction (O1)–(O3) | 799 survive all three |
| `H ∩ [1, 3·10^6]` (29298 values) | sieve for `k ≤ 255` | **0** values without a solution |

The last line is the strongest verified statement made in this repository:
every hard-core integer up to three million has a solution with `k ≤ 255`.
That is a **COMPUTATIONALLY VERIFIED** claim about a finite range, not a
theorem about all `n`.

## C2 A false counterexample, and how it was caught

An early implementation of the criterion reported

        n = 5, 13, 17, 25, 29, 37     (claimed: no solution)

as counterexamples. **All six are false.** For example
`4/5 = 1/2 + 1/4 + 1/20` and `4/13 = 1/5 + 1/10 + 1/130`.

Cause: the routine enumerated divisors of `b²` and stopped at the *first*
divisor encountered, instead of the first divisor satisfying the congruence
condition. The guard now in place is `test_regression_known_witnesses` in
`tests/test_theorems.py`, which pins the six correct witnesses.

**Lesson.** A "counterexample" to a widely believed conjecture is far more
likely to be a bug than a discovery. Every computational claim in this project
is now cross-checked by a second, independently written routine.

## C3 Near-misses in the hard core

Instances of `H` on which the small-`k` sieve fails longest. These are *not*
counterexamples; they are where the conjecture is least comfortable, and they
indicate which routes are weakest.

| `n` | smallest admissible `k = μ(n)` | first solution |
|---:|---:|---|
| `73` | 7 | `4/73 = 1/19 + 1/438 + 1/26862` |
| `193` | 7 | see `experiments/exp02_structure.py` |
| `246241` | 39 | `4/246241 = 1/61570 + 1/416639772 + 1/5806362780` |
| `118801` | 59 | `4/118801 = 1/29715 + 1/59875704 + 1/84724121160` |
| `806521` | 59 | — |

On `H ∩ [1, 300000]`, the set `{k = 3, 7, 11, 15, 23}` covers 3348 of 3380
values (99.05 %); adding `k = 27` and `k = 31` covers 3378. The two survivors
(`118801`, `246241`) are the hardest instances found at that scale.

**Observation (not a theorem).** Every one of the hardest instances found is a
*prime* `≡ 1 (mod 24)`. Composite members of `H` need `k ≤ 15` throughout
`H ∩ [1, 3·10^6]`. Why primes are harder is not understood here.

## C4 Sanity checks on the identities

Each of the four reduction identities was checked term by term for all
`n` in its class up to 600, and again for all `n` up to 20000 via the generic
search (`test_theorem7_reduction_holds`). Examples:

* `n = 4`: `4/4 = 1/2 + 1/4 + 1/4` (identity I1).
* `n = 7`: `4/7 = 1/2 + 1/28 + 1/28` (identity I2; note `y = z`, impossible in `H`).
* `n = 5`: `4/5 = 1/2 + 1/4 + 1/20` (identity I4 with `x = 2`).
* `n = 13`: `4/13 = 1/5 + 1/10 + 1/130` (Corollary 13 with `d = 7 | n+1`).

`n = 7` is worth noting: it has a solution with `y = z`, which Theorem 8
predicts, because `7` has the prime divisor `7 ≡ 3 (mod 4)`.
