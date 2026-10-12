# Research journal

Running record of decisions, dead ends, and changes of strategy.

---

## Session 1 — setup

**Environment.** Windows; Python 3.14.6; `sympy`, `networkx`; Lean
`leanprover/lean4:v4.35.0-rc4` with `lake` 5.0.0; **no LaTeX toolchain**
(`pdflatex` absent) — this is why the paper is supplied as both
`paper/main.tex` (source, not compiled here) and `paper/main.md`. Git 2.53,
`gh` 2.96 authenticated as `rajveersinh-is-dev`.

**Repository.** `erdos-straus-conjecture-investigation`, created public, pushed
to `main`.

## Session 1 — problem selection

Considered: Erdős–Straus, Alon–Jaeger–Tarsi, Beck–Fiala, Lonely Runner,
sunflowers/Erdős–Rado, Caccetta–Häggkvist, Zaremba. Rejected each with a
reason (`research/problem_selection.md`). Selected Erdős–Straus, with the
explicit understanding that the full conjecture is out of scope.

**Literature check.** Confirmed open via Wikipedia + arXiv + OpenAlex on
2026-10-12. Discovered a dense modern literature on the *structure* of the
solutions (Elsholtz–Tao 2011; Lopez 2024; Bello-Hernández 2026; Jiang 2026),
which forced a decision recorded below.

## Session 1 — the criterion, and a bug worth recording

Goal: an exact test for `a/b = 1/y + 1/z`. Starting from
`(ay−b)(az−b) = b²`, I concluded that a solution corresponds to a factorisation
`b² = uv` with `u ≡ v ≡ −b (mod a)`, and that it suffices to look for a divisor
`u | b²` with `u ≤ b` and `u ≡ −b (mod a)` (then `v ≡ −b (mod a)` follows from
`gcd(a,b) = 1`). This is Lemma 3.

**Bug.** The first implementation enumerated divisors of `b²` and `break`ed on
the *first* divisor found, regardless of the congruence. It reported
`n = 5, 13, 17, 25, 29, 37` as counterexamples — they are not; e.g.
`4/5 = 1/2 + 1/4 + 1/20`. Fixed; a regression test
(`test_regression_known_witnesses`) now pins the correct witnesses down so the
error cannot recur silently.

**Lesson applied.** After this, every computational claim in the project is
checked against an *independent* method (criterion vs. brute-force; sieve vs.
generic search; closed forms vs. criterion), not just produced by one routine.

## Session 1 — the hard core

Discovered empirically that all residue classes mod 24 other than `1` are
trivial, and that within `1 mod 24` the survivors are those whose prime factors
are all `≡ 1 (mod 24)`. Proved this as Theorem 7 (four identities + descent).
This is the classical reduction, but pinning it down as a set `H` made the rest
of the work concrete.

## Session 1 — structural findings in `H`

* **No repeated denominators.** Theorem 8 / Corollary 9. Verified on all
  solutions for all `n ∈ H` up to 20000.
* **Composite vs prime.** Over `H ∩ [1, 3·10^6]`: 2315 composite members, all
  with `μ ≤ 15`; 26983 prime members, reaching `μ = 59`. A striking asymmetry.
  *(These two figures were wrong at first — 2288 / 27010 — because
  `len(factorise(n)) == 1` was used as a primality test and also matches prime
  powers `p^e`, `e ≥ 2`. See `research/proof_attempts.md` A9. The qualitative
  conclusion is unaffected; the numbers are corrected everywhere.)*
* **The `k = 3` criterion is exact**, in both directions (Theorem 10).
* **`u = 1` never works** (Theorem 11) — proved, not guessed.

## Session 1 — resistant instances

`n = 118801` and `n = 806521` need `k = 59`; nothing smaller works. Explicit
first solutions recorded in the README. The closed forms of Corollary 13 still
kill `118801` (via `d = 191 | (n+1)`), which is a useful demonstration that
closed forms and the sieve are complementary.

## Session 1 — incident

The working directory `C:\Users\davea\Downloads\proj2\o` was **externally
replaced** mid-session by an unrelated concurrent project; local files were
lost. Nothing of that project was touched. The work was rebuilt from scratch in
a separate directory and the GitHub repository (created earlier, never pushed to
before the incident) was used as the destination. Full record:
`research/incident.md`. All numbers quoted in the README and paper were
re-derived after the rebuild, not carried over.

## Session 2 — consolidation

* Rewrote `es_theory.py` with an O(τ(b²)) divisor enumeration (the first
  version was O(τ(b)²) and made the test suite unusably slow).
* Corrected a mis-statement: an earlier experiment counted *distinct `k`
  values*, not *solutions*. The minimum over `H ∩ [1, 20000]` of the number of
  distinct admissible `k` is 3 (at `n = 73, 193`); the minimum number of full
  solutions `(x,y,z)` is 6 (at `n = 193`). Both are now stated separately.
* Fixed Lemma 4's statement: it gives a *necessary and sufficient* condition
  for `4/n = 1/x + 1/y + 1/z` with `y, z ≥ 1`; the extra requirement `x ≤ y`
  is verified separately at each point of use (Remark 4.1). The earlier wording
  silently assumed it.
* Rewrote the closing argument of Theorem 8, which had a tangle of case
  analysis; it is now two lines.

## Session 2 — the Lean file finally compiles

The formalisation of Lemma 3 went through three real type errors, each of which
was a genuine mistake rather than a toolchain quirk:

1. `h.mul_right t` on `Dvd.dvd a (b * c)` in `dvd_of_dvd_mul_of_bezout` —
   the orientation of the divisibility product lemma was backwards.
2. In `witness_gives_solution`, showing `v > 0` from `b² = u*v` with `u > 0`.
   The first attempt compared `v * u ≤ 0 * u`, which Lean normalises to
   `u * v ≤ u * 0`; the fix is to compare `u * v ≤ u * 0`, rewrite it to
   `u * v ≤ 0` via `mul_zero`, and push it through `hv`.
3. `rw [← hv]` was used where `rw [hv]` was needed (rewriting *into* the goal
   vs. *into* the hypothesis).

Also a linter warning about an unused hypothesis `hz` in
`solution_gives_witness`, silenced by renaming it `_hz` — no proof content was
touched. None of these was papered over with `sorry`.

The blocking obstacle before this was not the mathematics but the
`lake-manifest.json`/`lakefile.toml` mismatch, which silently rebuilt Mathlib
from source (3137 modules). Once that finished, each iteration on the file took
about half a minute.

**Decision on scope, restated.** Only Lemma 3 is formalised. Theorems 7–14 stay
`PROVED HERE` on the strength of the written proofs plus the test suite. The
Lean file does *not* verify that `src/es_theory.py` transcribes the criterion
faithfully; that remains the job of `tests/test_theorems.py`.

## Open threads (not pursued)

* **Proving `μ` is bounded on `H`.** Would be a genuine new result; the
  natural route needs control of prime divisors of consecutive linear functions
  of `n` in prescribed residue classes, which is out of reach here.
* **Proving composites in `H` always have `μ ≤ 15`.** Verified on
  `H ∩ [1, 3·10^6]`; a proof would be new and is listed as an open question in
  the README.
* **Whether the obstruction (O1)–(O4) can be strengthened to a provably
  unsatisfiable system.** This is the most promising route to a real advance.
