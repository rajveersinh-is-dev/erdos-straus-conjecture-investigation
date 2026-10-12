# Definitions and notation

Throughout, `n, x, y, z, a, b, k, d, j, u, v, A, B, G` are **positive
integers** unless stated otherwise. All arithmetic in this project is exact
integer arithmetic; no floating point enters any mathematical statement.

---

## D.1 The Erdős–Straus equation

For `n ≥ 2` write

        ES(n)  :⇔  there exist x ≤ y ≤ z with   4/n = 1/x + 1/y + 1/z.

When `ES(n)` holds, `(x, y, z)` is a **solution** of `n`. The ordering
`x ≤ y ≤ z` makes the triple unique up to that ordering, so the set of
solutions is a well-defined finite set.

> The **Erdős–Straus conjecture** (Erdős–Straus, 1948) is: `ES(n)` holds for
> every `n ≥ 2`.

## D.2 Repeated denominators

A solution is called

* **of type (y = z)** if `y = z`, i.e. `4/n = 1/x + 2/y`;
* **of type (x = y)** if `x = y`, i.e. `4/n = 2/x + 1/z`;
* **asymmetric** if `x < y < z`.

> These are *our own* labels, defined only by the shape of the triple. They are
> **not** the "Type I / Type II" of Elsholtz–Tao (2011) or of Jiang (2026),
> which is a different classification; see `research/literature_review.md`,
> Remark LR-3.

## D.3 The hard core

        H  =  { n ≥ 2 :  n ≡ 1 (mod 24)  and  every prime divisor p of n
                                    satisfies  p ≡ 1 (mod 24) }.

Elements of `H` are **hard-core integers**: products of primes `≡ 1 (mod 24)`.
The first few are `73, 97, 193, 241, 313, 337, 409, 433, 457, …`.

> Theorem 7 of `mathematics/proofs.md` proves `ES(n)` for every `n` not in `H`.
> `H` is therefore exactly where the difficulty of the conjecture lives.

**Size.** `|H ∩ [1, 3·10⁶]| = 29 298`. Among the 125 000 integers `≡ 1 (mod 24)`
up to `3·10⁶` this is 23.4 %; among *all* integers up to `3·10⁶` it is 0.98 %.
(The comparison that matters is with `n ≡ 1 (mod 24)`, since the other residue
classes are settled by Theorem 7.)

## D.4 The `k`-parametrisation

Given a solution with `x ≤ y ≤ z`, put

        k := 4x − n .

By Lemma 1 (proofs.md) `n/4 < x ≤ 3n/4`, hence `1 ≤ k ≤ 2n`; and

        1/y + 1/z  =  (4x − n)/(n x)  =  4k / ( n (n + k) ).                (S)

If `n ≡ 1 (mod 4)` then necessarily `k ≡ 3 (mod 4)`. Writing `n = 24m + 1` and
`k = 4j − 1` gives

        x = 6m + j ,      1/y + 1/z = (4j − 1) / ( n (6m + j) ).           (S')

With

        G = gcd(4j−1, n(6m+j)) ,   A = (4j−1)/G ,   B = n(6m+j)/G

we have `gcd(A, B) = 1`.

## D.5 The minimal `k`

For `n ≡ 1 (mod 24)` define

        μ(n)  :=  min { k > 0 : k ≡ 3 (mod 4)  and  there is a solution of n
                          whose smallest denominator x satisfies 4x − n = k },

with `μ(n) = +∞` if the set is empty.

## D.6 Witnesses

A **witness** for a given `k` is an integer `u` satisfying

        u | B² ,      1 ≤ u ≤ B ,      u ≡ −B  (mod A).                   (W)

Lemma 3 of `proofs.md` proves that a solution with `4x − n = k` exists **if and
only if** a witness exists; when it does, with `v := B²/u`,

        y = (B + u)/A ,     z = (B + v)/A .                               (W′)

A **prime witness** is a witness `u` that is prime; Lemma 5 shows one is always
sufficient. Theorem 11 shows that `u = 1` is *never* a witness in the hard core.

## D.7 Computed quantities

* `solution_count(n)` counts distinct admissible `k` values (equivalently
  distinct smallest denominators `x`).
* `enumerate_solutions(n)` lists full triples `(x, y, z)`.

These are different quantities and are reported separately throughout; an early
version of this project conflated them (see `research/proof_attempts.md`, A8).
