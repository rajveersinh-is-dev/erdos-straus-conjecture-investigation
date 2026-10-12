/-
# The two-unit-fraction criterion (Lemma 3 of `mathematics/proofs.md`)

For `a, b > 0` with `gcd a b = 1`:

    a/b = 1/y + 1/z  for some `1 <= y <= z`
  <=> there is `u` dividing `b^2` with `1 <= u <= b` and `a | (b + u)`.

Every computational statement in the Python code of this repository is a
consequence of this equivalence, so verifying it removes the main
"trust the program" dependency from the project.

Direction 1 (solution ⇒ witness) is formalised in `ℤ` (where subtraction is
genuine) and then transferred to `ℕ`; direction 2 (witness ⇒ solution) is
formalised directly in `ℕ`.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic

namespace ES

open Nat

/-- Cleared-denominator form of `a/b = 1/y + 1/z`. -/
def IsTwoUnitFraction (a b y z : ℕ) : Prop :=
  b * (y + z) = a * y * z

/-- The witness condition of Lemma 3. -/
def IsWitness (a b u : ℕ) : Prop :=
  0 < u ∧ u ∣ b ^ 2 ∧ u ≤ b ∧ a ∣ b + u

/-! ## The algebraic core, over the integers -/

theorem factorisation_int
    (hab : Nat.gcd a b = 1) (h : IsTwoUnitFraction a b y z)
    (hy : b < a * y) (hz : b < a * z) :
    ((a : ℤ) * y - b) * ((a : ℤ) * z - b) = (b : ℤ) ^ 2 := by
  have key : ((a : ℤ) * y - b) * ((a : ℤ) * z - b)
      = (a : ℤ) * ((a : ℤ) * y * z - b * (y + z)) + (b : ℤ) ^ 2 := by ring
  rw [key, h]
  ring

theorem factorisation_nat (h : IsTwoUnitFraction a b y z)
    (hy : b < a * y) (hz : b < a * z) :
    (a * y - b) * (a * z - b) = b ^ 2 := by
  have hz_int : (b : ℤ) < (a : ℤ) * y := by exact_mod_cast hy
  have hz2_int : (b : ℤ) < (a : ℤ) * z := by exact_mod_cast hz
  have h_int : (b : ℤ) * (y + z) = (a : ℤ) * y * z := by exact_mod_cast h
  have := factorisation_int (a := a) (b := b) (y := y) (z := z)
    (Nat.gcd_a_of_dvd_of_dvd h.2 h.2) h_int hz_int hz2_int
  rw [Nat.cast_sub hz_int, Nat.cast_sub hz2_int, Nat.cast_pow, Nat.cast_mul,
    Nat.cast_mul, Nat.cast_mul] at this
  exact_mod_cast this

/-! ## Direction 1: a solution produces a witness -/

theorem solution_gives_witness (h : IsTwoUnitFraction a b y z) (hyz : y ≤ z)
    (hy : b < a * y) (hz : b < a * z) :
    IsWitness a b (a * y - b) := by
  refine ⟨by omega, factorisation_nat h hy hz, ?_, ?_⟩
  · -- u <= b, because u * (a*z-b) = b^2 and u <= a*z-b
    have huz : a * y - b ≤ a * z - b := by omega
    have h2 : (a * y - b) * (a * y - b) ≤ (a * y - b) * (a * z - b) :=
      Nat.mul_le_mul_left _ huz
    rw [factorisation_nat h hy hz] at h2
    nlinarith
  · -- a | (b + (a*y - b)) because that is a*y
    have : b + (a * y - b) = a * y := by omega
    rw [this]
    exact ⟨y, rfl⟩

/-! ## Direction 2: a witness produces a solution -/

theorem witness_dvd_bv (huv : u * v = b ^ 2) (hu : a ∣ b + u) :
    a ∣ b + v := by
  have hmul : a ∣ b * (b + v) := by
    calc
      a ∣ v * (b + u) := Nat.dvd_mul_right hu
      _ = b * (b + v) := by rw [huv]; ring
  exact Nat.Coprime.dvd_of_dvd_mul_left (Nat.Coprime.symm (Nat.gcd_coprime a b).symm) hmul

theorem witness_gives_solution (hab : Nat.gcd a b = 1) (hu : u ≤ b)
    (hw : u ∣ b ^ 2) (huv : u ∣ b + u) :
    IsTwoUnitFraction a b ((b + u) / a) ((b + v) / a) := by
  obtain ⟨v, rfl⟩ := hw
  have huv' : u * (b ^ 2 / u) = b ^ 2 := Nat.mul_div_cancel' hw
  have hle : u ≤ b ^ 2 / u := by
    have : u ≤ b := hu
    have := Nat.div_le_iff_le_mul (by omega : 0 < u)
    have hb2 : u ≤ b * b := Nat.mul_le_mul_right u hu
    omega
  have hbv : a ∣ b + (b ^ 2 / u) := by
    refine witness_dvd_bv huv' huv |>.resolve_right (Nat.gcd_coprime a b) |>.symm ▸ rfl
  constructor
  · show b * ((b + u) / a + (b ^ 2 / u) / a) = a * ((b + u) / a) * ((b ^ 2 / u) / a)
    have e1 : a * ((b + u) / a) = b + u := Nat.mul_div_cancel' huv
    have e2 : a * ((b ^ 2 / u) / a) = b + (b ^ 2 / u) := Nat.mul_div_cancel' hbv
    rw [e1, e2]
    have hkey : (b + u) * (b + b ^ 2 / u)
        = b * ((b + u) / a + (b + b ^ 2 / u) / a) * a + b ^ 2 := by
      have h4 : (b + u) * (b ^ 2 / u) = b ^ 2 := huv'
      omega
    nlinarith [hkey]
  · omega

/-! ## The criterion, in full -/

theorem criterion_iff (hab : Nat.gcd a b = 1) :
    (∃ y z : ℕ, 1 ≤ y ∧ 1 ≤ z ∧ y ≤ z ∧ IsTwoUnitFraction a b y z)
      ↔ ∃ u : ℕ, 0 < u ∧ u ∣ b ^ 2 ∧ u ≤ b ∧ a ∣ b + u := by
  constructor
  · rintro ⟨y, z, _, hyz, h⟩
    refine ⟨a * y - b, ?_⟩
    by_cases hy : b < a * y
    · exact solution_gives_witness h hyz hy (by
        have : a * y * z = b * (y + z) := h.symm
        omega)
    · have : a * y ≤ b := by omega
      exfalso
      have : b * (y + z) = a * y * z := h
      have hz : a * z ≤ b := by
        by_contra hz
        push_neg at hz
        have : a * y * z > b * z := Nat.mul_lt_mul_right z hy
        omega
      omega
  · rintro ⟨u, hu0, hdiv, hule, hucongr⟩
    obtain ⟨v, hv⟩ := hdiv
    refine ⟨(b + u) / a, b ^ 2 / u, ?_⟩
    · have : a ∣ b + u := hucongr
      have : a ≤ b + u := Nat.le_of_dvd (by positivity) hucongr
      omega
    · have : 0 < b + (b ^ 2 / u) := by positivity
      have : a ∣ b + (b ^ 2 / u) := witness_dvd_bv hv hucongr
      exact this
    · have : a ∣ b + (b ^ 2 / u) := witness_dvd_bv hv hucongr
      have h1 : u ≤ b ^ 2 / u := by
        by_contra hc
        have : u > b ^ 2 / u := by omega
        have : u * (b ^ 2 / u) < u * u := Nat.mul_lt_mul_right u hc
        rw [hv] at this
        omega
      have e1 : a * ((b + u) / a) = b + u := Nat.mul_div_cancel' hucongr
      have e2 : a * ((b ^ 2 / u) / a) = b + (b ^ 2 / u) := Nat.mul_div_cancel' this
      omega
    · exact witness_gives_solution hab hule hv hucongr

end ES
