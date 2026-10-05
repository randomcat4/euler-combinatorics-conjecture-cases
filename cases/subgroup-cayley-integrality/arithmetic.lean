import Mathlib

/-!
Exact arithmetic core for the SubgroupIntegrality square-gap argument.

This file deliberately formalizes only the integer lemma.  It contains no claim
about the representation-theoretic construction of the spectral block.
-/

namespace SubgroupIntegrality

def N (d r k : ℤ) : ℤ := d * (k + 2) - 4 * r

def M (d r k : ℤ) : ℤ := d^2 * (k + 2)^2 - 8 * k * d * r

lemma M_eq_N_sq_add (d r k : ℤ) :
    M d r k = (N d r k)^2 + 16 * r * (d - r) := by
  simp only [M, N]
  ring

lemma not_square_of_between (a m : ℤ) (ha : 0 ≤ a)
    (hlow : a^2 < m) (hhigh : m < (a + 1)^2) :
    ¬ ∃ z : ℤ, z^2 = m := by
  rintro ⟨z, rfl⟩
  have hz : 0 ≤ |z| := abs_nonneg z
  have hzsq : |z|^2 = z^2 := by
    rw [sq_abs]
  have haz : a < |z| := by
    nlinarith [sq_nonneg (|z| - a)]
  have hstep : a + 1 ≤ |z| := by omega
  nlinarith [sq_nonneg (|z| - (a + 1))]

lemma nonsquare_of_positive_gap (d r k : ℤ)
    (hr : 0 < r) (hrd : r < d) (hN : 0 ≤ N d r k)
    (hgap : M d r k < (N d r k + 1)^2) :
    ¬ ∃ z : ℤ, z^2 = M d r k := by
  apply not_square_of_between (N d r k) (M d r k) hN
  · rw [M_eq_N_sq_add]
    have : 0 < r * (d - r) := mul_pos hr (sub_pos.mpr hrd)
    nlinarith
  · exact hgap

lemma exceptional_2_1_3 : ¬ ∃ z : ℤ, z^2 = M 2 1 3 := by
  have hm : M 2 1 3 = 52 := by norm_num [M]
  rw [hm]
  exact not_square_of_between 7 52 (by norm_num) (by norm_num) (by norm_num)

lemma exceptional_3_1_4 : ¬ ∃ z : ℤ, z^2 = M 3 1 4 := by
  have hm : M 3 1 4 = 228 := by norm_num [M]
  rw [hm]
  exact not_square_of_between 15 228 (by norm_num) (by norm_num) (by norm_num)

end SubgroupIntegrality
