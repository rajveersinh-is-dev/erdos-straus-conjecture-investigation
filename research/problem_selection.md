# Problem selection

Decision record. Criteria and weights are those stated in the project brief;
scores are *ordinal judgements*, not calibrated quantities.

---

## Selected target

**The Erdős–Straus conjecture.** For every `n >= 2` there are `x, y, z` in
`Z_{>0}` with

        4/n = 1/x + 1/y + 1/z .

Formulated in 1948; **confirmed open** on 2026-10-12 (see
`literature_review.md`, LR-1).

## Why this problem

| Criterion | Weight | Assessment |
|---|---:|---|
| Potential for meaningful new mathematics | 20 % | Medium. The full conjecture is almost certainly out of reach; but the *hard core* is small, precisely describable, and admits sharp structural results. |
| Plausible route to a rigorous result | 20 % | High. We produced complete proofs of a reduction, an exact criterion, a sharp criterion for the smallest `k`, two closed-form families, an impossibility result and an obstruction theorem. |
| Mathematical depth | 15 % | Medium-high. Genuine Diophantine structure: divisors, residue classes, quadratic residues. |
| Quality of the research frontier | 10 % | High. Active: Jiang 2026, Bello-Hernández 2026, Lopez 2024, Elsholtz–Tao 2011 all on the structure of the solutions. |
| Independence from large-scale computation | 15 % | Excellent. Every theorem is a symbolic argument. The largest computation is a sieve over 29 298 hard-core integers, which runs in seconds on one core. |
| Precision and testability | 10 % | Excellent. Every statement is a decision problem for exact integers; the test suite checks all of them. |
| Potential to explain the result elegantly | 5 % | Good. Everything reduces to the identity `1/x + d/(nx) = 4/n` with `4x = n+d`. |
| Portfolio and educational value | 5 % | Good. Clean separation of "known", "proved here", "computed", "conjectured". |

**Selection against the explicit criteria.**

* *Decisive work is mathematical, not computational.* Yes. The hard core `H`
  contains only 29298 integers up to `3*10^6`; the whole study takes seconds.
  Removing every experiment leaves the full argument intact.
* *Not a famous problem chosen for prestige.* The brief's warning is taken
  seriously: we did **not** pick Erdős–Straus hoping to solve it. We picked it
  because it has the rare combination of (a) a *small, precisely describable*
  surviving difficulty, and (b) a methodology that produces checkable theorems.
* *Not artificially easy.* The conjecture is genuinely open.
* *Not computation-limited.* Verified: see `results/sieve_summary.json`.

## Alternatives considered (see `literature_review.md` §LR-5 for the short list)

Each was rejected for a specific, stated reason rather than by preference:
Alon–Jaeger–Tarsi (re-derivations dominate), Beck–Fiala (quantitative, not
structural), Lonely Runner (no small gap remains after Tao), sunflowers
(log-factor gap), Caccetta–Häggkvist (constant gap), Zaremba (no small gap).

## Honest statement of ambition

A complete solution to Erdős–Straus is **not** claimed and is not plausible
within this project. The realistic, valuable target is: *localise the
difficulty exactly, prove sharp structural results about the surviving case, and
state precisely what a solution would still require.* That target was met.

## Note on the working directory

The first half of this session was conducted in
`C:\Users\davea\Downloads\proj2\o`. That directory was **externally replaced**
mid-session by an unrelated concurrent project (Erdős Problem #536), and the
local files were lost. The work was rebuilt from scratch in a separate
directory and the repository on GitHub was created fresh. Nothing belonging to
the other project was read, modified, or deleted; see `research/incident.md`.
