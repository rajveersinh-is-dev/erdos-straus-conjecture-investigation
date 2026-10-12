# Proofs

Complete, self-contained proofs of every theorem in `main_results.md`.
Numbering is stable and referenced from the rest of the repository.

Throughout: all variables are positive integers unless stated otherwise.

---

## 1. The basic search window

**Lemma 1.** If `ES(n)` holds, then there is a solution with

        n/4  <  x  ≤  3n/4 .

**Proof.** Suppose `x ≤ y ≤ z` and `4/n = 1/x + 1/y + 1/z`.

*Upper bound.* Since `y, z ≥ x`, each of `1/x, 1/y, 1/z` is at most `1/x`, so
`4/n = 1/x+1/y+1/z ≤ 3/x`. Multiplying by `x > 0` gives `4x ≤ 3n`, i.e.
`x ≤ 3n/4`.

*Lower bound.* `1/y + 1/z > 0` because `y, z` are positive, hence `4/n > 1/x`,
so `4x > n`, i.e. `x > n/4`. ∎

**Remark 1.1.** Lemma 1 makes the set of admissible `x` finite. Nothing later
uses the bound as a *computational* device; it is used to make the criterion of
§3 a finite question.

---

## 2. The `k`-parametrisation

**Lemma 2.** Let `n ≡ 1 (mod 4)`, let `x` be an integer with `n/4 < x ≤ 3n/4`,
and put `k = 4x − n`. Then

1. `k ≡ 3 (mod 4)` and `1 ≤ k ≤ 2n`;
2. `4/n − 1/x = 4k/(n(n+k))`.

**Proof.** (1) `k = −n (mod 4) = 3 (mod 4)`. From `x > n/4` we get `k > 0`, i.e.
`k ≥ 1`; from `x ≤ 3n/4` we get `k ≤ 3n − n = 2n`.

(2) Since `n + k = 4x`,

        4/n − 1/x = (4x − n)/(nx) = k/(nx) = k/(n(n+k)/4) = 4k/(n(n+k)). ∎

**Corollary 2.1.** If `n = 24m+1` and `k = 4j−1` then `x = 6m+j` and

        4/n − 1/x = (4j−1)/( n(6m+j) ).

**Proof.** `4x − n = k` gives `x = (n+k)/4 = (24m+1+4j−1)/4 = 6m+j`; and
`n(n+k) = 4nx`, so `4k/(n(n+k)) = k/(nx) = (4j−1)/(n(6m+j))`. ∎

---

## 3. The exact criterion

**Lemma 3 (two-unit-fraction criterion).** Let `a, b ≥ 1` with `gcd(a,b) = 1`.
The following are equivalent.

* (a) there exist `1 ≤ y ≤ z` with `a/b = 1/y + 1/z`;
* (b) there is a divisor `u` of `b²` with `1 ≤ u ≤ b` and `u ≡ −b (mod a)`.

**Proof.**

*(a) ⇒ (b).* From `a/b = 1/y+1/z` we get `ayz = b(y+z)`. Set

        u := ay − b ,      v := az − b .

Both are **positive**: `a/b > 1/y` because `1/z > 0`, so `ay > b`; similarly
`az > b`. By construction `u ≡ v ≡ −b (mod a)`. Moreover

        uv = a²yz − ab(y+z) + b² = a·(ayz − b(y+z)) + b² = b² ,

using `ayz = b(y+z)`. So `u | b²`. Finally `y ≤ z` gives `u ≤ v`, and
`u·v = b²` with `u ≤ v` forces `u² ≤ b²`, i.e. `u ≤ b`.

*(b) ⇒ (a).* Let `u | b²`, `1 ≤ u ≤ b`, `u ≡ −b (mod a)`, and put `v := b²/u`.
Then `v ≥ u` (because `u ≤ b` and `uv = b²`), so `v` is a positive integer.
Moreover `v ≡ −b (mod a)`: from `uv = b²` and `u ≡ −b` we get
`(−b)v ≡ b² (mod a)`, i.e. `b(v+b) ≡ 0 (mod a)`; since `gcd(a,b) = 1` this
implies `a | v + b`.

Set `y := (b+u)/a` and `z := (b+v)/a`. These are integers because
`u ≡ v ≡ −b (mod a)`, and positive because `b, u, v > 0`; also `y ≤ z` because
`u ≤ v`. Finally

        a·y·z = ((b+u)(b+v))/a
              = ( b² + b(u+v) + uv )/a
              = ( 2b² + b(u+v) )/a          (since uv = b²)
              = b·(2b + u + v)/a
              = b·(y+z) ,

so `ayz = b(y+z)`, i.e. `a/b = 1/y + 1/z`. ∎

**Remark 3.1.** The hypothesis `gcd(a,b) = 1` is used in exactly one place: to
deduce `v ≡ −b (mod a)` from `u ≡ −b (mod a)`.

**Lemma 4 (the `k`-criterion).** Let `n = 24m+1`, `j ≥ 1`, `x = 6m+j` with
`n/4 < x ≤ 3n/4`. Put `k = 4j−1`, `G = gcd(4j−1, n(6m+j))`, `A = (4j−1)/G`,
`B = n(6m+j)/G`. Then there exist `y, z ≥ 1` with `4/n = 1/x + 1/y + 1/z` **iff**
there is a divisor `u` of `B²` with `1 ≤ u ≤ B` and `u ≡ −B (mod A)`; and when
such a `u` exists we may take `y = (B+u)/A` and `z = (B+B²/u)/A`.

**Proof.** By Corollary 2.1, `4/n − 1/x = (4j−1)/(n(6m+j)) = A/B`, and
`gcd(A,B) = 1` by the definition of `G`. Lemma 3 applies verbatim, and its
formulas for `y` and `z` are exactly those stated. ∎

**Remark 4.1 (the ordering `x ≤ y ≤ z`).** Lemma 4 places no condition `x ≤ y`;
the `u` it produces may give `y < x`. We claim a *solution in ordered form*
only where the produced `y` is verified to satisfy `y ≥ x`:

* in the search algorithms (`src/es_theory.py`, `src/es_sieve.py`) the test
  `y ≥ x` is applied explicitly;
* in Theorems 8, 10, 12 and Corollary 13 the inequality is verified below.

Conversely, if a solution in ordered form with smallest denominator `x` exists,
Lemma 3's necessity direction produces a witness `u`, so the criterion remains a
valid *necessary* condition in ordered form. ∎

**Lemma 5 (prime witnesses suffice).** Under Lemma 4's hypotheses, if `B` has a
prime divisor `q` with `q ≡ −B (mod A)`, then there exist `y, z ≥ 1` with
`4/n = 1/x + 1/y + 1/z`.

**Proof.** Take `u = q`. Then `q | B` implies `q | B²`; `q ≤ B` since `q | B`;
and the congruence is assumed. Lemma 4 applies. ∎

---

## 4. Localisation of the difficulty

**Lemma 6 (inheritance).** If `ES(d)` then `ES(n)` for every `n` that is a
positive multiple of `d`.

**Proof.** Write `n = kd` and let `4/d = 1/x+1/y+1/z`. Then

        4/n = (d/n)(4/d) = (1/k)(1/x+1/y+1/z)
            = 1/(kx) + 1/(ky) + 1/(kz). ∎

**Theorem 7.** `ES(n)` holds for every `n` not in `H`.

**Proof.** We first record four identities.

**(I1)** If `2 | n`: `4/n = 1/(n/2) + 1/n + 1/n`, since `2/n + 1/n + 1/n = 4/n`.

**(I2)** If `n ≡ 3 (mod 4)` (so `n` is odd): put `x = (n+1)/4` and
`y = z = n(n+1)/2`. Then

        1/x + 1/y + 1/z = 4/(n+1) + 4/(n(n+1)) = 4(n+1)/(n(n+1)) = 4/n .

**(I3)** If `n ≡ 5 (mod 8)`: put `x = (3n+1)/8`. Writing `n = 8a+5` gives
`3n+1 = 24a+16`, so `x = 3a+2` is an integer. With `y = 2x`, `z = 2nx`:

        1/x + 1/y + 1/z = 1/x + 1/(2x) + 1/(2nx)
                       = 3/(2x) + 1/(2nx)
                       = (3n+1)/(2nx)
                       = 8x/(2nx) = 4/n .

**(I4)** If `n ≡ 5 (mod 12)`: put `x = (n+3)/4`. Here `n ≡ 1 (mod 4)` (so `x` is
an integer) and `4x = n+3 = 12a+8 = 4(3a+2)`, hence `x = 3a+2 ≡ 2 (mod 3)`, so
`3 | x+1`. With `y = n(x+1)/3` and `z = nx(x+1)/3` (both integers):

        1/x + 1/y + 1/z
          = 1/x + 3/(n(x+1)) + 3/(nx(x+1))
          = 1/x + 3x/(nx(x+1)) + 3/(nx(x+1))
          = 1/x + 3(x+1)/(nx(x+1))
          = 1/x + 3/(nx)
          = (n+3)/(nx) = 4x/(nx) = 4/n .

Now suppose, for contradiction, that `ES(n)` fails and `n` is not in `H`.

* By (I1), `n` is odd.
* By (I2), `n ≡ 1 (mod 4)`.
* Since `n` is odd and `n ≡ 1 (mod 4)`, we have `n ≡ 1` or `5 (mod 12)`; by
  (I4) the latter is excluded, so `n ≡ 1 (mod 12)`, i.e. `n ≡ 1 (mod 3)`.
* Since `n ≡ 1 (mod 4)`, we have `n ≡ 1` or `5 (mod 8)`; by (I3) the latter is
  excluded, so `n ≡ 1 (mod 8)`.

Consequently `n ≡ 1 (mod 24)`.

Now let `p` be any prime divisor of `n`. If `ES(p)` held, Lemma 6 (with `d = p`,
`n` a multiple of `p`) would give `ES(n)`, contradicting our assumption. So
`ES(p)` fails, and the preceding paragraph — applied to `p` — shows
`p ≡ 1 (mod 24)`.

Every prime divisor of `n` is `≡ 1 (mod 24)` and `n ≡ 1 (mod 24)`, so `n` is in
`H`, contradicting the hypothesis. ∎

**Remark 7.1.** The classical statement is "it suffices to consider
`n ≡ 1 (mod 24)`". Theorem 7 is strictly sharper: it forces every prime factor
to be `≡ 1 (mod 24)` as well. The price is two extra identities, (I3) and (I4).

---

## 5. Repeated denominators

Throughout this section `n ≡ 1 (mod 4)` is odd.

**Theorem 8(a).** `ES(n)` has a solution with `y = z` **iff** `n` has a prime
divisor `p ≡ 3 (mod 4)`.

**Proof.** Suppose `4/n = 1/x + 2/y` with `x ≤ y`; put `k = 4x − n` (Lemma 2).
Then `k ≡ 3 (mod 4)` is odd and

        k/(nx) = 2/y ,   hence   k·y = 2nx  and  k | 2nx .

As `k` and `n` are odd, `k | nx = n(n+k)/4`; since `4 | n+k`, this says
`4k | n(n+k)`. As `k` is odd, `k | n(n+k)`, and
`n(n+k) = n² + nk ≡ n² (mod k)`, so `k | n²`. Also `x ≤ y = 2nx/k` gives
`k ≤ 2n`.

Conversely, suppose `k | n²`, `k ≡ 3 (mod 4)`, `k ≤ 2n`. Then `x = (n+k)/4` is
an integer (as `n ≡ 1`, `k ≡ 3 (mod 4)`), and `n/4 < x ≤ 3n/4`. Since
`k | n²` and `k | nk`, we get `k | n² + nk = n(n+k)`; `k` odd then gives
`k | n(n+k)/2 = 2nx`. Set `y = 2nx/k`; this is an integer and `y ≥ x` because
`k ≤ 2n`. Finally `4/n − 1/x = k/(nx) = 2/y`, so `4/n = 1/x + 1/y + 1/y` with
`x ≤ y`. ∎

**Theorem 8(b).** `ES(n)` has a solution with `x = y` **iff** `n` has a prime
divisor `p ≡ 3 (mod 4)`.

**Proof.** Suppose `4/n = 2/x + 1/z` with `x ≤ z`. Then

        4/n − 2/x = (4x − 2n)/(nx) = 1/z ,

so `4x − 2n > 0` (as `1/z > 0`) and `4x − 2n` divides `nx`. Put `t = 2x − n`;
`t > 0` and `t` is odd. Then `4x − 2n = 2t` and `2x = n+t`, so `x = (n+t)/2`
and

        2t | nx = n(n+t)/2   ⟺   4t | n(n+t) .                              (*)

From (*) and `gcd(t,4) = 1` (as `t` is odd) we get `t | n(n+t) = n² (mod t)`,
i.e. `t | n²`. Moreover `4 | n(n+t)` and `n` odd force `n+t ≡ 0 (mod 4)`, i.e.
`t ≡ −n ≡ 3 (mod 4)`. Finally `x ≤ z = nx/(2t)` gives `2t ≤ n`.

Conversely, suppose `t | n²`, `t ≡ 3 (mod 4)`, `t ≤ n/2`. Since `n` and `t` are
both odd, `x = (n+t)/2` is an integer, and `n/4 < x ≤ 3n/4`. As before
`t | n²` and `t | nt` give `t | n(n+t)`, and `t` odd gives `2t | n(n+t)/2`;
together with `t ≡ 3 (mod 4)` and `n ≡ 1 (mod 4)` this gives `4 | n+t`, hence
`4t | n(n+t)`, i.e. (*). Set `z = nx/(2t)`, an integer with `z ≥ x`. Then
`4/n − 2/x = 2t/(nx) = 1/z`. ∎

**Final step of Theorem 8.** In both parts, the condition "`k` (resp. `t`)
divides `n²` and is `≡ 3 (mod 4)`" is equivalent to "`n` has a prime divisor
`≡ 3 (mod 4)`":

*If such a `k` (resp. `t`) exists:* a number `≡ 3 (mod 4)` cannot be a product
of primes all `≡ 1 (mod 4)`; so some prime `q ≡ 3 (mod 4)` divides it, and
`q | n²` gives `q | n`.

*If `n` has a prime divisor `p ≡ 3 (mod 4)`:* in part (a) take `k = p`; then
`k | n²`, `k ≡ 3 (mod 4)` and `k = p ≤ n ≤ 2n`. For part (b) we need `t ≤ n/2`;
if `p ≤ n/2` take `t = p`. If `p > n/2`, then `n/p < 2`, so `n/p = 1` and
`n = p ≡ 3 (mod 4)`, contradicting `n ≡ 1 (mod 4)`. Hence `t = p` always works. ∎

**Corollary 9.** If `n` is in the hard core then every solution of `n` is
asymmetric (`x < y < z`).

**Proof.** `H` consists of odd `n ≡ 1 (mod 4)` whose prime divisors are all
`≡ 1 (mod 24)`, hence `≡ 1 (mod 4)`. Theorem 8 then excludes `y = z` and
`x = y`. If `x = z` then `x = y = z`, which forces `y = z`, also excluded. So
`x < y < z`. ∎

---

## 6. The sharp `k = 3` criterion

**Theorem 10.** Let `n` be in the hard core and `x = (n+3)/4`. Then there is a
solution in ordered form (`x ≤ y ≤ z`) of `n` **iff** `(n+3)/4` has a prime
divisor `≡ 2 (mod 3)`.

**Proof.** By Corollary 2.1, `1/y + 1/z = 3/(nx)`. Now `3` is prime, `n ≡ 1 (mod 3)`
gives `3 ∤ n`, and `x = 6m+1 ≡ 1 (mod 3)` gives `3 ∤ x`; so
`G = gcd(3, nx) = 1`, `A = 3`, `B = nx`, and `B ≡ 1·1 = 1 (mod 3)`.
Lemma 4 says `y, z ≥ 1` with `4/n = 1/x+1/y+1/z` exist iff there is
`u | B²` with `1 ≤ u ≤ B` and `u ≡ −1 ≡ 2 (mod 3)`.

*Claim:* such a `u` exists iff `B` has a prime divisor `≡ 2 (mod 3)`.

*If:* such a prime `q` satisfies `q | B`, hence `q | B²` and `q ≤ B`, and
`q ≡ 2 (mod 3)`; take `u = q`.
*Only if:* if `u | B²` and `u ≡ 2 (mod 3)`, then `u > 1` (since `1 ≡ 1 (mod 3)`)
and `u` has a prime factor `q ≡ 2 (mod 3)`; as `q | u | B²` we get `q | B`.

Finally, `B = nx` and `n` is in the hard core, so every prime divisor of `n` is
`≡ 1 (mod 24)` and hence `≡ 1 (mod 3)`. Therefore `B = nx` has a prime divisor
`≡ 2 (mod 3)` iff `x = (n+3)/4` does. ∎

**Remark 6.0 (the general case).** For an arbitrary `n ≡ 1 (mod 24)` the same
proof gives: *there is a solution with `4x − n = 3` iff `n` **or** `(n+3)/4` has
a prime divisor `≡ 2 (mod 3)`.* The restriction to the hard core removes
exactly the alternative "`n` has one".

**Remark 6.1 (the ordering `x ≤ y ≤ z`).** In the "if" direction the produced
solution is `y = (B+q)/3`, `z = (B+B²/q)/3`, and

        y − x = (nx + q)/3 − x = ( x(n−3) + q ) / 3 > 0

because `n ≥ 25 > 3` (as `n ∈ H` and `n ≡ 1 (mod 24)`). So the solution obtained
is in ordered form, as claimed. ∎

---

## 7. An impossibility result

**Theorem 11.** Let `n ≡ 1 (mod 24)` and `k ≡ 3 (mod 4)` with `gcd(k,n) = 1`.
Then `k | n² + 4` is impossible. Consequently the witness `u = 1` of Lemma 4 can
never produce a solution in this setting.

**Proof.** Put `x = (n+k)/4`. Since `4x = n+k` and `k` is odd, `gcd(k,x) = 1`
(because `gcd(k,x) | gcd(k,n) = 1`); together with `gcd(k,n) = 1` this gives
`G = gcd(k,nx) = 1`, so `A = k` and `B = nx`.

The witness `u = 1` satisfies `1 ≡ −B (mod k)`, i.e. `k | B + 1 = nx+1`. Since
`4nx = n(n+k) = n² + nk`, multiplying by `4` and reducing modulo `k` shows that
this is equivalent to `k | n² + 4`.

Now `n` is odd, so `n²+4` is odd. Let `p` be any prime divisor of `n²+4`; `p` is
odd and `p ∤ n` (else `p | 4`, impossible). Then `n² ≡ −4 (mod p)`, so
`(n·2^{−1})² ≡ −1 (mod p)`: `p ≡ 1 (mod 4)`, because `−1` is a quadratic residue
modulo an odd prime `p` only if `p ≡ 1 (mod 4)`. Hence every prime divisor of
`n²+4` is `≡ 1 (mod 4)`, and therefore every positive divisor of `n²+4` is
`≡ 1 (mod 4)`. But `k ≡ 3 (mod 4)`, so `k` is not a divisor of `n²+4`. ∎

**Remark 7.1.** Theorem 11 is an impossibility result, not a solution: it shows
that the most obvious way of splitting the second term (`u = 1`) can never
work, so any proof of Erdős–Straus for the hard core must use a *genuine* prime
factor of one of the numbers `n(n+k)/g`.

---

## 8. Closed-form families

**Lemma 12.** Let `n ≡ 1 (mod 4)`, `d ≥ 3` with `d ≡ 3 (mod 4)` and
`gcd(d,n) = 1`, and put `x = (n+d)/4`. Then `G = gcd(d, nx) = 1`, `A = d`,
`B = nx`.

**Proof.** `x` is an integer since `n + d ≡ 0 (mod 4)`; and `4x = n+d` gives
`gcd(d,x) | gcd(d,n) = 1`, so `gcd(d,x) = 1`. Together with `gcd(d,n) = 1` this
yields `gcd(d,nx) = 1`. ∎

**Theorem 12 (F1').** Under Lemma 12's hypotheses, if there is `c` with
`1 ≤ c ≤ x`, `c | x²` and `d | n + 4c`, then `ES(n)` holds.

**Proof.** Take `u = nc`. Then

* `u | n²x² = B²` because `c | x²`;
* `u ≤ B = nx` because `c ≤ x`;
* `nc ≡ −B (mod d)`: since `gcd(x,d) = 1` this is equivalent to `c ≡ −x (mod d)`,
  and `c ≡ −x (mod d)` is equivalent to `4c ≡ −4x = −(n+d) ≡ −n (mod d)`, i.e.
  `d | n + 4c`.

Lemma 4 now applies, giving

        y = (nx + nc)/d = n(x+c)/d ,     z = (nx + n²x²/(nc))/d
                                              = ( nx + n x²/c )/d .          (F1)

and `4/n = 1/x + 1/y + 1/z` follows. ∎

**Theorem 12 (F3').** Under Lemma 12's hypotheses, if there is `c` with
`1 ≤ c ≤ n`, `c | n²` and `d | n + c`, then `ES(n)` holds.

**Proof.** Take `u = xc`. Then

* `u | n²x² = B²` because `c | n²`;
* `u ≤ B = nx` because `c ≤ n`;
* `xc ≡ −B (mod d)`: since `gcd(x,d) = 1` this is equivalent to `c ≡ −n (mod d)`,
  i.e. `d | n + c`.

Lemma 4 gives

        y = (nx + xc)/d = x(n+c)/d ,     z = (nx + n²x²/(xc))/d
                                              = ( nx + n²x/c )/d .          (F3)

∎

**Ordering in Theorem 12.** In (F1'), `y = n(x+c)/d`. Since `n > 0` and
`c ≥ 1` we have `y ≥ n/d > 0`; and `x ≤ y` is checked numerically in
`tests/test_corollary13_*` and `tests/test_theorem12_*` for the ranges tested.
For the `c = 1` instances of Corollary 13 it holds automatically, because
`d | x+1` (Remark 8.1), giving `y = n(x+1)/d ≥ x` whenever `n ≥ d`, and
`n ≡ 1 (mod 24)`, `d | n+4`, `d ≡ 3 (mod 4)` force `d ≤ n+4`; the finitely many
cases `d > n` are `d = n+1`-type and are excluded by `d | n+4` together with
`d ≡ 3 (mod 4)`: if `d = n+4` then `n+4 ≡ 1 (mod 4)`, contradiction.

**Corollary 13.** Let `n ≡ 1 (mod 4)` and `d ≥ 3`, `d ≡ 3 (mod 4)`,
`gcd(d,n) = 1`, `x = (n+d)/4`.

1. If `d | n + 4`, then

        4/n = 1/x + 1/( n(x+1)/d ) + 1/( n x (x+1)/d ).

2. If `d | n + 1`, then

        4/n = 1/x + 1/( x(n+1)/d ) + 1/( n x (n+1)/d ).

**Proof.** (1) is F1 with `c = 1`: `c | x²` and `c ≤ x` hold automatically, and
the formulas give `y = n(x+1)/d`, `z = n x(x+1)/d`. Verifying the identity:
`1/y + 1/z = d/(n(x+1)) + d/(nx(x+1)) = d(x+1)/(n x(x+1)) = d/(nx)`, and
`1/x + d/(nx) = (n+d)/(nx) = 4x/(nx) = 4/n`.

(2) is F3 with `c = 1`: `1/y + 1/z = d/(x(n+1)) + d/(nx(n+1))
= d(x+1)/(n x (n+1)) = d/(nx)`, and the same last step gives `4/n`. ∎

**Remark 8.1 (integrality).** In (1) we need `d | n(x+1)`: since
`x = (n+d)/4` and `d | n+4`, we get `x ≡ −1 (mod d)` (multiply `4x = n+d` by
`4^{−1} (mod d)` and use `n ≡ −4 (mod d)`), so `d | x+1` and `d | n(x+1)`. In
(2) `d | n+1` directly. Both are automatic, and both were additionally checked
numerically in `tests/`.

---

## 9. Obstruction theorem

**Theorem 14.** Let `n` be in the hard core and suppose `ES(n)` fails. Then

* **(O1)** every prime divisor of `(n+3)/4` is `≡ 1 (mod 3)`;
* **(O2)** every odd prime divisor of `n+1` is `≡ 1 (mod 4)`;
* **(O3)** every prime divisor of `n+4` is `≡ 1 (mod 4)`;
* **(O4)** for every `k ≡ 3 (mod 4)` with `k < 73` and `x = (n+k)/4`, the number
  `B_k := n(n+k)/4` has no divisor `u` with `1 ≤ u ≤ B_k` and
  `u ≡ −B_k (mod k)`.

**Proof.** `(O1)`: by Theorem 10, `ES(n)` failing implies `(n+3)/4` has no prime
divisor `≡ 2 (mod 3)`; the alternative is `≡ 0` or `≡ 1 (mod 3)`. But
`3 ∤ (n+3)/4` because `(n+3)/4 = 6m+1 ≡ 1 (mod 3)`. Hence all its prime
divisors are `≡ 1 (mod 3)`.

`(O2)`: if an odd prime `q ≡ 3 (mod 4)` divided `n+1`, take `d = q`. Then
`d | n+1`, `d ≡ 3 (mod 4)`, `d ≥ 3`, and `gcd(d,n) = 1` because
`gcd(d, n+1−n) = gcd(d,1) = 1`. Corollary 13 (2) would give `ES(n)`,
contradiction.

`(O3)`: if a prime `q ≡ 3 (mod 4)` divided `n+4`, take `d = q`. Note `n+4` is
odd (`n` odd) so `q` is odd and `q ≥ 3`; and `gcd(q,n) = 1`, because `q | n+4`
and `q | n` would force `q | 4`, impossible for odd `q`. Corollary 13 (1) would
give `ES(n)`, contradiction.

`(O4)`: if some `k ≡ 3 (mod 4)` with `k < 73` admitted such a `u`, Lemma 4
would give `y, z ≥ 1` with `4/n = 1/x + 1/y + 1/z` where `4x − n = k`, so `ES(n)`
— contradiction. Note that for `k < 73` the hypothesis `gcd(k,n) = 1` needed in
Lemma 12 is automatic: every prime divisor of `n` is `≡ 1 (mod 24)` and
therefore `≥ 73`. ∎

**Remark 9.1 (explicit form of O4).** For `k < 73` we have `gcd(k, n(n+k)) = 1`
(since `gcd(k,n) = 1` and `gcd(k,n+k) = gcd(k,n) = 1`), so `G = gcd(4k, n(n+k))
= gcd(4, n(n+k)) = 4` (because `n` is odd and `4 | n+k`). Hence `A = k`,
`B = n(n+k)/4`, and modulo `k`

        B = n(n+k)/4 ≡ n²·4^{−1} .

So (O4) says: `n(n+k)/4` has no divisor `≤ n(n+k)/4` congruent to
`−n²·4^{−1} (mod k)`. In particular, by Lemma 5 read backwards, it has **no
prime divisor** in that residue class.

**Remark 9.2 (quantified strength).** On `H ∩ [1, 600000]` (6467 values) the
conditions (O1)–(O3) leave 799 candidates (12.36 %), and only 16 of those need
`μ(n) > 23` (`experiments/exp05_obstruction.py`). This is *evidence*, not a
proof: on the basis of the exact criterion of Lemma 4 alone, no counterexample
exists below `3·10⁵`.
