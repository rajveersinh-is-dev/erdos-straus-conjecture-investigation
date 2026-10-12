# Evidence labels

Every substantive claim in this repository carries exactly one of the following
labels. A stronger label is never used than the evidence supports.

| Label | Meaning | Where used |
|---|---|---|
| **PROVED HERE** | A complete proof is written in `mathematics/proofs.md` and is checked against the implementation by `tests/test_theorems.py`. | Theorems 7, 8, 9, 10, 11, 12, 13, 14; Lemmas 1–5; Corollary 2.1 |
| **ESTABLISHED IN PRIOR WORK** | The mathematical content is classical or published; we give a self-contained proof for completeness, not as a new contribution. | The reduction to `n ≡ 1 (mod 24)`; the `k = 3` and `d | n+4`, `d | n+1` parametric identities |
| **FORMALLY VERIFIED** | The proof has been accepted by the Lean 4 kernel (Mathlib), with no `sorry` and no `axiom` beyond the standard library. | `lean/ESCriterion.lean` (Lemma 3) — **see the note below** |
| **COMPUTATIONALLY VERIFIED** | The claim is about an explicitly stated finite range, produced by an exact-integer algorithm that ships in `src/`. Never used as evidence for a universal statement. | The `k`-census, coverage figures, the `μ` records, resistant instances |
| **CONDITIONAL** | Depends on an assumption not proved here. | *(none)* |
| **CONJECTURED** | Suggested by evidence, not proved. | The Erdős–Straus conjecture itself; boundedness of `μ` |
| **HEURISTIC** | Suggestive reasoning only. | The remark that the difficulty concentrates in "does a linear function of `n` have a prime divisor in a given residue class" |
| **UNRESOLVED** | An essential step remains open. | `ES(n)` for all `n ∈ H`; any bound on `μ(n)` |

## Note on the Lean status

The Lean file `lean/ESCriterion.lean` is a formalisation of **Lemma 3 only** —
not of the reduction theorem, not of the closed forms, and certainly not of the
conjecture.

**Status: built successfully.** `lake build` completes with exit code 0 and
`lake env lean ESCriterion.lean` produces no output; the axiom audit in
`lean/AxiomAudit.lean` shows that `ES.criterion_iff` depends only on `propext`,
`Classical.choice` and `Quot.sound`, and in particular not on `sorryAx`. The
exact commands, the toolchain version and the verbatim output are recorded in
`lean/BUILD_STATUS.md`. The `FORMALLY VERIFIED` label is therefore claimed for
Lemma 3 and for no other statement in this repository.

The one thing the formalisation does *not* establish is that the Python
transcription of the criterion in `src/es_theory.py` is faithful to it; that
link rests on the test suite, which carries a different label.

## Novelty convention

For each theorem we give three separate judgements:

1. **Is it true?** — `PROVED HERE` or `FORMALLY VERIFIED`.
2. **Is it new?** — one of `KNOWN`, `EQUIVALENT TO KNOWN WORK`,
   `NEW PRESENTATION`, `POTENTIALLY NEW`, `NOVELTY UNCERTAIN`.
3. **How confident are we in (2)?** — stated in words, with the limitation of
   the literature search recorded (`research/literature_review.md`, LR-6).

Judgement (2) is deliberately conservative. The Erdős–Straus literature is large
and active, and we do not claim priority without evidence of it.
