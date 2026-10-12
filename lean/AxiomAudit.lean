/-
# Axiom audit for `ESCriterion.lean`

This file is not part of the library. It is run by hand with

```bash
cd lean
lake env lean AxiomAudit.lean
```

and prints the axiom dependencies of every theorem in `ESCriterion`. The
output is pasted verbatim into `lean/BUILD_STATUS.md` as the evidence for the
`FORMALLY VERIFIED` label.

Expected output: each of `factorisation`, `criterion_iff` depends on at most
the three standard Lean axioms `propext`, `Classical.choice`, `Quot.sound`.
No `sorryAx` may appear: `sorryAx` is what Lean's kernel reports for an
unfinished proof, so its absence is exactly the statement "no `sorry` was
used".
-/
import ESCriterion

open ES

#print axioms ES.factorisation
#print axioms ES.dvd_of_dvd_mul_of_bezout
#print axioms ES.solution_gives_witness
#print axioms ES.witness_gives_solution
#print axioms ES.criterion_iff