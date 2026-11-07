/-
SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
SPDX-FileCopyrightText: 2026 Chethan Dandebala Venkatarama
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Interpolation between measurements

`heart_rate_at` in `src/lib.rs` finds the weeks `w₀ < w₁` of the two weekly medians that
bracket the requested week `x` (each median is placed at the middle of its week) and
evaluates `lerp` below on the medians `b₀` and `b₁`. The theorems say that this formula
reproduces each measurement at its own week and never leaves the range of the two
measurements in between.

They are about exact real numbers. The Rust code evaluates the same formula in floating point
and then clamps the result to the range of `b₀` and `b₁`, which by `lerp_between` changes
nothing in exact arithmetic; the golden vectors check its rounding against an exact rational
oracle.
-/

namespace BiologicalRhythmsDataset

/-- Linear interpolation through `(w₀, b₀)` and `(w₁, b₁)`, evaluated at `x`. -/
noncomputable def lerp (w₀ b₀ w₁ b₁ x : ℝ) : ℝ :=
  b₀ + (x - w₀) * (b₁ - b₀) / (w₁ - w₀)

/-- At each measured point, interpolation returns the measurement itself. -/
theorem lerp_at_ends {w₀ w₁ : ℝ} (b₀ b₁ : ℝ) (h : w₀ ≠ w₁) :
    lerp w₀ b₀ w₁ b₁ w₀ = b₀ ∧ lerp w₀ b₀ w₁ b₁ w₁ = b₁ := by
  have hw : w₁ - w₀ ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
  constructor
  · simp [lerp]
  · unfold lerp
    rw [mul_div_right_comm, div_self hw, one_mul]
    ring

/-- Between two measurements, interpolation stays within the range of the measured values. -/
theorem lerp_between {w₀ w₁ x : ℝ} (b₀ b₁ : ℝ) (hw : w₀ < w₁) (h₀ : w₀ ≤ x) (h₁ : x ≤ w₁) :
    min b₀ b₁ ≤ lerp w₀ b₀ w₁ b₁ x ∧ lerp w₀ b₀ w₁ b₁ x ≤ max b₀ b₁ := by
  have hd : 0 < w₁ - w₀ := sub_pos.mpr hw
  -- The fraction of the way from w₀ to w₁.
  have t0 : 0 ≤ (x - w₀) / (w₁ - w₀) := div_nonneg (sub_nonneg.mpr h₀) hd.le
  have t1 : (x - w₀) / (w₁ - w₀) ≤ 1 := (div_le_one hd).mpr (by linarith)
  have hl : lerp w₀ b₀ w₁ b₁ x = b₀ + (x - w₀) / (w₁ - w₀) * (b₁ - b₀) := by
    unfold lerp
    ring
  rw [hl]
  rcases le_total b₀ b₁ with hb | hb
  · have up := mul_nonneg t0 (sub_nonneg.mpr hb)
    have down := mul_nonneg (sub_nonneg.mpr t1) (sub_nonneg.mpr hb)
    rw [min_eq_left hb, max_eq_right hb]
    constructor <;> nlinarith
  · have up := mul_nonneg t0 (sub_nonneg.mpr hb)
    have down := mul_nonneg (sub_nonneg.mpr t1) (sub_nonneg.mpr hb)
    rw [min_eq_right hb, max_eq_left hb]
    constructor <;> nlinarith

end BiologicalRhythmsDataset
