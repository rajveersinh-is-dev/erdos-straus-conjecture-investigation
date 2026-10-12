# Final report

**Project.** An autonomous mathematical investigation of the Erdős–Straus
conjecture.

**Repository.** <https://github.com/rajveersinh-is-dev/erdos-straus-conjecture-investigation>
(public, default branch `main`).

**Date of this report.** 2026-10-12.

**Verdict.** **C — RIGOROUS PARTIAL RESULT** (see §9 for the reasoning, and for
why B was not awarded).

---

## 1. The problem, and why this one

The Erdős–Straus conjecture (1948): for every integer `n ≥ 2` there are positive
integers `x, y, z` with `4/n = 1/x + 1/y + 1/z`. Confirmed still open on
2026-10-12 (`research/literature_review.md`, LR-1).

Several candidate open problems were considered and rejected with recorded
reasons in `research/problem_selection.md`: Alon–Jaeger–Tarsi (the AJT
conjecture is a spin-off whose decisive content is a finite-field polynomial
non-vanishing statement with no known point of entry), Beck–Fiala (the
conjecture has been *disproved*; the remaining question is a hard quantitative
one), the Lonely Runner conjecture (effectively the Erdős–Straus conjecture
repackaged, with a decades-long literature and no local handle), sunflowers /
Erdős–Rado (already resolved for `r = 3`), Caccetta–Häggkvist (known false for
small parameters, and the surviving cases need genuinely new input), Zaremba's
conjecture (the interesting content is about `n`, not the numerators).

Erdős–Straus was selected because there is a decisive first reduction — fix the
smallest denominator `x`, put `k = 4x − n`, and the remaining question is a
*two*-unit-fraction equation, i.e. a divisor problem — and because that
reduction can be carried to a genuine, non-trivial and precisely statable
endpoint. The ambition was scoped explicitly and in advance: **do not attempt a
full solution; produce a sharp localisation, structural theorems, an
obstruction theorem, and exact computation.** That decision is recorded in
`research/problem_selection.md` and was not revised once results came in.

## 2. Method

The method was insight-driven at every step:

1. **Reduce, do not search.** The first move was to parametrise by the smallest
   denominator, which turns the three-variable problem into a sequence of
   two-variable problems. This is classical, and it was used as a platform
   rather than as the contribution.
2. **Solve the two-variable problem exactly.** A closed-form criterion
   (Lemma 3) reduces `a/b = 1/y + 1/z` to factoring `b²`. This is the single
   step that makes everything else cheap.
3. **Look for obstructions, not constructions.** Once a cheap criterion existed,
   the productive question was not "can I find a solution" but "what must be
   true of `n` if *no* solution exists". That reframing produced Theorem 11 and
   Theorem 14, which are the two results in the project with real content
   beyond bookkeeping.
4. **Only then compute.** The experiments exist to test and delimit the
   theorems; they are not the source of any claim about an infinite set.

No brute-force search was used as evidence for a universal statement anywhere.

## 3. What was proved

Complete proofs of all of the following are in `mathematics/proofs.md`;
statements with labels are in `mathematics/main_results.md`.

| # | Statement | Evidence | Novelty |
|---|---|---|---|
| Lemma 1 | search window `n/4 < x ≤ 3n/4` | PROVED HERE | known |
| Lemma 2 | `k`-parametrisation `4x − n = k`, `n = 24m+1`, `k = 4j−1` | PROVED HERE | known |
| **Lemma 3** | **two-unit-fraction criterion**: `a/b = 1/y+1/z`, `y ≤ z` ⟺ ∃ `u \| b²`, `1 ≤ u ≤ b`, `u ≡ −b (mod a)` | **PROVED HERE + FORMALLY VERIFIED** | known in substance (same object as Jiang 2026) |
| Lemma 4 | criterion for `4/n` with prescribed `x` | PROVED HERE | known |
| Lemma 5 | prime witnesses | PROVED HERE | known |
| Lemma 6 | inheritance under `d \| n` | PROVED HERE | known |
| **Theorem 7** | `ES(n)` holds unless `n ≡ 1 (mod 24)` **and** every prime divisor `≡ 1 (mod 24)` | PROVED HERE (of classical content) | ESTABLISHED IN PRIOR WORK |
| **Theorem 8** | for odd `n ≡ 1 (mod 4)`: `ES(n)` has a solution with `y = z` **iff** `n` has a prime divisor `≡ 3 (mod 4)`; same for `x = y` | PROVED HERE | KNOWN in spirit; priority not certified |
| **Corollary 9** | if `n` is in the hard core `H`, **every** solution has `x < y < z` | PROVED HERE | as above |
| **Theorem 10** | for `n ∈ H`: a solution with `4x − n = 3` exists **iff** `(n+3)/4` has a prime divisor `≡ 2 (mod 3)` | PROVED HERE, both directions sharp | KNOWN in substance (classical `k = 3` family) |
| **Theorem 11** | for `n ≡ 1 (mod 24)`, `k ≡ 3 (mod 4)`, `gcd(k,n) = 1`: `k ∤ n² + 4`; hence `u = 1` never works | PROVED HERE | **NOVELTY UNCERTAIN** |
| Theorem 12 / Cor. 13 | four closed-form solution families (`F1'`, `F3'` and their `c = 1` instances) | PROVED HERE | KNOWN in substance (classical) |
| **Theorem 14** | if `n ∈ H` and `ES(n)` fails, then (O1)–(O4) hold; quantified on `H ∩ [1, 600000]` | PROVED HERE (+ COMPUTATIONALLY VERIFIED quantification) | **NOVELTY UNCERTAIN** |

### 3.1 The three results carrying the most weight

**Theorem 7 (localisation).** Any counterexample must lie in
`H = { n ≡ 1 (mod 24) : every prime divisor of n ≡ 1 (mod 24) }`. This is
built from four explicit identities, each checked term by term, plus a descent
lemma. `H` is thin: **29 298** integers up to `3·10^6`, i.e. 23.4 % of the
125 000 integers `≡ 1 (mod 24)` in that range and **0.98 %** of all integers.

**Theorem 8 / Corollary 9 (structural rigidity).** In the hard core, `ES(n)` has
a solution with two equal denominators **if and only if** `n` has a prime
divisor `≡ 3 (mod 4)` — which, by the definition of `H`, it never does.
Consequently *every* solution in `H` satisfies `x < y < z`. The two-denominator
shortcuts that dispose of every easy case are **provably unavailable** exactly
where the difficulty is concentrated.

**Theorem 14 (obstruction).** Failure of `ES(n)` for `n ∈ H` forces: (O1) every
prime divisor of `(n+3)/4` is `≡ 1 (mod 3)`; (O2) every odd prime divisor of
`n+1` is `≡ 1 (mod 4)`; (O3) every prime divisor of `n+4` is `≡ 1 (mod 4)`;
(O4) for every `k ≡ 3 (mod 4)` with `k < 73`, `n(n+k)/4` has no divisor `≤ n(n+k)/4`
congruent to `−n²·4⁻¹ (mod k)`. Quantified: on `H ∩ [1, 600000]` (6467 values)
(O1)–(O3) leave only **799** candidates (12.36 %), of which only **16** need
`μ(n) > 23`.

## 4. What was computed

All exact integer arithmetic; no floating point anywhere in `src/` or `tests/`;
no random number generators. `results/sieve_summary.json` holds the output.

* On `H ∩ [1, 3·10^6]`: **0** values lack a solution with `k ≤ 255`.
* `μ(n)` (smallest `k ≡ 3 (mod 4)` admitting a solution) reaches **59**, at
  exactly `n = 118801` and `n = 806521`.
* Composites in `H` are dramatically easier: the 2315 composite members of
  `H ∩ [1, 3·10^6]` all have `μ ≤ 15` (the maximum, at `n = 458761`) —
  including the 27 that are prime powers `p^e`, `e ≥ 2`, which have `μ ≤ 11` —
  while the 26983 prime members reach 59, at `n = 118801` and `n = 806521`
  (both prime).
* Separate minima (after correcting an earlier conflation of two different
  quantities — see `research/proof_attempts.md` A8): minimum number of distinct
  admissible `k` over `H ∩ [1, 6000]` is 3 (`n = 73, 193`); minimum number of
  full solutions `(x,y,z)` over `H ∩ [1, 20000]` is 6 (`n = 193`).

Explicit resistant instance:

```text
4/118801 = 1/29715   + 1/59875704    + 1/84724121160     (k = 59, the first solution)
4/118801 = 1/29748   + 1/18503256    + 1/2198205316056   (closed form, d = 191 | n+1)
```

The second line matters: the closed-form families of Corollary 13 and the `k`-sieve
are genuinely complementary, not redundant.

## 5. Formal verification

`lean/ESCriterion.lean` formalises **Lemma 3 only**, over `ℤ`:

```text
$ lake build                      →  exit 0, "Build completed successfully (3138 jobs)"
$ lake env lean ESCriterion.lean  →  no output (no errors, no warnings)
$ lake env lean AxiomAudit.lean
'ES.criterion_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
```

`sorryAx` does not appear, which is exactly the sense in which the file contains
no unfinished proof. Toolchain `leanprover/lean4:v4.35.0-rc4`. Full record,
including the three genuine type errors that were fixed rather than bypassed,
in `lean/BUILD_STATUS.md` and `research/research_log.md`.

**What this does not do.** It does not formalise Theorems 7–14, and it does not
verify that `src/es_theory.py` transcribes the criterion faithfully. Those
statements rest on the written proofs plus the test suite, and are labelled
accordingly.

## 6. What was not proved, and the honest failures

* **The Erdős–Straus conjecture is not proved and not disproved.**
* `ES(n)` for all `n ∈ H` is equivalent to the conjecture and remains
  **UNRESOLVED**.
* No bound on `μ(n)` is proved; whether `μ` is bounded is **UNRESOLVED**.
* The claim that every composite in `H` has `μ ≤ 15` is verified only on
  `H ∩ [1, 3·10^6]` (where the 27 prime powers have `μ ≤ 11`); no proof is
  offered and it is listed as an open question in the README.
* `paper/main.tex` was **not** compiled — no LaTeX toolchain was available. It
  ships as uncompiled source alongside `paper/main.md`.
* Priority is **not** claimed for anything. The Erdős–Straus literature is large
  and active (Elsholtz–Tao 2011, Lopez 2024, Bello-Hernández 2026, Jiang 2026);
  `research/literature_review.md` records both what was verified and what could
  not be verified, including a naming collision between this project's "witness"
  and a different object in the literature (LR-3).
* One incident is recorded rather than hidden: the first working directory was
  **externally replaced** mid-session by an unrelated concurrent project and the
  local files were lost. Nothing belonging to that project was touched. The work
  was rebuilt from scratch in a separate directory, and **every number quoted in
  the README and paper was re-derived after the rebuild**, not carried over. See
  `research/incident.md`.
* Two independent miscounts in this project came from the same habit —
  trusting a helper's name for what it returns. The first counted distinct
  admissible `k` values where the text said "solutions"; the second used
  `len(factorise(n)) == 1` as a primality test, which is also true of prime
  powers `p^e` and misclassified 27 members of `H`. Both were caught by
  re-deriving the headline figures with a second implementation that shares no
  code with `src/` (`experiments/exp06_recheck_headline.py`), fixed, and
  recorded rather than quietly patched: `research/proof_attempts.md` A8 and A9.
  A mis-stated percentage (`0.098 %` corrected to `0.98 %`) is recorded in
  `research/research_log.md` for the same reason.

## 7. The one obstacle that matters

Every criterion in the project — Theorems 5, 10, 11, 12 — asks the same kind of
question about an explicit integer built from `n`:

> does `(n+3)/4`, `n+1`, `n+4`, `n(n+k)/4`, … have a prime divisor in a
> prescribed residue class modulo a small `k`?

For `n ∈ H` those integers are large and their residue classes modulo small `k`
are precisely what would need to be controlled, and nothing established here
forces such a prime divisor to exist. **The remaining gap is mathematical, not
computational.** Extending the search to `n = 10^18` would change no label in
this repository.

## 8. Verification status of this report

* `python tests/test_theorems.py` → **27/27 passing** (exact rational arithmetic;
  each computational routine cross-checked against an independently written one).
* `lake build` and the axiom audit → as in §5, output recorded verbatim in
  `lean/BUILD_STATUS.md`.
* `experiments/exp01`–`exp07` all reproduce; `results/sieve_summary.json` is
  committed. `exp06` re-derives the headline figures from scratch, sharing no
  code with `src/`.
* Instructions, environment and expected outputs: `docs/reproducibility.md`.

## 9. Verdict

The selected problem was not solved. What was produced is a machine-checked
exact criterion, a sharp localisation of the remaining difficulty, a structural
rigidity theorem, a quantified obstruction theorem, and a reproducible exact
computation. Most of the mathematical content is classical or known in
substance, and that is stated rather than glossed; the two items whose novelty
could not be settled are labelled **NOVELTY UNCERTAIN** rather than promoted.

Because (a) the headline problem remains open, (b) no result here is certified
as new, and (c) the obstruction theorem narrows but does not close the gap, the
honest category is:

> ### C — RIGOROUS PARTIAL RESULT

Concretely, and against the obvious alternatives: **A** (solved) is false — the
conjecture is untouched. **B** (a substantial new advance) was not awarded
because the only two results whose novelty could not be settled are the two
shortest arguments in the project, and because the central theorem (7) is
classical. **D** (inconclusive / no usable result) is too harsh: Lemma 3 is
machine-checked, Theorem 7 and Corollary 9 are complete proofs, and the
obstruction theorem is quantified. **E** (failure) is simply wrong.

What has been proved is what the proof establishes—not what the project hoped
to establish.