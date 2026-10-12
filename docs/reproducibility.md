# Reproducibility

Everything in this repository runs from a clean checkout with no network
access, except the optional Lean step.

---

## 1. Requirements

| Component | Version used | Notes |
|---|---|---|
| Python | 3.14.6 (works on ≥ 3.10) | **Standard library only.** No NumPy, no SciPy, no SageMath, no internet. |
| Git | 2.53 | |
| Lean 4 (optional) | 4.34.1 | plus Mathlib; only for `lean/` |

## 2. Getting the code

```bash
git clone https://github.com/rajveersinh-is-dev/erdos-straus-conjecture-investigation.git
cd erdos-straus-conjecture-investigation
```

## 3. Running the tests

```bash
python tests/test_theorems.py
```

Expected: `25/25 tests passed`, exit status 0.

or

```bash
python -m pytest tests/ -q
```

Runtime: a few minutes on a single core. The suite is dominated by
`test_theorem7_reduction_holds` (generic search for every `n ≤ 20000`) and the
cross-checks between the two independent implementations.

**What the tests actually check.** Each test mirrors a numbered statement:

| test | statement |
|---|---|
| `test_lemma3_criterion_matches_brute_force` | Lemma 3, criterion vs. direct search, all reduced `a/b` with `b ≤ 260` |
| `test_lemma3_pair_formulas` | Lemma 3, the produced `(y,z)` really sum to `a/b` |
| `test_window_bound_and_all_solutions_exact` | Lemma 1, and exact verification of every solution found |
| `test_es_holds_up_to_2000` | no counterexample up to 2000 |
| `test_regression_known_witnesses` | the six values a buggy implementation once reported as counterexamples |
| `test_identity_I1..I4` | the four reduction identities, term by term |
| `test_theorem7_reduction_holds` | Theorem 7 for every `n ≤ 20000` outside `H` |
| `test_hard_core_membership_and_first_values` | definition of `H`, and its first members |
| `test_theorem8_repeated_denominator_classification` | Theorem 8, both parts, for all `n ≡ 1 (mod 4)` up to 1200 |
| `test_corollary9_hard_core_solutions_asymmetric` | Corollary 9 for all `n ∈ H` up to 20000 |
| `test_theorem10_k3_criterion_exact` | Theorem 10, both directions, for all `n ∈ H` up to 100000 |
| `test_theorem11_no_k_divides_n2_plus_4` | Theorem 11, for all `n ∈ H` up to 100000 |
| `test_corollary13_1/2` | Corollary 13 for every `n ≡ 1 (mod 4)` up to 2500 |
| `test_theorem12_f1_and_f3_witness_conditions` | Theorem 12 witness conditions |
| `test_sieve_agrees_with_generic_search` | the `k`-sieve vs. the generic window search |
| `test_witness_presence_matches_solver` | the divisor criterion vs. the solver |
| `test_resistant_instance_118801/246241/806521` | the specific instances quoted in the README |
| `test_composite_hard_core_are_easier` | composites in `H` need `k ≤ 15` |
| `test_minimum_number_of_solutions_in_hard_core` | minimum number of admissible `k` values |

## 4. Running the experiments

```bash
python experiments/exp01_baseline.py       # witnesses for small n; regression values
python experiments/exp02_structure.py      # residue classes, the reduction, H, asymmetry
python experiments/exp03_kcensus.py        # k-census; checks Theorems 10 and 11
python experiments/exp04_closed_forms.py   # closed forms; coverage of H by F1'/F3'
python experiments/exp05_obstruction.py    # obstruction strength; mu records to 3*10^6
```

Total runtime: under two minutes on a single core. `exp05` writes
`results/sieve_summary.json`.

### Key numbers these scripts produce

| script | figure | value |
|---|---|---|
| exp01 | `n ∈ [2,2000]` with no solution | none |
| exp02 | `n ≤ 20000` outside `H` without a solution | none |
| exp02 | solutions in `H` that are not strictly increasing | 0 |
| exp03 | `H ∩ [1,300000]` size | 3380 |
| exp03 | Theorem 10 mismatches | 0 of 3380 |
| exp03 | Theorem 11 violations | 0 |
| exp03 | coverage by `{k = 3,7,11,15,23}` | 3348/3380 = 99.05 % |
| exp04 | closed-form instances verified exactly | 5654 |
| exp04 | union coverage `F1' ∪ F3'` on `H ∩ [1,300000]` | 2920/3380 = 86.39 % |
| exp05 | `H ∩ [1,600000]` size; survivors of (O1)+(O2)+(O3) | 6467; 799 (12.36 %) |
| exp05 | `H ∩ [1,3·10^6]` size | 29298 (27010 prime, 2288 composite) |
| exp05 | max `μ` among primes / composites | 59 / 15 |
| exp05 | values of `H ∩ [1,3·10^6]` with no solution for `k ≤ 255` | 0 |

## 5. Determinism

* No random number generators are used anywhere in the reported pipeline.
* All arithmetic is exact: integers and `fractions.Fraction`. There is not a
  single floating-point comparison in `src/` or `tests/`.
* Results depend only on the Python standard library, so they are
  platform-independent.

## 6. Lean step (optional)

`lean/ESCriterion.lean` is a formalisation of **Lemma 3 only**.

```bash
cd lean
lake exe cache get     # downloads prebuilt Mathlib oleans (~9000 files)
lake build
```

**Honest status.** The authoring environment has Lean 4.34.1 and `lake` 5.0.0
and fetched the Mathlib cache, but **no LaTeX toolchain and no guarantee of a
successful build were available there**. The build outcome is recorded in
`lean/BUILD_STATUS.md`. If that file does not record a successful
`lake build`, the file must be treated as a formalisation *attempt* and the
`FORMALLY VERIFIED` label in `research/evidence_labels.md` is **not** claimed
for it.

Nothing else in the project depends on this step.

## 7. What is *not* reproduced here

* The published verification of Erdős–Straus up to `n ≤ 10^17`. It is
  reported in the literature and is not needed for any statement here.
* Any claim about `n` beyond `3·10^6`.
* The paper is supplied as `paper/main.tex` and `paper/main.md`; **no LaTeX
  compiler was available**, so `main.tex` was not compiled here.

## 8. Note on the first working directory

The first half of the session was lost to an external workspace reset; see
`research/incident.md`. All figures in this document were re-derived **after**
the rebuild, by the scripts above.
