# Proof attempts, dead ends, and failed routes

Kept deliberately: a record of what *did not* work is part of the research
result and is more useful to a reader than a clean list of successes.

---

## A1. "Just prove a few more residue classes" — rejected

The standard way to publish progress on Erdős–Straus is to exhibit a new
polynomial identity covering a residue class not yet handled. We can *do* this
mechanically (Theorem 12 / Corollary 13 generate families automatically), but:

* it is low-value, and the literature already contains hundreds of such
  families (see `literature_review.md`, LR-4);
* it would not be new mathematics in any interesting sense.

**Decision:** contribute structural theorems instead, and label the families
honestly as classical in substance.

## A2. Counting solutions — abandoned as a target, not as a tool

Natural ambition: prove a lower bound such as "every `n ∈ H` has at least
`c·log log n` solutions". Observed behaviour (min number of full solutions over
`H ∩ [1, 20000]` = 6, at `n = 193`) gives no room for growth in the tested
range, and no argument for growth was found. Elsholtz–Tao (2011) and Jiang
(2026) own this territory.

**Decision:** report the *observed* minimum accurately and do not conjecture a
growth law we cannot support.

## A3. The `u = 1` shortcut — proved impossible

Wanted a one-line family. Taking the smallest possible witness `u = 1` in the
criterion requires `k | nx + 1`, which for `4x = n + k` reduces to
`k | n² + 4`. But every prime divisor of `n² + 4` is `≡ 1 (mod 4)` (because
`−4` a square forces `−1` a square), so no `k ≡ 3 (mod 4)` can divide it.

**Outcome:** became Theorem 11 — a genuine impossibility result, and a useful
statement that any successful construction must use a real prime factor.

## A4. Proving the conjecture for the hard core via the sieve — blocked

The plan was to show that for every `n ∈ H`, one of
`(n+3)/4, (n+7)/4, …, (n+23)/4` has a prime divisor in a prescribed residue
class modulo `4j−1`. Empirically the set `{k = 3, 7, 11, 15, 23}` covers
3348 of 3380 hard-core values up to 300000, and adding `k = 27, 31` covers
3378; two values (`118801`, `246241`) survive all `k ≤ 31`.

**Why blocked.** Each condition is a statement about the residue classes of the
prime divisors of a large, essentially arbitrary integer. Nothing elementary
forces such a prime divisor to exist; and proving existence is exactly the
Erdős–Straus conjecture in disguise. **This is the central obstacle and it is
recorded as such**, not hidden.

## A5. Attack through the two-denominator identities — proved impossible

A natural hope: in the hard core, maybe some `n` has a solution with `y = z`.
Computed: none do, for any `n ∈ H`. Proved as Theorem 8: for odd
`n ≡ 1 (mod 4)`, a solution with `y = z` exists iff `n` has a prime divisor
`≡ 3 (mod 4)`, and every prime divisor of `n ∈ H` is `≡ 1 (mod 24)`.

**Outcome:** became Corollary 9. Every solution in the hard core is strictly
`x < y < z`.

## A6. First criterion implementation — buggy, and the bug was informative

The initial implementation reported `n = 5, 13, 17, 25, 29, 37` as
counterexamples. These were false positives caused by `break`ing on the first
divisor of `b²` rather than on the first divisor satisfying the congruence.
Caught immediately by cross-checking `4/5 = 1/2 + 1/4 + 1/20`.

**Consequence for method:** every computational claim in the final project is
produced by a routine that is cross-checked against an independent one
(criterion vs. brute force; `k`-sieve vs. generic window search; closed forms
vs. criterion). This is recorded in `research_log.md`.

## A7. Lean formalisation — scope deliberately limited

A first attempt (`ESBasic.lean`, discarded) tried to prove the whole criterion
with `sorry` placeholders and a malformed term. Rejected: an unverified Lean
file with `sorry`s is worse than none, because it invites false confidence.

The replacement (`lean/ESCriterion.lean`) formalises **Lemma 3 only**, which is
the single statement the entire computational side depends on. Statements with
truncated `ℕ` subtraction are proved over `ℤ` and transferred. Whether the build
completed in the authoring environment is reported honestly in
`docs/reproducibility.md`; if not, the label is downgraded rather than asserted.

## A8. Numerical artefact: a miscounted statistic

An early experiment reported "minimum number of solutions over `H` = 3". On
inspection the routine was counting *distinct admissible `k` values*, not
solutions `(x, y, z)`. The correct figures are: minimum number of distinct `k`
over `H ∩ [1, 6000]` is 3 (`n = 73, 193`); minimum number of full solutions
over `H ∩ [1, 20000]` is 6 (`n = 193`). Both are now reported separately, and
the README does not quote the ambiguous figure.
