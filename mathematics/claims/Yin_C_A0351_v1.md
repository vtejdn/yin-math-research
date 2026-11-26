---
author: Yin
---

# Preserving inverse layers under one transcendental coefficient

## Statement

Assume the [integral determinant property](Yin_C_A0347_v7.md#statement) for \(G\) and put \(k=\overline{\mathbb Q}\).
For a coefficient subfield \(K\subset\mathbb C\) let \(D_j(K)\) denote the \(j\)-th actual scalar inverse layer starting from \(KG\) in \(U(G)\).
Write \(P_j(K)\) for the assertion that every nonzero element of this layer is an affiliated unit.
For every finite \(j\) and every transcendental \(\xi\in\mathbb C\),
\[
                            P_j(k)\ \Longrightarrow\ P_j(k(\xi)).
\]
In particular the scalar hypothesis alone transfers to one rational function field at depth zero, without assuming matrix integrality on \(G\).

If \(G\) is torsion-free and strong Atiyah integrality holds over \(kG\), then it holds for every complex coefficient field of transcendence degree at most one over \(\mathbb Q\), including arbitrary algebraic extensions inside \(\mathbb C\) of a one-variable rational function field.
The trace on finite matrix coordinates is unnormalized.
The argument does not assume rank independence for an arbitrary complex coefficient field.

## Full polynomial evaluations at a transcendental point

Suppose a square matrix polynomial \(F(t)\) over \(kG\) is an affiliated unit matrix at some algebraic \(t_0\).
Then \(F(\xi)\) is an affiliated unit at every transcendental \(\xi\).
For positive degree \(d\), \(x^d F(t_0+x^{-1})\) has leading coefficient \(F(t_0)\).
Multiplication on the left by its inverse makes this matrix polynomial monic, with coefficients that are actual algebraic rational evaluations over \(G\).
Use the block companion on \(d\) copies of the input: the first \(d-1\) equations identify the components of a kernel vector at parameter \(x\) as \(v,xv,\ldots,x^{d-1}v\), and the last gives the monic polynomial equation.
This elimination takes place in affiliated modules and preserves nonzero kernel.
An eigenvalue of the constant companion must be algebraic by the [unbounded rational atom theorem](Yin_C_A0347_v7.md#statement).
Thus \(x=(\xi-t_0)^{-1}\) cannot give a nonzero kernel.
A square matrix of full regular rank is an affiliated unit.
The degree-zero case is immediate.

## Keeping all gates defined in an algebraic specialization

Assume \(P_j(k)\) and take any nonzero evaluation \(s\in D_j(k(\xi))\).
Represent it by a finite scalar expression in the marks with coefficients rational in \(t\), evaluated at \(t=\xi\), of scalar inverse depth at most \(j\).
Include the condition that all original scalar denominators stay nonzero.
For each actual inverse gate take the full bounded linearization of its operand as a test matrix, formed by adjoining that operand's output row and input column to its square auxiliary system.
Once all earlier gates in the operand are valid, the rank of this test is its auxiliary size plus the rank of the scalar operand by affiliated Schur elimination.
The auxiliary system is then invertible. Use the same full linearization for the final output.
Their entries are rational in \(t\) with coefficients in \(kG\); common ordinary scalar polynomial denominators may be cleared, preserving all these ranks on a neighborhood of \(\xi\).
All inverse-gate tests have full rank at \(\xi\).
The final test has rank strictly greater than its auxiliary size because \(s\ne0\).

Regular rank is lower semicontinuous under operator-norm continuous variation of bounded matrices.
Indeed their positive Gram spectral distributions converge weakly on a common compact interval, and the mass at zero is upper semicontinuous.
On some neighborhood of \(\xi\), every gate test therefore has rank strictly greater than its size minus one, and the final test still has rank strictly greater than its auxiliary size.
Choose an algebraic \(t_0\) in that neighborhood.
In dependency order, the inverses in the expression exist at \(t_0\): if the preceding gates are valid, the current test implies its operand is nonzero.
It lies in an algebraic layer of depth at most \(j\), hence is an affiliated unit by \(P_j(k)\).
The same argument at the final output makes it nonzero and therefore an affiliated unit at \(t_0\).
Consequently its full polynomial test matrix has full regular rank there.
The preceding section now gives full rank of this matrix at \(\xi\), and Schur elimination in the original valid expression makes \(s\) a unit.
This argument uses only openness of the displayed strict rank inequalities; a general set of full regular rank need not be open.

## Finite algebraic extensions of one rational variable

Under the strong algebraic-coefficient hypothesis the actual division closure \(D=D_\infty(k)\) is a skew field by the torsion-free division-closure criterion.
The central polynomial ring \(D[t]\) is left and right Euclidean by ordinary degree division and has its classical skew field of fractions \(D(t)\).
Every nonzero polynomial in \(D[t]\) remains an affiliated unit at \(t=\xi\): divide on the left by its leading coefficient and use its monic companion as above.
Here the coefficients in \(D\) are finite actual rational evaluations, so the no-transcendental-eigenvalue result applies.
Evaluation gives a unital embedding of \(D(t)\) into \(U(G)\) extending \(k(t)\to k(\xi)\).

Identify \(k(t)\) with this scalar field and let \(L/k(t)\) be a finite field extension inside \(\mathbb C\).
The central scalar extension \(D(t)\otimes_{k(t)}L\) is a division ring.
First \(D\otimes_k L\) is a domain.
For two nonzero tensors express each as a sum of \(k\)-linearly independent elements of \(D\) with coefficients in \(L\).
The finitely generated \(k\)-subalgebra generated by both coefficient lists remains nonzero after inverting the product of one nonzero coefficient from each list.
It has a \(k\)-valued point by the weak Nullstellensatz.
Evaluating a proposed zero product at that point would give a zero product of two nonzero elements of \(D\), a contradiction.
Next \(D\otimes_k L\) embeds in \(D(t)\otimes_{k(t)}L\): localize \(D[t]\) first at nonzero central \(k[t]\), include it in \(D(t)\), then extend over the field \(k(t)\) to \(L\).
For nonzero \(x,y\) in the latter tensor algebra, multiply \(x\) on the left by a common nonzero denominator in \(D[t]\) and \(y\) on the right by another.
The resulting two elements are nonzero and belong to the embedded \(D\otimes_k L\).
Their product cannot vanish.
The tensor algebra is thus a domain of finite dimension over \(D(t)\) on both sides, so left multiplication by any nonzero element is surjective on its right vector space, giving an inverse.

The two evaluation maps into \(U(G)\) commute on the central scalar factor and give a unital homomorphism from this division ring, necessarily injective.
It contains the actual image of \(LG\), so matrix elimination gives integer regular ranks there.
For any proposed matrix over a field of transcendence degree one, adjoin \(k\) and a transcendence basis element, then take the finite field extension containing its finitely many coefficients.
Transcendence degree zero is already covered by the algebraic hypothesis.

## Assessment history

### Decision one-transcendental-coefficient-at-a-fixed-inverse-depth

| Field | Value |
| --- | --- |
| date | 2026-11-26T19:16 |
| status | proved |
| reason | A full algebraic specialization and a companion with no transcendental eigenvalue preserve scalar injectivity at each depth. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A full algebraic specialization and a companion with no transcendental eigenvalue preserve scalar injectivity at each depth. |
| argument | [Full polynomial evaluations at a transcendental point](#full-polynomial-evaluations-at-a-transcendental-point) | Full polynomial evaluations at a transcendental point. |
| argument | [Keeping all gates defined in an algebraic specialization](#keeping-all-gates-defined-in-an-algebraic-specialization) | Keeping all gates defined in an algebraic specialization. |
| argument | [Finite algebraic extensions of one rational variable](#finite-algebraic-extensions-of-one-rational-variable) | Finite algebraic extensions of one rational variable. |
| review | [One transcendental coefficient at a fixed inverse depth](../audits/reviews/Yin_R_A0242_v1.md#one-transcendental-coefficient-at-a-fixed-inverse-depth) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-one-transcendental-coefficient-at-a-fixed-inverse-depth)
