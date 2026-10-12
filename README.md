# The Erdős–Straus conjecture: an exact criterion, a localised hard core, and where a proof would still have to go

**Repository:** <https://github.com/rajveersinh-is-dev/erdos-straus-conjecture-investigation>

**Status of the headline result:** the Erdős–Straus conjecture is **not solved here**.
What is proved is a sharp localisation of the difficulty plus a set of
structural theorems about the surviving case, one of which is new as far as we
can verify and none of which is advertised as more than it is.

**Final report (including the verdict and the list of things that were wrong):**
[`FINAL_REPORT.md`](FINAL_REPORT.md).

---

## 1. The problem

> **Erdős–Straus conjecture (1948).** For every integer `n ≥ 2` there exist
> positive integers `x, y, z` with
>
>         4/n = 1/x + 1/y + 1/z .

Confirmed **open** as of 2026-10-12 (`research/literature_review.md`, LR-1).
Computer searches verify it up to `n ≤ 10^17`; that verification is *not* our
contribution and is not needed for any theorem below.

## 2. What we proved — read this part

Complete proofs: [`mathematics/proofs.md`](mathematics/proofs.md).
Statements and evidence labels: [`mathematics/main_results.md`](mathematics/main_results.md).

### 2.1 The difficulty is confined to a thin, explicit set

> **Theorem 7 (PROVED HERE).** `ES(n)` holds for every `n` that is **not** in
> the hard core
>
>         H = { n : n ≡ 1 (mod 24)  and  every prime divisor of n ≡ 1 (mod 24) }.
>
> Equivalently: **any** counterexample lies in `H`.

Built from four explicit identities (each verified by hand *and* by the test
suite) and one descent lemma. `H` contains only **29 298** integers up to
`3·10^6` — 23.4 % of the 125 000 integers `≡ 1 (mod 24)` in that range, and
0.98 % of all integers.

### 2.2 In the hard core, every solution is asymmetric

> **Theorem 8 (PROVED HERE).** For odd `n ≡ 1 (mod 4)`: `ES(n)` has a solution
> with `y = z` **iff** `n` has a prime divisor `≡ 3 (mod 4)`; the same
> equivalence holds with `x = y` in place of `y = z`.
>
> **Corollary 9 (PROVED HERE).** If `n ∈ H` then **every** solution satisfies
> `x < y < z`.

So in the hardest case the two-denominator identities that solve every easy
case are *provably unavailable*. This is a clean statement about what a solution
would have to look like.

### 2.3 An exact, cheap criterion

> **Lemma 3 (PROVED HERE; FORMALLY VERIFIED in Lean).** For `gcd(a,b) = 1`,
>
>         a/b = 1/y + 1/z for some 1 ≤ y ≤ z
>     ⟺  ∃ u | b²  with  1 ≤ u ≤ b  and  u ≡ −b (mod a).
>
> Proof idea: `(ay−b)(az−b) = b²`, so a solution corresponds to a factorisation
> `b² = uv` with `u ≡ v ≡ −b (mod a)`; and if `u ≡ −b (mod a)` and `uv = b²`
> then `v ≡ −b (mod a)` automatically, because `gcd(a,b) = 1`.

This converts the Diophantine question into a finite divisor computation — the
only reason the experiments below are cheap.

### 2.4 A sharp criterion for the *smallest* possible `x`

> **Theorem 10 (PROVED HERE, both directions).** For `n ∈ H`, a solution with
> `4x − n = 3` exists **iff** `(n+3)/4` has a prime divisor `≡ 2 (mod 3)`.

Verified with **zero** mismatches against the brute-force criterion on all
3380 hard-core values `≤ 300000`.

### 2.5 An impossibility result

> **Theorem 11 (PROVED HERE).** For `n ≡ 1 (mod 24)` and `k ≡ 3 (mod 4)` with
> `gcd(k,n) = 1`, one has `k ∤ n² + 4`. Hence the most obvious witness
> `u = 1` **never** yields a solution.

The proof is the classical fact that every prime divisor of `n² + 4` is
`≡ 1 (mod 4)`. Consequence: any proof of Erdős–Straus for the hard core must
use a *genuine* prime factor of one of the integers `n(n+k)/g`.

### 2.6 Two closed-form families

> **Theorem 12 / Corollary 13 (PROVED HERE).** Let `n ≡ 1 (mod 4)`,
> `d ≡ 3 (mod 4)`, `gcd(d,n) = 1`, `x = (n+d)/4`. Then
>
> * if `d | n+4`:  `4/n = 1/x + 1/(n(x+1)/d) + 1/(n x(x+1)/d)`;
> * if `d | n+1`:  `4/n = 1/x + 1/(x(n+1)/d) + 1/(n x(n+1)/d)`;
> * more generally `F1'`: `d | n+4c`, `c | x²`, `1 ≤ c ≤ x`;
> * more generally `F3'`: `d | n+c`,  `c | n²`, `1 ≤ c ≤ n`.

All four are the single identity `1/x + d/(nx) = 4/n` with `4x = n + d`; the
content is that the second term splits into two unit fractions.
`4/5 = 1/2 + 1/4 + 1/20` and `4/13 = 1/5 + 1/10 + 1/130` are the `d = 3`
and `d = 7` instances.

### 2.7 An obstruction theorem for counterexamples

> **Theorem 14 (PROVED HERE).** If `n ∈ H` and `ES(n)` fails then
> **(O1)** every prime divisor of `(n+3)/4` is `≡ 1 (mod 3)`;
> **(O2)** every odd prime divisor of `n+1` is `≡ 1 (mod 4)`;
> **(O3)** every prime divisor of `n+4` is `≡ 1 (mod 4)`;
> **(O4)** for every `k ≡ 3 (mod 4)`, `k < 73`, the integer `n(n+k)/4` has no
> divisor `≤ n(n+k)/4` congruent to `−n²·4⁻¹ (mod k)`.

Quantitatively (COMPUTATIONALLY VERIFIED): on `H ∩ [1, 600000]` (6467 values),
(O1)–(O3) together leave only **799** candidates (12.36 %), and of those only
**16** need `μ(n) > 23`.

### 2.8 The resistant instances

> **Finding (COMPUTATIONALLY VERIFIED).** On `H ∩ [1, 3·10^6]` every `n` has
> `μ(n) ≤ 59` (where `μ(n)` is the smallest `k ≡ 3 (mod 4)` admitting a
> solution), and the maximum is attained at exactly `n = 118801` and
> `n = 806521`. In particular
>
>         4/118801 = 1/29715 + 1/59875704 + 1/84724121160
>
> is the *first* solution of `118801` (`k = 59`); no `k < 59` works. The
> closed form of Corollary 13 does kill it, via `d = 191 | (n+1)`:
>
>         4/118801 = 1/29748 + 1/18503256 + 1/2198205316056 .
>
> **Finding (COMPUTATIONALLY VERIFIED).** Composite members of `H` are much
> easier than prime ones: among `H ∩ [1, 3·10^6]` the 2315 composite members
> all have `μ ≤ 15` (the maximum, at `n = 458761`; the 27 of them that are prime
> powers `p^e`, `e ≥ 2`, have `μ ≤ 11`), while the 26983 prime members reach
> `μ = 59`.

## 3. What we did **not** prove

* The Erdős–Straus conjecture. Not proved, not disproved.
* `ES(n)` for all `n ∈ H`. By Theorem 7 this is *equivalent* to the conjecture.
* Any bound on `μ(n)` as `n → ∞`. We record that `μ` reaches 59 on the tested
  range; whether it is bounded is **UNRESOLVED**.

## 4. The single most important obstacle

Every criterion above (Theorems 5, 10, 11, 12) asks the same kind of question
about a linear function of `n`:

> does some explicit integer built from `n` — namely `(n+3)/4`, `n+1`, `n+4`,
> `n(n+k)/4`, … — have a prime divisor in a prescribed residue class modulo a
> small `k`?

For `n ∈ H` those integers are large and their residue classes modulo small `k`
are exactly what we would need to control, and nothing in this project forces
such a prime divisor to exist. **That gap, not any computational limit, is where
a solution would have to live.**

## 5. Evidence categories used throughout

`PROVED HERE` · `ESTABLISHED IN PRIOR WORK` · `FORMALLY VERIFIED` ·
`COMPUTATIONALLY VERIFIED` · `CONDITIONAL` · `CONJECTURED` · `HEURISTIC` ·
`UNRESOLVED`. Definitions: [`research/evidence_labels.md`](research/evidence_labels.md).

Every claim in `mathematics/main_results.md` carries one. The honest summary:

| Statement | Category |
|---|---|
| Theorem 7 (reduction to `H`) | ESTABLISHED IN PRIOR WORK (classical), re-proved here with explicit identities |
| Lemma 3 (criterion) | ESTABLISHED IN PRIOR WORK in substance (same object as Jiang 2026), proved and formally verified here |
| Theorem 8 / Corollary 9 | PROVED HERE; KNOWN in spirit; priority not certified |
| Theorem 10 | PROVED HERE; KNOWN in substance (classical `k = 3` family) |
| Theorem 11 | PROVED HERE; novelty **uncertain** |
| Theorem 12 / Corollary 13 | PROVED HERE; KNOWN in substance (classical parametric families) |
| Theorem 14 (obstruction) | PROVED HERE; novelty **uncertain** |
| Resistant instances (2.8) | COMPUTATIONALLY VERIFIED |

**We do not claim priority over the literature.** The field is active (Jiang
2026, Bello-Hernández 2026, Lopez 2024, Elsholtz–Tao 2011); see
`research/literature_review.md` for what is known and where we could not verify.

## 6. Proof strategy in one paragraph

Fix the smallest denominator `x` and set `k = 4x − n`. Lemma 1 confines `x` to
`n/4 < x ≤ 3n/4`, and the equation becomes `1/y + 1/z = 4k/(n(n+k))` — a
*two*-unit-fraction problem, which Lemma 3 solves exactly by factoring `b²`.
Writing `n = 24m+1` and `k = 4j−1` makes `k` run over `3, 7, 11, …` and turns
the whole conjecture into an explicit sequence of finite divisor questions
about `n(6m+j)/gcd(4j−1, n(6m+j))`. Everything else in this repository is a
study of those questions.

## 7. Repository map

```
mathematics/     definitions.md, main_results.md, proofs.md   <- the mathematics
research/        problem_selection.md, literature_review.md, research_log.md,
                 proof_attempts.md, known_results.md, evidence_labels.md,
                 counterexamples.md, incident.md
src/             es_theory.py (Lemma 1 + Lemma 3), es_sieve.py (k-sieve)
tests/           test_theorems.py  (27 tests, exact arithmetic)
experiments/     exp01..exp07, all reproducible
results/         sieve_summary.json
paper/           main.tex (LaTeX mirror), main.md (readable version)
lean/            ESCriterion.lean (formal proof of Lemma 3),
                 AxiomAudit.lean, BUILD_STATUS.md
docs/            reproducibility.md
```

## 7b. Known errors, found and corrected

Two statistics in earlier drafts of this repository were wrong. Both were found
by re-deriving the headline numbers with an independent implementation
(`experiments/exp06_recheck_headline.py`, which shares no code with `src/`), and
both are documented rather than quietly patched:

* **§A8** — an experiment counted *distinct admissible `k`* where the text said
  "number of solutions". Now reported separately: min 3 distinct `k`
  (`n = 73, 193`) on `H ∩ [1, 6000]`, min 6 solutions (`n = 193`) on
  `H ∩ [1, 20000]`.
* **§A9** — `len(factorise(n)) == 1` was used as a primality test, which is also
  true of prime powers `p^e`, `e ≥ 2`, and `p^e ∈ H` whenever `p ≡ 1 (mod 24)`.
  This moved the hard-core prime/composite split by 27. Corrected to
  **26 983 prime, 2 315 composite**; the qualitative conclusion is unchanged.

Full write-ups: [`research/proof_attempts.md`](research/proof_attempts.md).

## 8. Dependencies and reproduction

* **Python ≥ 3.10**, standard library only (`fractions`, `math`). No NumPy,
  no Sage, no internet access needed.
* Run the tests: `python tests/test_theorems.py` (or `python -m pytest tests/ -q`).
* Run the experiments: `python experiments/exp01_baseline.py`, … `exp07`.
* Lean (optional): `cd lean && lake build && lake env lean AxiomAudit.lean` —
  builds cleanly; see `lean/BUILD_STATUS.md` and `docs/reproducibility.md`.

Full instructions, environment details and expected outputs:
[`docs/reproducibility.md`](docs/reproducibility.md).

## 9. Tests and validation

`python tests/test_theorems.py` → **27/27 passing** (all arithmetic exact;
`fractions.Fraction`, never floats). The tests check, among other things:

* the criterion against brute-force search for all reduced `a/b`, `b ≤ 260`;
* every one of the four identities of Theorem 7, term by term;
* the reduction of Theorem 7 for all `n ≤ 20000`;
* the repeated-denominator classification of Theorem 8 for all `n ≡ 1 (mod 4)`
  up to 1200, and asymmetry for all `n ∈ H` up to 20000;
* the sharpness of Theorem 10 on all `n ∈ H` up to 100 000;
* Theorem 11 on all `n ∈ H` up to 100 000;
* Corollary 13 for every `n ≡ 1 (mod 4)` up to 2500;
* agreement between the `k`-sieve and the generic search;
* the specific resistant instances quoted above.

## 10. Known limitations

* No proof of Erdős–Straus. The project reduces it to a thin set and studies
  that set; it does not finish it.
* Prior-art claims are conservative but not exhaustive. We could not access
  MathSciNet or zbMATH, and we did not do a full-text search of a field with
  hundreds of papers. **Absence of a search hit is not evidence of novelty.**
* The computational claims are finite statements about finite ranges; they are
  labelled COMPUTATIONALLY VERIFIED and are never used as universal evidence.
* A LaTeX toolchain is not installed in the authoring environment, so
  `paper/main.tex` is provided as a faithful source file but was **not compiled
  here**. `paper/main.md` is the same content in Markdown.
* See `research/incident.md`: the first working directory was externally
  replaced mid-session; the project was rebuilt from scratch elsewhere.

## 11. Open questions this project leaves

1. Is `μ(n)` bounded on `H`? (It reaches 59 on `H ∩ [1, 3·10^6]`.)
2. Is there an `n ∈ H` for which **no** `k < 100` works?
3. Is every hard-core *composite* `n` solvable with `k ≤ 15`? (Verified on
   `H ∩ [1, 3·10^6]`; a proof would be a genuine new result.)
4. Can the obstruction conditions (O1)–(O4) be strengthened into a set that is
   provably never satisfied?

## 12. Citations

* P. Erdős and E. G. Straus, *On a Diophantine equation of Erdős and Straus*,
  Acta Arith. **3** (1948), 363–367.
* C. Elsholtz and T. Tao, *Counting the number of solutions to the Erdős–Straus
  equation on unit fractions*, arXiv:1107.1010 (2011).
* M. A. Lopez, *A Complete Congruence System for the Erdős–Straus Conjecture*,
  arXiv:2404.01508 (2024).
* M. Bello-Hernández, *A Divisor Parametrization for the Erdős–Straus
  Conjecture*, arXiv:2606.10922 (2026).
* X. Jiang, *Counting Type I and Type II solutions of the Erdős–Straus
  equation: concentration, local obstructions, and a pointwise comparison*,
  arXiv:2609.09204 (2026).

All five were verified to exist on arXiv / Crossref on 2026-10-12; see
`research/literature_review.md`.

## 13. Licence

MIT — see [`LICENSE`](LICENSE). This project is not affiliated with, or
endorsed by, any of the authors cited above.
