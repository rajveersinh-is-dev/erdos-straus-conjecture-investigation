# Literature review — Erdős–Straus and neighbours

All entries were checked against a live bibliographic source (OpenAlex, Crossref,
arXiv API, Wikipedia) on **2026-10-12**. Nothing below is asserted from memory
alone; where a source could not be reached, that is stated.

---

## LR-1 The conjecture itself

* **Erdős, P.; Straus, E. G. (1948).** "On a Diophantine equation of
  Erdős and Straus". *Acta Arith. 3* (1948), 363–367.
  Formulation: for every `n >= 2`, `4/n` is a sum of three unit fractions.

* **Status (confirmed 2026-10-12): OPEN.** Wikipedia's "Erdős–Straus
  conjecture" article states the conjecture is unproven; it also records that
  computer searches verify it for `n <= 10^17`, that any composite
  counterexample would give a smaller prime counterexample, and that allowing
  *negative* unit fractions makes the statement true. None of the sources
  consulted claimed a proof.

## LR-2 The reduction to `n = 1 (mod 24)`

The classical reduction is standard folklore in the Erdős–Straus literature:
the cases "n even", "n = 3 (mod 4)", "n = 2 (mod 3)" have immediate
identifications, and by descent (`d | n` and a solution for `d` gives one for
`n`) only primes need be considered. The sharpened statement used here —
*every* counterexample lies in `H = {n = 1 (mod 24) : all prime divisors
= 1 (mod 24)}` — follows from those two facts plus the two extra identities
proved in Theorem 7 of `mathematics/proofs.md`.

**Novelty assessment: KNOWN (classical).** We did not locate a paper that
states the reduction in exactly the `H`-formulation, but the ingredients are all
standard and any competent treatment of the conjecture contains them. The value
of our Theorem 7 is that it is *self-contained, proved and machine-checked*, not
that it is new.

## LR-3 Prior work on the structure of solutions

This is where the genuinely competitive literature sits, and it is dense.

* **Elsholtz, C.; Tao, T. (2011).** "Counting the number of solutions to the
  Erdős–Straus equation on unit fractions." arXiv:1107.1010.
  Defines `f(n)` = number of solutions, proves
  `N log^2 N << sum_{p<=N} f(p) << N log^2 N log log N`, `f(p) = O(log^3 p log log p)`
  for a density-1 set of primes, and `f(p) << p^{3/5} + O(1/log log p)` for all
  primes. Introduces the Type I / Type II classification used in that line of work.

* **Lopez, M. A. (2024).** "A Complete Congruence System for the Erdős–Straus
  Conjecture." arXiv:2404.01508. Defines two new solution types (Type A, Type B)
  and a congruence system conjectured to contain all primes.

* **Bello-Hernández, M. (2026).** "A Divisor Parametrization for the
  Erdős–Straus Conjecture." arXiv:2606.10922. Introduces a divisor-based
  function and compares it with "well-known Type I/II descriptions".

* **Jiang, X. (2026).** "Counting Type I and Type II solutions of the
  Erdős–Straus equation: concentration, local obstructions, and a pointwise
  comparison." arXiv:2609.09204 (submitted 2026-09-05).
  Gives an exact counting identity: `f_I(p)` and `f_II(p)` are sums over
  denominators `n` coprime to `p` of the number of divisors of `n^2` in a single
  residue class modulo `e_n = 4n - p`; proves `f_I(n) = f_II(n) = 0` for every
  odd perfect square `n`; conjectures `f_I(p) > f_II(p)` for all `p > 5` with
  `p` not `= 1 (mod 8)`, verified for `p <= 10^6`.

**Consequence for our novelty claims.** Two of our statements are directly
adjacent to this literature and must be labelled conservatively:

* our *Lemma 3 criterion* (a divisor of `b^2` in a residue class) is the same
  object as Jiang's "number of divisors of `n^2` in a single residue class
  modulo `e_n`", stated in a cleaner, self-contained way. Label: **KNOWN /
  new presentation**.
* our *Corollary 9* (no solution in `H` has a repeated denominator) is
  closely related to Jiang's statement about odd perfect squares and to the
  classical Type I/II split. Label: **KNOWN in spirit; the `H`-version appears
  to be new but we cannot certify priority.**

**Remark LR-3 (naming collision).** Our labels "type (y = z)" and "type (x = y)"
are defined purely by the shape of the triple and are **not** Elsholtz–Tao's or
Jiang's "Type I"/"Type II". The two classifications are different: for a prime
`p`, their Type II solutions have the shape `4/p = 1/x + 1/(pY) + 1/(pZ)`,
which is about divisibility by `p`, not about repeated denominators.

## LR-4 Recently active adjacent searches

arXiv listings touched during the search (2026-10-12) include
arXiv:2608.24035 ("Sieve dimension and search depth for the Erdős–Straus
conjecture, `n = 1 mod 24`"), arXiv:2511.07465 (constructive proofs for primes
`= 1 (mod 4)`), arXiv:2206.10319 (structure and form of the solutions),
arXiv:2505.08716 (discrete zeta function and Erdős–Straus under Mballa's
conjecture). This indicates an active field; it is also the reason we do **not**
claim novelty for "one more residue class".

## LR-5 Alternatives considered and rejected

| Candidate | Why rejected |
|---|---|
| Alon–Jaeger–Tarsi conjecture | Open, but the graph-polynomial reformulation makes most new partial results re-derivations of the classical criterion; our capacity was better spent elsewhere. |
| Beck–Fiala discrepancy | Needs analytic machinery; progress is quantitative constants, not structure; hard to make a verifiable structural claim. |
| Lonely Runner Conjecture | Essentially equivalent to Zaremba-type Diophantine approximation; Tao's density-1 theorem removes the small gap that would admit a short structural attack. |
| Sunflower / Erdős–Rado | Best known bound is only a log factor from the target; no plausible point of entry. |
| Caccetta–Häggkvist | The remaining gap is in numerical constants (0.3465 vs 1/3), not structure. |
| Zaremba's conjecture | Deep, but the recent density-1 results again leave no small gap. |

## LR-6 What we could *not* verify

* We could not access MathSciNet or zbMATH, so we cannot rule out that some
  variant of Corollary 9, Theorem 11 or Theorem 12 appears in a journal not
  indexed by OpenAlex/arXiv.
* We did not attempt a full-text search of the Erdős–Straus literature; the
  field has hundreds of papers on parametric identities. Absence of a search hit
  is **not** evidence of originality.
