# An exact criterion for the Erdős–Straus equation, the hard core in which its difficulty lives, and an obstruction theorem

## Abstract

We investigate the Erdős–Straus conjecture: for every integer `n ≥ 2` do there
exist positive integers `x, y, z` with `4/n = 1/x + 1/y + 1/z`? The conjecture
has been open since 1948 and we do not resolve it. We do establish a self-contained
set of structural results about the part of the problem that is not already
settled by the classical identities.

After deriving an exact divisibility criterion for the two-unit-fraction
equation `a/b = 1/y + 1/z`, we prove that any counterexample to Erdős–Straus must
lie in the *hard core*

        H = { n : n ≡ 1 (mod 24) and every prime divisor of n is ≡ 1 (mod 24) },

a set containing 29 298 integers up to three million — 23.4 % of the integers
`≡ 1 (mod 24)` in that range, and 0.98 % of all integers. We then show
that inside `H` no solution can have a repeated denominator, so the
two-denominator identities that solve every easy case are provably unavailable.
We derive a sharp necessary-and-sufficient criterion for the smallest possible
denominator `4x − n = 3`, prove that the trivial witness in the divisibility
criterion can never succeed, give two closed-form families of solutions, and
prove an obstruction theorem giving four explicit necessary conditions for `n`
to be a counterexample. Exact computation on the hard core up to `3 · 10^6`
shows that these conditions eliminate more than seven eighths of the candidates,
and identifies the integers of `H` on which the search is hardest.

**Keywords.** Erdős–Straus conjecture; Egyptian fractions; divisor criterion;
Euclidean division; hard core; obstruction.

---

## 1. Introduction

The Erdős–Straus conjecture, posed in 1948, asserts that for every `n ≥ 2` the
number `4/n` is a sum of three positive unit fractions. It is one of the oldest
unresolved problems in elementary number theory. It has been verified
computationally for `n ≤ 10^17`; that verification is a statement about a finite
range and contributes nothing to the general case.

The classical literature attacks the problem by exhibiting parametric
identities that cover residue classes of `n`; there are hundreds of such
families. Recently a second line of work has studied the *structure* of the
solution set rather than individual solutions — Elsholtz and Tao obtained
asymptotics for the number of solutions, and Jiang (2026) expressed the counts
exactly in terms of divisors of `n^2` lying in a prescribed residue class.

This paper sits in that second line. We make three contributions.

1. **Localisation.** We give a clean, self-contained proof that the whole
   difficulty is confined to the hard core `H` above — a strictly sharper
   statement than the familiar "it suffices to consider `n ≡ 1 (mod 24)`",
   because it also forces every prime factor.

2. **Structure.** We prove that within `H` every solution is asymmetric
   (`x < y < z`), i.e. the equation `4/n = 1/x + 2/y` is never solvable there.
   We derive an exact criterion for the smallest admissible value of `k = 4x − n`,
   prove an impossibility result about the most obvious candidate solution
   method, and give two closed-form families.

3. **Obstruction.** We give four explicit, provable necessary conditions for
   `n ∈ H` to be a counterexample, and quantify their joint strength
   computationally.

The proof strategy is uniform and is worth stating before the technical
material. Fix the smallest denominator `x` of a putative solution and put
`k = 4x − n`. A short argument confines `x` to `n/4 < x ≤ 3n/4`, and the
equation then reduces to a *two*-unit-fraction problem

        1/y + 1/z = 4k / ( n(n+k) ),

which we solve exactly by factoring a square. Writing `n = 24m+1` and
`k = 4j − 1` makes `k` range over `3, 7, 11, …` and converts the conjecture into
a sequence of finite divisor questions about explicit linear functions of `n`.
Everything below is a study of those questions.

A note on honesty. We do not claim priority for the main ideas: the divisor
criterion is the same mathematical object that appears in Jiang (2026), and
the parametric families of Section 6 are classical in substance. What we claim
is a complete, checked and self-contained treatment, plus the structural
results of Sections 4, 5 and 7, whose novelty we assess conservatively.

---

## 2. The basic reduction

Throughout, solutions are written in the form `x ≤ y ≤ z`; `ES(n)` denotes the
assertion that such a solution exists.

**Lemma 1.** If `ES(n)` then there is a solution with `n/4 < x ≤ 3n/4`.

*Proof.* Since `y, z ≥ x` we have `4/n = 1/x+1/y+1/z ≤ 3/x`, whence
`x ≤ 3n/4`. Since `1/y + 1/z > 0` we have `4/n > 1/x`, whence `x > n/4`. ∎

**Lemma 2.** Let `n ≡ 1 (mod 4)` and `n/4 < x ≤ 3n/4` with `x` integral, and
put `k = 4x − n`. Then `k ≡ 3 (mod 4)`, `1 ≤ k ≤ 2n`, and

        4/n − 1/x = 4k / ( n(n+k) ).

*Proof.* `k = −n (mod 4) = 3 (mod 4)`; the bounds on `k` follow from those on
`x`; and the identity follows from `n + k = 4x`. ∎

This already explains why the hard cases are `n ≡ 1 (mod 4)`: there `k` is
forced into the residue class `3 (mod 4)`, so the "second denominator" cannot
be split as freely as in the easy cases.

---

## 3. An exact criterion

**Lemma 3.** Let `a, b ≥ 1` with `gcd(a,b) = 1`. The following are equivalent.

* (a) there exist `1 ≤ y ≤ z` with `a/b = 1/y + 1/z`;
* (b) there is a divisor `u` of `b^2` with `1 ≤ u ≤ b` and `u ≡ −b (mod a)`.

*Proof.* (a) ⇒ (b). From `a/b = 1/y + 1/z` we get `ayz = b(y+z)`. Put
`u = ay − b` and `v = az − b`. Both are positive because `a/b > 1/y` and
`a/b > 1/z`. By construction `u ≡ v ≡ −b (mod a)`, and

        uv = a(ayz − b(y+z)) + b^2 = b^2 .

So `u | b^2`; and `y ≤ z` gives `u ≤ v`, whence `u ≤ b` from `uv = b^2`.

(b) ⇒ (a). Let `u | b^2`, `1 ≤ u ≤ b`, `u ≡ −b (mod a)`, and put `v = b^2/u`.
Then `v ≥ u`. Moreover `v ≡ −b (mod a)`: from `uv = b^2` and `u ≡ −b` we get
`(−b)v ≡ b^2 (mod a)`, i.e. `b(v+b) ≡ 0 (mod a)`, and `gcd(a,b) = 1` gives
`a | v + b`. Set `y = (b+u)/a`, `z = (b+v)/a`; these are positive integers with
`y ≤ z`, and

        ayz = ((b+u)(b+v))/a = (2b^2 + b(u+v))/a = b(y+z),

so `a/b = 1/y + 1/z`. ∎

*Remark.* The hypothesis `gcd(a,b) = 1` is used in exactly one place, to
deduce `v ≡ −b (mod a)` from `u ≡ −b (mod a)`.

**Corollary 4.** Let `n = 24m + 1`, `j ≥ 1`, `x = 6m + j` with `n/4 < x ≤ 3n/4`,
and put `k = 4j − 1`, `G = gcd(4j−1, n(6m+j))`, `A = (4j−1)/G`,
`B = n(6m+j)/G`. Then there exist `y, z ≥ 1` with `4/n = 1/x + 1/y + 1/z` if and
only if some `u | B^2` satisfies `u ≤ B` and `u ≡ −B (mod A)`; in that case
`y = (B+u)/A` and `z = (B+B^2/u)/A`.

This is the criterion the computations use. It converts the Diophantine
question into a finite divisor computation, which is why the experiments in
Section 8 — 29 298 hard-core integers — run in seconds.

---

## 4. Localisation: the hard core

**Lemma 5 (descent).** If `ES(d)` then `ES(n)` for every multiple `n` of `d`.

*Proof.* With `n = kd` and `4/d = 1/x+1/y+1/z`, multiply by `1/k`. ∎

**Theorem 6.** `ES(n)` holds for every `n` that is not in

        H = { n ≥ 2 : n ≡ 1 (mod 24), every prime divisor p of n with p ≡ 1 (mod 24) }.

*Proof.* Four identities, each verified directly.

* (I1) `2 | n`: `4/n = 1/(n/2) + 1/n + 1/n`.
* (I2) `n ≡ 3 (mod 4)`: with `x = (n+1)/4`, `y = z = n(n+1)/2`,
  `1/x + 1/y + 1/z = 4/(n+1) + 4/(n(n+1)) = 4/n`.
* (I3) `n ≡ 5 (mod 8)`: with `x = (3n+1)/8`, `y = 2x`, `z = 2nx`,
  `1/x+1/(2x)+1/(2nx) = (3n+1)/(2nx) = 8x/(2nx) = 4/n`.
* (I4) `n ≡ 5 (mod 12)`: with `x = (n+3)/4` (so `x ≡ 2 (mod 3)`),
  `y = n(x+1)/3`, `z = nx(x+1)/3`, we get
  `1/x + 3/(n(x+1)) + 3/(nx(x+1)) = 1/x + 3/(nx) = 4/n`.

Now suppose `ES(n)` fails. Then `n` is odd by (I1), `n ≡ 1 (mod 4)` by (I2),
`n ≡ 1 (mod 12)` by (I4), and `n ≡ 1 (mod 8)` by (I3); hence `n ≡ 1 (mod 24)`.
For any prime `p | n`, the failure of `ES(n)` together with Lemma 5 forces the
failure of `ES(p)`, and repeating the above gives `p ≡ 1 (mod 24)`. So `n ∈ H`. ∎

**Remark.** The classical statement is "it suffices to consider `n ≡ 1 (mod 24)`".
Theorem 6 is strictly sharper: it forces every prime factor to be `≡ 1 (mod 24)`
as well. The price is two extra identities, (I3) and (I4).

---

## 5. Asymmetry in the hard core

**Theorem 7.** Let `n ≡ 1 (mod 4)` be odd.

* (a) `ES(n)` has a solution with `y = z` **iff** `n` has a prime divisor
  `≡ 3 (mod 4)`.
* (b) `ES(n)` has a solution with `x = y` **iff** `n` has a prime divisor
  `≡ 3 (mod 4)`.

*Proof.* (a) Suppose `4/n = 1/x + 2/y` with `x ≤ y`, and put `k = 4x − n`. By
Lemma 2, `k ≡ 3 (mod 4)` is odd and `k/(nx) = 2/y`, so `k | 2nx`, hence (as `k`
is odd) `k | nx = n(n+k)/4`, hence `k | n(n+k)`, hence `k | n^2`; and
`x ≤ y = 2nx/k` gives `k ≤ 2n`. Conversely, if `k | n^2`, `k ≡ 3 (mod 4)` and
`k ≤ 2n`, then `x = (n+k)/4` is integral with `n/4 < x ≤ 3n/4`, `k | 2nx`
follows from `k | n(n+k)`, and `y = 2nx/k ≥ x` gives the solution. Finally
`k | n^2` with `k ≡ 3 (mod 4)` forces some prime `q ≡ 3 (mod 4)` to divide `k`,
hence `n`; conversely if `p ≡ 3 (mod 4)` divides `n` then `k = p` works, since
`p ≤ n ≤ 2n`.

(b) Suppose `4/n = 2/x + 1/z` with `x ≤ z`. Then `4x − 2n > 0` divides `nx`; put
`t = 2x − n > 0`, which is odd. Then `2t | nx = n(n+t)/2`, i.e.
`4t | n(n+t)`, whence `t | n^2`, and `4 | n+t` (since `n` is odd) gives
`t ≡ −n ≡ 3 (mod 4)`; also `x ≤ z = nx/(2t)` gives `t ≤ n/2`. Conversely these
conditions suffice, with `x = (n+t)/2` and `z = nx/(2t)`. As in (a), such a `t`
exists iff `n` has a prime divisor `≡ 3 (mod 4)` — and here `p ≤ n/2`
automatically, because `p > n/2` would force `n = p ≡ 3 (mod 4)`. ∎

**Corollary 8.** If `n ∈ H` then every solution of `n` is asymmetric:
`x < y < z`.

*Proof.* `H` consists of odd `n ≡ 1 (mod 4)` all of whose prime divisors are
`≡ 1 (mod 24)`, hence `≡ 1 (mod 4)`. Theorem 7 excludes `y = z` and `x = y`; and
`x = z` forces all three equal. ∎

*Interpretation.* Inside the hard core the equation `4/n = 1/x + 2/y` — the
form that solves (I1), (I2) and most easy cases — is *never* solvable. Whatever
solution exists must use three genuinely distinct denominators.

---

## 6. The `k`-sieve

By Corollary 4, each `k = 4j − 1` gives a finite test. The first one is sharp
in a satisfying way.

**Theorem 9.** Let `n ∈ H` and `x = (n+3)/4`. Then there is a solution with
`4x − n = 3` **iff** `(n+3)/4` has a prime divisor `≡ 2 (mod 3)`.

*Proof.* By Corollary 4 with `j = 1`: `3` is prime, `3 ∤ n` because
`n ≡ 1 (mod 3)`, and `3 ∤ x` because `x = 6m+1`; so `A = 3`, `B = nx ≡ 1 (mod 3)`,
and a solution exists iff `B^2` has a divisor `u ≤ B` with `u ≡ 2 (mod 3)`. Such
a `u` exists iff `B` has a prime divisor `≡ 2 (mod 3)`: one direction by taking
`u` to be that prime, the other because a number `≡ 2 (mod 3)` must have a prime
factor `≡ 2 (mod 3)`. Finally every prime divisor of `n` is `≡ 1 (mod 3)`, so
`B = nx` has such a prime iff `x` does. (The ordering `x ≤ y` holds because
`y − x = (x(n−3) + q)/3 > 0` for `n ≥ 3`.) ∎

For a general `n ≡ 1 (mod 24)` the same proof gives: a solution with
`4x − n = 3` exists iff `n` **or** `(n+3)/4` has a prime divisor `≡ 2 (mod 3)`.

**Theorem 10 (impossibility).** Let `n ≡ 1 (mod 24)` and `k ≡ 3 (mod 4)` with
`gcd(k,n) = 1`. Then `k ∤ n^2 + 4`; consequently the witness `u = 1` of
Corollary 4 never applies.

*Proof.* Put `x = (n+k)/4`; then `gcd(k,x) = 1` (because `4x = n+k`), so `A = k`
and `B = nx`. The witness `u = 1` requires `k | nx + 1`, and since
`4nx = n(n+k) ≡ n^2 (mod k)` this is equivalent to `k | n^2 + 4`. Now `n` is odd,
so `n^2+4` is odd; if `p | n^2 + 4` is prime, then `(n·2^{-1})^2 ≡ −1 (mod p)`,
so `−1` is a quadratic residue mod `p` and `p ≡ 1 (mod 4)`. Every divisor of
`n^2+4` is therefore `≡ 1 (mod 4)`, and `k ≡ 3 (mod 4)` cannot divide it. ∎

*Interpretation.* The most obvious construction — splitting the second term
without using any factor of `n` — is not merely unhelpful, it is impossible.
Any solution must be built from a genuine prime factor of one of the integers
`n(n+k)/g`.

**Theorem 11 (closed forms).** Let `n ≡ 1 (mod 4)`, `d ≥ 3`, `d ≡ 3 (mod 4)`,
`gcd(d,n) = 1`, `x = (n+d)/4`.

* (F1') If `d | n + 4c` for some `c` with `1 ≤ c ≤ x` and `c | x^2`, then
  `ES(n)`.
* (F3') If `d | n + c` for some `c` with `1 ≤ c ≤ n` and `c | n^2`, then
  `ES(n)`.

*Proof.* Then `gcd(d,x) = 1` and `G = 1`, `A = d`, `B = nx`. For (F1') take
`u = nc`: then `u | B^2` (as `c | x^2`), `u ≤ B` (as `c ≤ x`), and
`nc ≡ −nx (mod d)` because `gcd(x,d) = 1` and `4c ≡ −4x ≡ −n (mod d)`.
For (F3') take `u = xc`, using `gcd(x,d) = 1` and `c ≡ −n (mod d)`. Apply
Corollary 4. ∎

**Corollary 12.** Under the hypotheses of Theorem 11:

* if `d | n + 4`, then `4/n = 1/x + 1/(n(x+1)/d) + 1/(n x(x+1)/d)`;
* if `d | n + 1`, then `4/n = 1/x + 1/(x(n+1)/d) + 1/(n x(n+1)/d)`.

*Proof.* Specialise to `c = 1` in (F1') and (F3'), or verify directly: both
reduce to `1/x + d/(nx) = 4/n`, since `4x = n + d`. ∎

Examples: `4/5 = 1/2 + 1/4 + 1/20` (`d = 3 | 5+4`),
`4/13 = 1/5 + 1/10 + 1/130` (`d = 7 | 13+1`),
`4/17 = 1/5 + 1/34 + 1/170` (`d = 3 | 17+4`).

---

## 7. An obstruction theorem

**Theorem 13.** Let `n ∈ H` and suppose `ES(n)` fails. Then

* **(O1)** every prime divisor of `(n+3)/4` is `≡ 1 (mod 3)`;
* **(O2)** every odd prime divisor of `n+1` is `≡ 1 (mod 4)`;
* **(O3)** every prime divisor of `n+4` is `≡ 1 (mod 4)`;
* **(O4)** for every `k ≡ 3 (mod 4)` with `k < 73`, the integer
  `B_k = n(n+k)/4` has no divisor `u` with `1 ≤ u ≤ B_k` and
  `u ≡ −B_k (mod k)`.

*Proof.* (O1) is Theorem 9 read contrapositively, together with
`3 ∤ (n+3)/4` since `(n+3)/4 = 6m+1`. For (O2): if an odd prime `q ≡ 3 (mod 4)`
divided `n+1`, then `gcd(q,n) = 1` (because `q | n+1`) and Corollary 12 would
give `ES(n)`. For (O3): if `q ≡ 3 (mod 4)` divided `n+4`, then `n+4` is odd so
`q` is odd, and `gcd(q,n) = 1` (else `q | 4`), again contradicting Corollary 12.
(O4) is Corollary 4 read contrapositively; the condition `gcd(k,n) = 1` needed
there is automatic for `k < 73`, since every prime divisor of `n` is
`≡ 1 (mod 24)` and hence `≥ 73`. ∎

---

## 8. Computation

All computations use exact integer arithmetic; no floating point is involved
anywhere. The algorithm is Corollary 4: for each `k = 4j − 1`, factor
`B = n(n+k)/G` and test its divisors of `B^2` against the congruence.

Results (exact, reproducible via `experiments/`):

* `ES(n)` holds for every `n ∉ H` with `n ≤ 20000`, and for every
  `n ≤ 2000` (including `H`).
* `H` contains 3380 integers up to `300000` and 29298 up to `3·10^6`.
* Theorem 9 was verified with **zero** mismatches against a brute-force search
  on all 3380 hard-core values up to `300000`; Theorem 10 with zero violations
  on the same set.
* Coverage by a single `k`: `k = 3` covers 50.8 %, `k = 23` 76.8 %,
  `k = 7` 75.5 %, `k = 15` 74.1 % of `H ∩ [1, 300000]`. The set
  `{3, 7, 11, 15, 23}` covers 3348 of 3380 (99.05 %).
* The closed forms of Theorem 11 together cover 2920 of 3380 (86.4 %).
* Obstruction: on `H ∩ [1, 600000]` (6467 values), (O1), (O2), (O3) alone leave
  47.9 %, 53.1 %, 51.6 % respectively, and jointly **12.36 %**; of the 799
  survivors, only 16 need `μ(n) > 23`.
* **No hard-core integer up to `3·10^6` lacks a solution with `k ≤ 255`.**
* Defining `μ(n)` as the smallest admissible `k`: `μ` reaches 59, attained at
  exactly `n = 118801` and `n = 806521`. Explicitly
  `4/118801 = 1/29715 + 1/59875704 + 1/84724121160` is the *first* solution of
  118801, and none with `k < 59` exists. Corollary 12 still solves it, via
  `d = 191 | (n+1)`: `4/118801 = 1/29748 + 1/18503256 + 1/2198205316056`.
* Composite members of `H` are markedly easier: among `H ∩ [1, 3·10^6]` the
  2315 composite members all satisfy `μ ≤ 15` — the 27 of them that are prime
  powers `p^e`, `e ≥ 2`, satisfy `μ ≤ 11` — while the 26 983 prime members
  reach `μ = 59`.

These are finite-range statements. They are reported as evidence for the
structure described above and are never used as proof of a universal claim.

---

## 9. What remains open

The conjecture itself. By Theorem 6 it is equivalent to `ES(n)` for every
`n ∈ H`, and `H` contains every prime `p ≡ 1 (mod 24)`.

Every criterion we proved asks whether some explicit integer built from `n` —
`(n+3)/4`, `n+1`, `n+4`, `n(n+k)/4` — has a prime divisor in a prescribed
residue class modulo a small `k`. For `n ∈ H` those integers are large and
their residue-class structure is precisely what is uncontrolled. That, and not
any computational limitation, is where a proof would have to live.

Three specific open questions:

1. Is `μ` bounded on `H`? (It reaches 59 on the tested range.)
2. Is there `n ∈ H` with no solution for any `k < 100`?
3. Is every composite `n ∈ H` solvable with `k ≤ 15`? Verified on
   `H ∩ [1, 3·10^6]`; a proof would be a genuine advance.

---

## 10. Relation to prior work

The divisor criterion of Lemma 3 is the same mathematical object as the
"divisors of `n^2` in a single residue class modulo `e_n`" appearing in the
counting identity of Jiang (2026). The parametric identities of Corollary 12
are classical in substance. We make no claim of priority; see
`research/literature_review.md` for the full picture and for the limits of our
search.

## References

* P. Erdős, E. G. Straus. *On a Diophantine equation of Erdős and Straus.*
  Acta Arith. **3** (1948), 363–367.
* C. Elsholtz, T. Tao. *Counting the number of solutions to the Erdős–Straus
  equation on unit fractions.* arXiv:1107.1010 (2011).
* M. A. Lopez. *A Complete Congruence System for the Erdős–Straus Conjecture.*
  arXiv:2404.01508 (2024).
* M. Bello-Hernández. *A Divisor Parametrization for the Erdős–Straus
  Conjecture.* arXiv:2606.10922 (2026).
* X. Jiang. *Counting Type I and Type II solutions of the Erdős–Straus
  equation: concentration, local obstructions, and a pointwise comparison.*
  arXiv:2609.09204 (2026).
