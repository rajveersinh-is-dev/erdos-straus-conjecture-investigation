/-
# The two-unit-fraction criterion (Lemma 3 of `mathematics/proofs.md`)

For `a, b > 0` with `gcd a b = 1`:

    a/b = 1/y + 1/z  for some `1 <= y <= z`
  <=> there is `u` dividing `b^2` with `1 <= u <= b` and `a | (b + u)`.

Every computational statement in the Python code of this repository is a
consequence of this equivalence, so verifying it removes the main
"trust the program" dependency from the project.

The statement is phrased over the integers so that subtraction is genuine
(no truncated subtraction in `N`). Since all variables are assumed positive it
is equivalent to the `N`-statement in the paper; positivity appears explicitly
in the hypotheses `0 < a`, `0 < b`, `0 < u` and in the conclusions
`0 < y`, `0 < z`.

Coprimality is entered through Bezout's identity,

    Bezout a b  :  exists s t : Z,  s * a + t * b = 1 ,

which for `a, b > 0` is equivalent to `gcd a b = 1`. This is exactly the
hypothesis of Lemma 3, and it is used in exactly one place: to cancel `b` from
`a | b * (b + v)`.
-/
import Mathlib.Data.Int.GCD
import Mathlib.Tactic

namespace ES

/-- Cleared-denominator form of `a/b = 1/y + 1/z`. -/
def TwoUF (a b y z : Int) : Prop := b * (y + z) = a * y * z

/-- The witness condition of Lemma 3. -/
def IsWitness (a b u : Int) : Prop :=
  0 < u /\ Dvd.dvd u (b ^ 2) /\ u <= b /\ Dvd.dvd a (b + u)

/-- Bezout form of `gcd a b = 1`. -/
def Bezout (a b : Int) : Prop :=
  Exists fun s : Int => Exists fun t : Int => s * a + t * b = 1

/-! ### The algebraic core -/

theorem factorisation {a b y z : Int} (h : TwoUF a b y z) :
    (a * y - b) * (a * z - b) = b ^ 2 := by
  calc
    (a * y - b) * (a * z - b) = a * (a * y * z - b * (y + z)) + b ^ 2 := by ring
    _ = b ^ 2 := by rw [h]; ring

/-- Cancellation of a coprime factor, via Bezout. -/
theorem dvd_of_dvd_mul_of_bezout {a b c : Int} (h : Dvd.dvd a (b * c))
    (hbz : Bezout a b) : Dvd.dvd a c := by
  obtain ⟨s, t, hst⟩ := hbz
  have h1 : Dvd.dvd a (s * a * c) := by
    refine ⟨s * c, ?_⟩
    ring
  have h2 : Dvd.dvd a (t * (b * c)) := by
    have hstep : t * (b * c) = (b * c) * t := by ring
    rw [hstep]
    exact h.mul_right t
  have hid : c = s * a * c + t * (b * c) := by
    calc
      c = (s * a + t * b) * c := by rw [hst]; ring
      _ = s * a * c + t * (b * c) := by ring
  rw [hid]
  exact h1.add h2

/-! ### Direction 1: a solution yields a witness -/

theorem solution_gives_witness {a b y z : Int} (ha : 0 < a) (hb : 0 < b)
    (h : TwoUF a b y z) (hyz : y <= z) (hy : b < a * y) (_hz : b < a * z) :
    IsWitness a b (a * y - b) := by
  refine ⟨by linarith, ?_, ?_, by simp⟩
  · have h1 : Dvd.dvd (a * y - b) ((a * y - b) * (a * z - b)) :=
      (Int.dvd_refl (a * y - b)).mul_right (a * z - b)
    rw [factorisation h] at h1
    exact h1
  · have hle : a * y <= a * z := mul_le_mul_of_nonneg_left hyz ha.le
    have hu0 : 0 <= a * y - b := by linarith
    have huz : a * y - b <= a * z - b := by linarith
    have h2 : (a * y - b) * (a * y - b) <= (a * y - b) * (a * z - b) :=
      mul_le_mul_of_nonneg_left huz hu0
    rw [factorisation h] at h2
    nlinarith

/-! ### Direction 2: a witness yields a solution -/

theorem witness_gives_solution {a b u : Int} (ha : 0 < a) (hb : 0 < b) (hu0 : 0 < u)
    (hbz : Bezout a b) (huv : Dvd.dvd u (b ^ 2)) (hu_le : u <= b)
    (hcong : Dvd.dvd a (b + u)) :
    Exists fun y : Int => Exists fun z : Int =>
      0 < y /\ 0 < z /\ y <= z /\ TwoUF a b y z := by
  obtain ⟨v, hv⟩ := huv                       -- hv : b ^ 2 = u * v
  have hv_pos : 0 < v := by
    by_contra hc
    have hv' : v ≤ 0 := le_of_not_gt hc
    have hmul0 : u * v ≤ u * 0 := mul_le_mul_of_nonneg_left hv' hu0.le
    have h1 : b ^ 2 ≤ 0 := hv ▸ (by rwa [mul_zero] at hmul0 : u * v ≤ 0)
    have hb2 : 0 < b ^ 2 := sq_pos_of_pos hb
    linarith
  have hmul : Dvd.dvd a (b * (b + v)) := by
    have h1 : Dvd.dvd a ((b + u) * v) := hcong.mul_right v
    rwa [show (b + u) * v = b * (b + v) from by nlinarith [hv]] at h1
  have hbv : Dvd.dvd a (b + v) := dvd_of_dvd_mul_of_bezout hmul hbz
  obtain ⟨y, hy⟩ := hcong                     -- hy : b + u = a * y
  obtain ⟨z, hz⟩ := hbv                       -- hz : b + v = a * z
  refine ⟨y, z, ?_, ?_, ?_, ?_⟩
  · by_contra hc
    have hy' : y <= 0 := le_of_not_gt hc
    have hneg : a * y <= 0 := mul_nonpos_of_nonneg_of_nonpos ha.le hy'
    have hpos : 0 < b + u := by linarith
    linarith
  · by_contra hc
    have hz' : z <= 0 := le_of_not_gt hc
    have hneg : a * z <= 0 := mul_nonpos_of_nonneg_of_nonpos ha.le hz'
    have hpos : 0 < b + v := by linarith
    linarith
  · have huv_le : u <= v := by
      by_contra hc
      have hlt : v * u < u * u := mul_lt_mul_of_pos_right (lt_of_not_ge hc) hu0
      have hsq : u ^ 2 <= b ^ 2 := by nlinarith [hu_le]
      nlinarith [hlt, hsq, hv]
    have hle : b + u <= b + v := by linarith
    rw [hy, hz] at hle
    have h1 : 0 <= z - y := by
      by_contra hc
      have h2 : z - y < 0 := by linarith
      have h3 : a * (z - y) < 0 := mul_neg_of_pos_of_neg ha h2
      linarith
    linarith
  · have key : a * y * z * a = b * (y + z) * a := by
      calc
        a * y * z * a = (a * y) * (a * z) := by ring
        _ = (b + u) * (b + v) := by rw [hy, hz]
        _ = b * (2 * b + u + v) := by nlinarith [hv]
        _ = b * ((b + u) + (b + v)) := by ring
        _ = b * (a * y + a * z) := by rw [hy, hz]
        _ = b * (y + z) * a := by ring
    exact (mul_right_cancel₀ ha.ne' key).symm

/-! ### The criterion, in full -/

theorem criterion_iff {a b : Int} (ha : 0 < a) (hb : 0 < b) (hbz : Bezout a b) :
    (Exists fun y : Int => Exists fun z : Int =>
        0 < y /\ 0 < z /\ y <= z /\ TwoUF a b y z)
      <-> Exists fun u : Int =>
        0 < u /\ Dvd.dvd u (b ^ 2) /\ u <= b /\ Dvd.dvd a (b + u) := by
  constructor
  · rintro ⟨y, z, hy0, hz0, hyz, h⟩
    have h' : b * (y + z) = a * y * z := h
    have hby : 0 < b * y := mul_pos hb hy0
    have hbz : 0 < b * z := mul_pos hb hz0
    by_cases hy : b < a * y
    · refine ⟨a * y - b, ?_⟩
      by_cases hz : b < a * z
      · exact solution_gives_witness ha hb h hyz hy hz
      · exfalso
        have h1 : a * z <= b := le_of_not_gt hz
        have h2 : a * z * y <= b * y := mul_le_mul_of_nonneg_right h1 hy0.le
        have h3 : a * y * z = a * z * y := by ring
        rw [← h3] at h2
        linarith
    · exfalso
      have h1 : a * y <= b := by linarith
      have h2 : a * y * z <= b * z := mul_le_mul_of_nonneg_right h1 hz0.le
      linarith
  · rintro ⟨u, hu0, hdiv, hule, hcong⟩
    exact witness_gives_solution ha hb hu0 hbz hdiv hule hcong

end ES
