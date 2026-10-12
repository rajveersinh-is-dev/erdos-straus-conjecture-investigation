# Main results

Each statement carries an evidence label (definitions in
`research/evidence_labels.md`) and a novelty judgement (conventions in
`research/known_results.md`).

Complete proofs of everything below are in `mathematics/proofs.md`.

---

## 0. The headline

> **The Erdős–Straus conjecture is not proved here.** What is proved is a sharp
> localisation of the difficulty, a set of structural theorems about the
> surviving case, and an obstruction theorem quantifying how little room a
> counterexample would have.

## 1. The exact two-unit-fraction criterion

> **Lemma 3 (PROVED HERE; formally verified in Lean — see `lean/`).**
> For `gcd(a,b) = 1` and `a, b ≥ 1`:
>
>       `a/b = 1/y + 1/z` for some `1 ≤ y ≤ z`
>   ⟺  some `u` divides `b²` with `1 ≤ u ≤ b` and `u ≡ −b (mod a)`.

This is the workhorse of the project: it converts an existential Diophantine
question into a finite divisor computation.

*Novelty:* **known in substance.** The same mathematical object appears as the
"divisors of `n²` in a single residue class modulo `e_n`" in Jiang (2026). Our
contribution is a self-contained, proved and machine-checked statement.

## 2. Localisation of the difficulty

> **Theorem 7 (ESTABLISHED IN PRIOR WORK; re-proved here).** `ES(n)` holds for
> every `n` **not** in the hard core `H` (Definition D.3). Equivalently: *any*
> counterexample to Erdős–Straus lies in `H`.

The four identities used, each proved explicitly in `proofs.md` §4:

| condition on `n` | identity |
|---|---|
| `n` even | `4/n = 1/(n/2) + 1/n + 1/n` |
| `n ≡ 3 (mod 4)` | `4/n = 1/((n+1)/4) + 1/(n(n+1)/2) + 1/(n(n+1)/2)` |
| `n ≡ 5 (mod 8)` | `4/n = 1/x + 1/(2x) + 1/(2nx)`, `x = (3n+1)/8` |
| `n ≡ 5 (mod 12)` | `4/n = 1/x + 1/(n(x+1)/3) + 1/(nx(x+1)/3)`, `x = (n+3)/4` |

*H* contains 29 298 integers up to `3·10⁶`: 23.4 % of the 125 000 integers
`≡ 1 (mod 24)` in that range, and 0.98 % of all integers.

## 3. No solution in the hard core has a repeated denominator

> **Theorem 8 (PROVED HERE).** Let `n ≡ 1 (mod 4)` be odd. Then `ES(n)` has a
> solution with `y = z` **iff** `n` has a prime divisor `≡ 3 (mod 4)`; and the
> same equivalence holds with `x = y` in place of `y = z`.
>
> **Corollary 9 (PROVED HERE).** If `n ∈ H` then **every** solution is
> asymmetric: `x < y < z`.

In the hardest case the two-denominator identities that solve every easy case
are *provably unavailable*: `4/n = 1/x + 2/y` is never solvable there.

*Novelty:* **known in spirit, `H`-version apparently new, priority not
certified.** Closely related to Jiang (2026)'s statement that the Type I and
Type II counts vanish for odd perfect squares, and to the classical Type I/II
split.

## 4. The `k`-sieve

> **Lemma 5 (PROVED HERE).** A prime witness is sufficient: if `B` has a prime
> divisor `q ≡ −B (mod A)` then a solution exists with that `x`.

> **Theorem 10 (PROVED HERE, both directions).** For `n ∈ H`, a solution in
> ordered form with `4x − n = 3` exists **iff** `(n+3)/4` has a prime divisor
> `≡ 2 (mod 3)`.

Exact, not merely sufficient. Verified with **zero** mismatches against the
brute-force criterion on all 3380 hard-core values `≤ 300000`
(`experiments/exp03_kcensus.py`).

## 5. An impossibility result

> **Theorem 11 (PROVED HERE).** Let `n ≡ 1 (mod 24)` and `k ≡ 3 (mod 4)` with
> `gcd(k,n) = 1`. Then `k | n² + 4` is impossible, so the witness `u = 1` can
> **never** produce a solution.

The proof uses the classical fact that every prime divisor of `n² + 4` is
`≡ 1 (mod 4)`. Any proof of Erdős–Straus for the hard core must therefore use a
*genuine* prime factor of one of the numbers `n(n+k)/g`.

*Novelty:* **uncertain.**

## 6. Closed-form solution families

> **Theorem 12 (PROVED HERE).** Let `n ≡ 1 (mod 4)`, `d ≥ 3`, `d ≡ 3 (mod 4)`,
> `gcd(d,n) = 1`, `x = (n+d)/4`. Then
>
> * **(F1')** if `d | n + 4c` with `c | x²`, `1 ≤ c ≤ x`: `ES(n)` holds;
> * **(F3')** if `d | n + c` with `c | n²`, `1 ≤ c ≤ n`: `ES(n)` holds.
>
> **Corollary 13 (PROVED HERE).** The `c = 1` instances are closed-form
> identities:
> * if `d | n+4`: `4/n = 1/x + 1/(n(x+1)/d) + 1/(n x(x+1)/d)`;
> * if `d | n+1`: `4/n = 1/x + 1/(x(n+1)/d) + 1/(n x(n+1)/d)`.

Both reduce to the single identity `1/x + d/(nx) = 4/n`; the content is that the
second term splits into two unit fractions.

*Novelty:* **known in substance** (classical parametric families).

## 7. An obstruction theorem for counterexamples

> **Theorem 14 (PROVED HERE).** If `n ∈ H` and `ES(n)` fails, then:
>
> * **(O1)** every prime divisor of `(n+3)/4` is `≡ 1 (mod 3)`;
> * **(O2)** every odd prime divisor of `n+1` is `≡ 1 (mod 4)`;
> * **(O3)** every prime divisor of `n+4` is `≡ 1 (mod 4)`;
> * **(O4)** for every `k ≡ 3 (mod 4)` with `k < 73`, the integer
>   `B_k = n(n+k)/4` has no divisor `u ≤ B_k` with
>   `u ≡ −B_k ≡ −n²·4^{−1} (mod k)`; in particular it has no prime divisor in
>   that residue class.

**Quantified consequence (COMPUTATIONALLY VERIFIED).** On `H ∩ [1, 600000]`
(6467 integers), (O1), (O2), (O3) alone leave 47.9 %, 53.1 %, 51.6 %
respectively, and jointly **12.36 %** (799 values); of those, only **16** need
`μ(n) > 23` (`experiments/exp05_obstruction.py`).

*Novelty:* **uncertain.**

## 8. Computed findings

> **(COMPUTATIONALLY VERIFIED)** On `H ∩ [1, 3·10⁶]` (29 298 integers) every
> `n` has a solution with `k ≤ 255`, and `μ(n) ≤ 59`, with the maximum attained
> at exactly `n = 118801` and `n = 806521`. The first solution of `118801` is
>
>       4/118801 = 1/29715 + 1/59875704 + 1/84724121160          (k = 59),
>
> and no `k < 59` works. Corollary 13 still solves it, via `d = 191 | (n+1)`:
>
>       4/118801 = 1/29748 + 1/18503256 + 1/2198205316056 .

> **(COMPUTATIONALLY VERIFIED)** Composite members of `H` are markedly easier:
> among `H ∩ [1, 3·10⁶]` the 2288 composite members all have `μ ≤ 15`, while
> the 27 010 prime members reach `μ = 59`.

> **(COMPUTATIONALLY VERIFIED)** Coverage on `H ∩ [1, 300000]` (3380 values):
> `k = 3` alone covers 50.8 %, `k = 23` 76.8 %, and `{3, 7, 11, 15, 23}`
> covers 3348/3380 = 99.05 %; adding `k = 27, 31` covers 3378. The closed forms
> `F1' ∪ F3'` cover 2920/3380 = 86.4 %.

> **(COMPUTATIONALLY VERIFIED)** The minimum number of *distinct admissible `k`*
> over `H ∩ [1, 6000]` is 3, attained at `n = 73` and `n = 193`. The minimum
> number of full solutions `(x,y,z)` over `H ∩ [1, 20000]` is 6, at `n = 193`.
> (These are different quantities; see `research/proof_attempts.md`, A8.)

## 9. What is NOT proved

* The Erdős–Straus conjecture. Not proved; not disproved.
* `ES(n)` for all `n ∈ H`. **OPEN** — by Theorem 7 this is the whole remaining
  problem, and it contains every prime `p ≡ 1 (mod 24)`.
* Any bound on `μ(n)` as `n → ∞`. **UNRESOLVED.**

## 10. The single most important obstacle

Every criterion proved here (Lemmas 5, Theorems 10, 11, 12) asks the same kind
of question about a linear function of `n`:

> does some explicit integer built from `n` — namely `(n+3)/4`, `n+1`, `n+4`,
> `n(n+k)/4`, … — have a prime divisor in a prescribed residue class modulo a
> small `k`?

For `n ∈ H` those integers are large and their residue classes modulo small `k`
are exactly what we would have to control. Nothing in this project (and nothing
known to us) forces such a prime divisor to exist. **That gap — not any
computational limitation — is where a solution to Erdős–Straus would have to
live.**
