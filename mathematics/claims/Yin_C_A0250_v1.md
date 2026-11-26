---
author: Yin
---

# Dividing a projection trace by a prescribed integer and realizing all traceless matrix systems

## Statement

Write \(\mathcal R(G)\) for the actual star-regular closure of \(\mathbb CG\) inside its regular affiliated algebra.
It is closed under adjoints and affiliated Moore–Penrose inverses.
If the complex strong Atiyah conjecture fails, there is a single finitely generated torsion-free group \(J\) such that for every \(d\ge2\) the ring \(\mathcal R(J)\) contains a unital algebraic copy of \(M_d(\mathbb C)\).
This assertion permits an irrational initial rank.

Equivalently, fix any **one** integer \(d\ge2\).
The strong Atiyah conjecture across all torsion-free groups holds if and only if all finitely generated torsion-free groups exclude the [complete traceless system of size \(d\)](Yin_C_A0243_v2.md#statement) for a finite generating list.
Such a system consists of ordinary rank-one matrix units \(E_{ij}\) from bounded biorthogonal vectors \(x_i,y_i\) whose paired left translation spans give an orthogonal partition of \(\ell^2(J)\), and
\[
     \operatorname{span}_{\mathbb C}\{E_{ij}\}\ \cap\
     \left\{\sum_{g}[\rho_g,T_g]: T_g\text{ of finite ordinary rank}\right\}
       =\left\{\sum c_{ij} E_{ij}: \sum c_{ii}=0\right\}.
\]
In the counterexample direction all sizes occur on every fixed finite generating list of \(J\).
In particular regular ranks of two polynomial matrices in \(J\) differing by a single constant coordinate row have difference exactly \(1/d\) on the scalar trace and center-valued difference \((1/d)1\).
These are assertions about the star-regular closure and differences of polynomial ranks.
Obtaining an individual noninteger rational group-ring rank from an exclusively irrational obstruction remains open in this argument.

## Orthogonal copies up to a prescribed total trace

Regular subgroup inclusion preserves adjoints, spectral projections and Moore–Penrose inverses by decomposing convolution over right cosets.
It therefore preserves the star-regular expressions used here.
For a matrix over \(\mathcal R(G)\), image and kernel projections belong to the corresponding matrix ring, by matrix regularity; for a scalar \(b\) its image projection is \(bb^\dagger\).
All kernel projections used below for rectangular columns are also obtained from their scalar positive Gram entries.

Let \(p\in\mathcal R(G)\) be an orthogonal projection of trace \(a>0\).
For any positive integer \(k\) with \(ka\le1\), one can form \(k\) orthogonal projections of trace \(a\) in \(\mathcal R(G*\langle x\rangle)\), each algebraically equivalent there to \(p\).
Place \(p_i=x^ipx^{-i}\) at \(k\) distinct positions.
Their supporting conjugate group algebras are freely independent by free product normal form.
Given the sum \(Q\) of the earlier orthogonal projections, put \(b_i=(1-Q)p_i\) and \(q_i=b_i b_i^\dagger\).
The projection \(Q\) belongs to the algebra of the earlier positions.
The [free intersection formula](../audits/literature/CK14/Yin_U001.md#ck14-u001) gives \(Q\wedge p_i=0\) from \(\tau(Q)+a\le1\).
This includes equality; an empty sum gives \(Q=0\).
Thus \(b_i^\dagger b_i=p_i\), \(q_i\le1-Q\), and \(q_i\) is equivalent to \(p_i\), itself equivalent to \(p\).
The argument works with different original projection traces in the positions as long as their sum is at most one, giving orthogonal copies of the individual projections.

## A kernel on finite marked intervals

Suppose \(\mathcal R(B)\) contains \(d\) mutually orthogonal projections of the same trace \(a>0\), with \(d\ge2\) and \(da\le1\).
In \(\mathcal R(B\wr\mathbb Z)\) there is an orthogonal projection of trace exactly \(a/d\).
To see this, use the first two projections as \(A,B_1\) of trace \(a\), their next \(d-2\) as a sum \(C\) of trace \((d-2)a\), and their common remaining complement \(E\) of trace \(1-da\).
The four projections commute, sum to one, and their copies at different lamp sites have the product trace.
The shift \(t\) together with these projections has the Bernoulli line representation used in the [regular lamp calculation](Yin_C_A0017_v2.md#copies-in-the-regular-representation).
Choose the shift orientation so that \((t z)_i=z_{i-1}\) on the line.
Form the column with entries
\[
        L_1=(E+B_1+C)+(A-E)t,\qquad L_2=Ct.
\]
For a given sequence of site labels the two equations say the following at site \(i\).

| Label | Constraint |
| --- | --- |
| \(E\) | \(z_i=z_{i-1}\) |
| \(A\) | \(z_{i-1}=0\) |
| \(B_1\) | \(z_i=0\) |
| \(C\) | \(z_{i-1}=z_i=0\) |

A marked site has label different from \(E\), with probability \(da>0\).
Almost surely every interval between successive marked sites is finite and the associated sets of variables \([i,j-1]\) partition the whole line.
This follows because a ray of unmarked sites has probability zero and there are countably many possible endpoints.
Between marks at \(i<j\) the coordinates \(z_i,\ldots,z_{j-1}\) are constant.
They give one kernel dimension precisely when the left mark is \(A\) and the right mark is \(B_1\); otherwise the constant is zero.
This description also covers consecutive marks, a missing \(C\) when \(d=2\), and the case \(da=1\).

For length \(h=j-i\ge1\) the probability of such an interval starting at a specified site is \(a^2(1-da)^{h-1}\).
The normalized constant vector on each qualifying interval contributes one across its \(h\) possible positions in the trace at the origin.
By the orthogonal fiber decomposition, the trace of the entire kernel projection is
\[
                  \sum_{h\ge1} a^2(1-da)^{h-1}=\frac{a}{d}.
\]
The first term is \(a^2\) also for \(da=1\).
The column entries lie in \(\mathcal R(B\wr\mathbb Z)\); taking the kernel projection of \(L_1^*L_1+L_2^*L_2\) places this particular projection in that ring.

## A single group for all sizes

Failure of matrix integrality gives a finitely generated torsion-free group \(G\) and a nonzero singular scalar in the actual division closure, by the [division closure criterion and support reduction](../tasks/Yin_T_A0001_v1.md#starting-references).
Its kernel projection \(p\in\mathcal R(G)\) has trace \(0<\alpha<1\).
Take \(H_0=G\wr\mathbb Z\).
For a fixed \(d\) multiply \(m\) distinct lamp copies of \(p\), choosing \(m\) so that the resulting projection has trace \(a=\alpha^m\le1/d\).
This step uses independent commuting copies and works at every real \(0<\alpha<1\).

In \(H_1=H_0*\mathbb Z\), form \(k=\lfloor1/a\rfloor\) orthogonal copies by the first construction.
Their complementary projection has trace \(r=1-ka\), with \(0\le r<a\).
At least \(d\) members of the first family are available.
If \(r>0\), in \(H_2=H_1*\mathbb Z\) form \(d\) orthogonal copies of the remainder, since \(dr\le1\).
In \(H_3=H_2\wr\mathbb Z\) use the interval kernel on \(d\) copies of each positive size.
It gives projections of traces \(a/d\) and, when \(r>0\), \(r/d\).
These two projections need no independence from one another.

In \(H_4=H_3*\mathbb Z\) place \(k\) copies of the first result and one copy of the second when present in distinct free positions.
Orthogonalize them as above; the sum has trace
\[
                        k(a/d)+r/d=1/d .
\]
In \(J=H_4*\mathbb Z\) form \(d\) orthogonal projections algebraically equivalent to this last projection, summing to the identity by faithfulness of the trace.
For each equivalence choose \(v_i,w_i\) with \(w_i v_i=p_*\), \(v_iw_i=q_i\), where \(p_*\) is the common original trace-\(1/d\) projection and \(v_i=q_i v_i p_*\), \(w_i=p_*w_i q_i\).
Then \(v_iw_j\) form unital algebraic matrix units.
All groups in this finite sequence of wreath products and free cyclic extensions are finitely generated and torsion-free, and the sequence of groups is independent of \(d\).

The [traceless matrix characterization](Yin_C_A0243_v2.md#statement) gives the claimed finite-rank commutators and the [original-group coordinate increment](Yin_C_A0243_v2.md#a-rank-increment-on-every-central-summand) in \(J\).
Conversely, whenever the strong conjecture holds, the actual division closure for each group is a star-closed skew field in its affiliated algebra.
It is already star-regular, so the star-regular closure equals that skew field and contains no nontrivial matrix units.
Equivalently the original [rank-one exclusion](Yin_C_A0157_v1.md#separating-the-ranges-and-excluding-rank-one) already forbids each off-diagonal matrix unit in such a system.

## Assessment history

### Decision dividing-a-trace-on-finite-marked-intervals

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:32 |
| status | proved |
| reason | Independent review verified exact trace division, the single ambient group, the algebraic matrix units and the implication for every finite marking. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All dimensions of complete traceless systems from any failure in one group. |
| argument | [Orthogonal copies up to a prescribed total trace](#orthogonal-copies-up-to-a-prescribed-total-trace) | Free position, equality at total trace one and algebraic support equivalence. |
| argument | [A kernel on finite marked intervals](#a-kernel-on-finite-marked-intervals) | The four site constraints and exact regular trace of the kernel. |
| argument | [A single group for all sizes](#a-single-group-for-all-sizes) | The remainder, fixed sequence of groups, matrix units and global converse. |
| review | [Dividing a trace on finite marked intervals](../audits/reviews/Yin_R_A0201_v1.md#dividing-a-trace-on-finite-marked-intervals) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-dividing-a-trace-on-finite-marked-intervals)
