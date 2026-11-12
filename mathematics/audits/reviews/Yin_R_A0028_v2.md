---
author: Yin
---
# Independent review of the finite joint-word kernel bounds

Review performed at 2026-11-11T18:39 UTC for Yin.
The inspected fixed artifact is [C_A0009_v3](../../claims/Yin_C_A0009_v3.md), including its complete statement, argument, comparisons, source attribution and concluding limitations.
This is a new independent inspection in the existing R_A0028 topic family, not a reassessment inherited from its earlier physical version.

## Review arrangement and inputs

The reviewer was separate from substantive development of C_A0009_v3 and received the fixed artifact, review assignment, governing rules and operational metadata without development dialogue or a mathematical proof summary.
No development draft, author explanation or previous review finding was consulted.
The previous R_A0028_v1 was inspected only through its four-line author/title header to confirm the existing family; its argument, findings and verdict were not read or adopted.
The reviewer reconstructed the complete argument and formed the finding below directly from C_A0009_v3.

The necessary local comparisons were the [cyclic regular-representation argument](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), the [coefficient-angle statement](../../claims/Yin_C_A0009_v2.md#statement), the [ordered-quotient and normality screen](../../ledger/Yin_L_A0021_v1.md), and the relevant bounded tensor estimates in [L_A0027_v1](../../ledger/Yin_L_A0027_v1.md).
These materials were used at their stated comparison or elementary-input scope, not as prior reviews of the candidate.
The source inspection used the registered [Sim08 arXiv v1 original](../../literature/pdf/Sim08--arxiv-v1.pdf), with its title/version page and printed/PDF pp. 15 and 17 read directly; the two mathematical pages were also visually inspected.
No external theorem proof, computation program or existing review verdict is needed to supply the candidate's displayed tree recurrence, moment counts or polynomial minimization.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact statement](../../claims/Yin_C_A0009_v3.md#statement) | All stated translate conclusions, strict four-moment bound, collision correction and arbitrary-depth conditional bound, under their exact actual-group hypotheses. |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete argument](../../claims/Yin_C_A0009_v3.md#argument) | The entire argument from the bounded translate calculation through the concluding source and coverage discussion, including T1--T7 and M1--M15. |

## Whole-artifact finding

The complete argument supports the stated conclusions, with no unresolved mathematical gap found in this inspection.
The numerical improvement is conditional on actual canonical moments or the sufficient finite no-collision hypothesis for the fixed labels.
The translate results and the augmentation strictness argument have the unconditional scope stated in the candidate, but neither supplies the missing moment control for an arbitrary torsion-free group.

### Actual representation, trace and bounded domains

The operators are left regular group operators on \(\ell^2(G)\), with \(M:=\mathcal N(G)\) and its faithful normal probability trace \(\tau\).
The kernel projection of the bounded operator \(T:=1+u-v\) belongs to \(M\), commutes with \(X:=T^*T\), and is also the spectral projection of \(X\) at zero.
Its range and all group translates are closed right-\(G\)-invariant subspaces, so their dimensions are the relevant projection traces.
For a synthesis map from several copies of the kernel, the domain dimension uses the sum of the component traces, rather than a normalized matrix trace.
Every displayed compression, polynomial and kernel equation is bounded and acts on the whole relevant Hilbert space.
The proof never applies an unbounded inverse to a vector and never assumes that the unknown projection belongs to a rational closure or to the finite-support group algebra.

The cyclic input is applicable because a nonidentity element in the torsion-free group acts as a bilateral shift on each right coset of its infinite cyclic subgroup.
A nonzero one-variable Laurent polynomial therefore has zero kernel, since its finitely many circle zeros have Haar measure zero.
This checks the actual spectral law required in the proof; abstract infinite order of a unitary would not suffice.
The accepted foundational facts used here are bounded spectral calculus, faithfulness of the finite trace and polar decomposition for finite von Neumann modules, with no new audit of those general theories asserted.

### The translate configuration and all powers

Taking the adjoint-product of both sides of \(vp=(1+u)p\) gives \(p(u+u^*)p=-p\).
Thus the compression \(a:=pup\) has \(a+a^*=-p\), is a bounded normal operator in the corner, and satisfies \(pvp=p+a=-a^*\), as in T1.
For \(\eta\in K\) with \(u\eta\in K\), the equality \(a\eta=u\eta\) gives \(\|a\eta\|=\|\eta\|\).
Normality transfers this equality to \(a^*\eta=pu^*\eta\), so the equality case for an orthogonal projection implies \(u^*\eta\in K\).
Consequently \((1+u+u^*)\eta=0\), and the cyclic input forces \(\eta=0\).
Applying this to a vector represented as \(u\eta\) in \(K\cap uK\) proves T2.
Polar decomposition of the resulting injective two-column bounded map gives T3 for the closed sum without a closed-range or bounded-inverse assumption.

The analogous compressions of \(v\) and \(u^{-1}v\) are \(-a^*\) and \(-a\), respectively, and each has real part \(p/2\).
The corresponding cyclic equation is \((1-w-w^*)\eta=0\).
Both group elements are nonidentity because \(e,u,v\) are distinct, so the same argument proves the two assertions in T4.
The equation \(v\eta=\eta+u\eta\) then reduces the three-column synthesis equation to the already injective two-column equation.
This yields precisely the kernel \(\{(-\eta,-\eta,\eta):\eta\in K\}\) in T5.
The map \(\eta\mapsto(-\eta,-\eta,\eta)/\sqrt3\) identifies that kernel isometrically and equivariantly with \(K\), giving dimension \(\delta\) and closed range dimension \(3\delta-\delta=2\delta\).
The conclusion describes the dimension formula and does not assert a realization with \(\delta>0\).

For every integer \(k\), conjugation by \(u^k\) gives the stated kernel operator for \(u^kK\).
Subtracting its kernel equation from that of \(T\) yields T6.
When the conjugated labels differ, factoring out \(v\) leaves \(1-w\) with \(w:=v^{-1}u^kvu^{-k}\ne e\), to which the cyclic binomial certificate applies.
When they coincide, \(u^k\) commutes with \(T\), its adjoint and its kernel projection, hence \(u^kK=K\).
This verifies both alternatives in T7, including zero and negative powers, and their translated two-column consequences.
Neither calculation proves injectivity of an arbitrary row with at least three columns; T5 explicitly checks why pairwise transversality cannot justify that inference.

### Four moments, strictness and collision arithmetic

Distinctness of the three labels makes the identity coefficient of \(X\) equal to \(3\), so \(m_1=3\) even when other short words collide.
For the real polynomial in M3, direct squaring gives
\[
q(s)^2=1-\frac98s+\frac{113}{256}s^2
       -\frac{18}{256}s^3+\frac1{256}s^4.
\]
Since \(q(0)=1\), bounded functional calculus gives \(q(X)^2-p=q(X)^2(1-p)\ge0\), proving M4 and M5 with the displayed coefficients.
Substitution of \((3,15,87,543)\) gives
\[
\frac{256-864+1695-1566+543}{256}=\frac14.
\]

If equality held in M5, faithfulness would give \(q(X)^2=p\), and idempotence would give the group-algebra identity M6.
Faithfulness of the regular representation on \(\mathbb CG\) permits applying the ordinary algebraic augmentation to that finite-support identity.
The values \(\varepsilon(T)=\varepsilon(X)=1\) and \(q(1)=1/2\) would force \(1/16=1/4\), which is impossible.
This proves M7 and the strict conclusion in M2 without extending augmentation to the von Neumann algebra.
The projection enters the finite-support algebra only under the equality hypothesis, exactly as required by this reasoning.

The integer coefficients of \(X\) make all \(m_j\) integers.
Subtracting the free values from M5 yields precisely M8 and M9, without any positivity claim for the separate relation corrections.
The threshold checks are
\[
\frac14+\frac{21}{256}=\frac{85}{256}<\frac13,
\qquad
\frac14+\frac\Gamma{256}>\frac13
\Longrightarrow\ \Gamma>\frac{64}{3}.
\]
Thus integer \(\Gamma\le21\) gives the claimed strict improvement, \(\delta\ge1/4\) requires \(\Gamma>0\), and \(\delta=1/3\) requires \(\Gamma\ge22\).
These are necessary conditions on a hypothetical large kernel, with no converse existence assertion.

### Free-word moments and arbitrary finite depth

The bipartite block operator over \(F_2\) has three incident edges at each vertex.
Contracting its identity-labelled matching gives the ordinary four-regular Cayley tree of the free pair, so the original connected graph is a three-regular tree.
The signs can be removed along its unique paths, and the lower diagonal block of its square is \(X_0=T_0^*T_0\).
Therefore the identity coefficient of \(X_0^j\) counts the length-\(2j\) closed walks at a tree root.
For a Dyck path with \(j\) outward steps and \(r\) excursions, exactly \(r\) outward steps leave the root; this gives the factor \(3^r2^{j-r}\).
The excursion counts displayed in the candidate are the Catalan excursion decompositions for \(j=1,2,3,4\), and yield \(3,15,87,543\) with the displayed summands.
This finite combinatorial derivation is sufficient mathematical evidence; the candidate's additional report of a direct multiplication check was not needed or independently reproduced.

A monomial in \(X_0^j\) contains at most \(2j\) letters before reduction.
Under the indicated map from \(F_2\) to the subgroup generated by the fixed labels, the absence of nonempty identity words up to length eight therefore prevents every additional identity contribution for \(j\le4\).
The same length argument gives the sufficient bound \(4d\) for matching moments through \(2d\).
Signed extra contributions can cancel, so the candidate correctly uses no-collision as a sufficient condition and the actual moments as the weaker hypothesis.

The sphere sizes \(3\cdot2^{j-1}\) and normalized sphere indicators give exactly the adjacency coefficients \(\sqrt3\) and \(\sqrt2\) in M12.
The polynomial vectors form an orthonormal sequence because they equal those disjoint sphere indicators.
Parity and the recurrence at zero give M13, with the first nonconstant even value \(-3/\sqrt6=-\sqrt{3/2}\) and each later even value its negative.
In particular the first three polynomials for the squared adjacency measure are
\[
h_0(s)=1,\qquad
h_1(s)=\frac{s-3}{\sqrt6},\qquad
h_2(s)=\frac{s^2-7s+6}{\sqrt{24}}.
\]
They confirm directly that \(\kappa_d=1+3d/2\) and that M14 at \(d=2\) gives exactly M3.
Orthonormality proves M15, and the polynomial square has degree \(2d\), precisely the supplied moment range.
Transferring this finite polynomial identity to the actual trace and applying M4 proves \(\delta\le2/(3d+2)\).
The Cauchy--Schwarz argument also proves the claimed optimality for all complex polynomials of degree at most \(d\) with value one at zero, with equality attained by \(q_d\).
That optimality is correctly restricted to the indicated polynomial certificates, without claiming an optimal kernel bound among all uses of the moment data.

### Source attribution and scope of the conclusion

Sim08 is Barry Simon's *The Christoffel--Darboux Kernel*, arXiv:0806.1528v1, dated 9 June 2008.
Theorem 9.2 and equations (9.6)--(9.7) on printed/PDF p. 15 are exactly the stated finite-moment variational principle and its normalized diagonal-kernel minimizer.
The preceding Lemma 9.1 and the orthonormal expansion give the short proof, which was checked directly.
The tree adjacency measure and its squared pushforward are compactly supported probability measures, and the explicitly constructed orthonormal polynomials make the needed specialization valid at every finite degree.
Theorem 9.7 on printed/PDF p. 17 states the compact-support real-line atom limit used for the candidate's comparison.
Its statement and applicability were checked; this review does not certify its printed proof or the rest of the survey.
The candidate's independent recurrence and Cauchy--Schwarz proof supplies the finite estimate, so that comparison introduces no unresolved premise into M11.

The earlier coefficient-angle result gives \(1/3\) for these equal coefficient moduli, whereas the cited diagonal-tensor inequalities do not force vanishing in that interval.
The ordered-quotient and normality conditions in L_A0021 are additional sufficient hypotheses giving zero kernel; none is assumed or derived by the finite moment argument.
Those older results serve as coverage comparisons, not logical premises of M2 or M11, and their external source proofs were not re-audited here.
No claim is made that the finite no-collision condition escapes every known Atiyah class or that a concrete group outside those classes has been supplied.
For the same pair, absence of relations at arbitrarily large lengths does imply a free pair, whereas any fixed nontrivial relator bounds the available no-collision depth.
Changing generators or replacing labels by powers changes the operator and cannot transfer the original kernel without a further argument.
The review consequently supports the stated finite conditional improvement and exact collision obstruction, while leaving the unrestricted trinomial question, arbitrary multi-column synthesis injectivity and the all-matrix Task unresolved.
It supplies no historical-priority claim, formal verification or proof of that broader Task.
