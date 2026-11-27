# Manuscript revision opinions

These opinions concern the paragraph beginning “Proposition … computes these ranks” immediately after Theorem 1.9 in [the introduction](sections/introduction.tex).

## Required writing corrections

- **Identify the Hankel matrix.**
  The phrase “the associated Laurent series” leaves the series used for the Hankel rank implicit.
  Give the series \(r(\lambda+z^{-1})-r(\lambda)\), with \(\lambda\) chosen so that the matrix \(A(\lambda)\) of the minimal linear representation is invertible.
  State Kronecker's criterion for Laurent series vanishing at infinity and use the locator given in the one-variable comparison in [Section 5](sections/dual-system-criterion.tex).

- **Specify the roles of Theorem 1.9 and Proposition 5.8.**
  The final sentence's broad reference to “the ranks of Hankel matrices” leaves the correspondence between the two rationality criteria and the rank formula implicit.
  Attribute the finite-rank characterization of rationality to Theorem 1.9 and the computation of the fraction-commutator ranks on rational evaluations to Proposition 5.8.
  Use the equality with Hankel rank in one variable to close the comparison.

## Optional improvement

- **Display the rank identity.**
  Name the fraction-commutator closure and give the three equal ranks in a formula.
  Introduce \(A_i\) through \(A=A_0+\sum_j A_jx_j\) in a minimal linear representation of \(r\), retaining the assumption \(r\ne 0\).
