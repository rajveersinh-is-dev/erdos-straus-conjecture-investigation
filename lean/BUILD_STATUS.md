# Build status of the Lean formalisation

This file records **what was actually executed** in the authoring environment.
It is written to be falsifiable: if any command below did not run, the label
attached to it is not claimed.

Date of the run: **2026-10-12**. Platform: Windows (win32).

## 1. What is formalised

`ESCriterion.lean` formalises **Lemma 3 of `mathematics/proofs.md` only**, in the
two directions that the Python code depends on:

* `ES.solution_gives_witness` — if `a/b = 1/y + 1/z` with `y ≤ z` then
  `u := a*y − b` satisfies `0 < u`, `u ∣ b²`, `u ≤ b`, `a ∣ b + u`;
* `ES.witness_gives_solution` — conversely, from such a `u` one recovers
  `y ≤ z`, `0 < y`, `0 < z` with `b(y+z) = a*y*z`;
* `ES.criterion_iff` — the equivalence as a single theorem, in the form used in
  `src/es_theory.py`.

Two structural lemmas are also formalised: `ES.factorisation`
(`(a*y − b)(a*z − b) = b²`) and `ES.dvd_of_dvd_mul_of_bezout` (cancellation of a
coprime factor, entered through Bezout's identity rather than `Nat.gcd`).

**Not** formalised: the reduction to `H` (Theorem 7), the closed forms
(Corollary 13), the obstruction theorem (Theorem 14), or anything about the
Erdős–Straus conjecture. A `FORMALLY VERIFIED` label is claimed for Lemma 3 and
for nothing else.

## 2. The commands that were run

Toolchain: `leanprover/lean4:v4.35.0-rc4` (from `lean-toolchain`).
`lake` version: `5.0.0-src+c29b6dd`. Dependency: `mathlib`, `git#master`
(lake manifest `lean/lake-manifest.json`). Mathlib was fetched from
source. `lake exe cache get` was attempted, but the fetched oleans did not match
the revision pinned in `lake-manifest.json`, so `lake` fell back to compiling
Mathlib from source: the build log ends with `Build completed successfully
(3138 jobs)`, i.e. 3137 Mathlib modules plus `ESCriterion`. Subsequent
single-file checks take ≈ 30 s.

```text
$ cd lean
$ lake build
⚠ [3137/3138] Built ESCriterion (6.4s)
warning: ESCriterion.lean: imports `Mathlib.Data.Int.GCD` from package `mathlib`,
  which is designed for use with the module system; consider adding `module` to
  the start of this file
warning: ESCriterion.lean: imports `Mathlib.Tactic` from package `mathlib`,
  which is designed for use with the module system; consider adding `module` to
  the start of this file
Build completed successfully (3138 jobs).
$ echo $?
0
```

```text
$ lake env lean ESCriterion.lean
$ echo $?
0
```

The second command produced **no output at all**: no errors and no warnings from
the file itself. (The two `warning:` lines above are emitted by `lake build`,
not by `lean`, and concern the `import` style in a non-module file; they are not
statements about the proof.)

## 3. No `sorry`, no added axioms

`grep -n 'sorry\|axiom\|native_decide' ESCriterion.lean` returns nothing.

The stronger, kernel-level check is the axiom audit in `AxiomAudit.lean`:

```text
$ lake env lean AxiomAudit.lean
'ES.factorisation' depends on axioms: [propext, Quot.sound]
'ES.dvd_of_dvd_mul_of_bezout' depends on axioms: [propext]
'ES.solution_gives_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
'ES.witness_gives_solution' depends on axioms: [propext, Classical.choice, Quot.sound]
'ES.criterion_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
```

These are the three axioms Lean's own standard library is built on and that
every Mathlib theorem depends on. **`sorryAx` does not appear**, which is the
precise sense in which the file contains no unfinished proof.

## 4. Relation to the Python implementation

`src/es_theory.py` implements exactly this criterion over `int`. The Lean proof
establishes the mathematical statement; it does *not* establish that the Python
transcription of it is correct. That link is covered by the test suite
(`tests/test_theorems.py`, 25/25 passing), which is a different kind of evidence
and is labelled separately.

## 5. Honest limitations

* Coverage is one lemma out of the whole project. The interesting theorems —
  the hard-core localisation (Theorem 7), the obstruction theorem (Theorem 14)
  — are **not** machine-checked, only proved on paper.
* The development was checked against Lean 4.35.0-rc4. The exact commit of
  `mathlib` used is the one recorded in `lake-manifest.json`; results on other
  revisions are not claimed.
* A successful build here says nothing about the correctness of the proofs in
  `mathematics/proofs.md` that were not formalised.