---
author: Yin
---
# Independent review of the Brown-measure obstruction for coarse Sylvester equations

## Whole-proof finding

At 2026-11-13T14:50 UTC a separate agent outside proof development checked the complete [statement](../../claims/Yin_C_F0220_v1.md#statement) and [argument](../../claims/Yin_C_F0220_v1.md#argument) of the candidate dated 2026-11-13T14:45.
The reviewer received the fixed candidate and the requested scope, without development dialogue, exploration notes, author explanations or earlier findings on this candidate.
The energy and corner inequalities and the stated cyclic-matrix exclusions follow with the given normalizations.

Sending the second tensor factor to its opposite preserves its Hilbert inner product by cyclicity and turns right multiplication by \(B\) into left multiplication by \(B^{\mathrm{op}}\).
Thus \(DK=1\) in the finite algebra of measurable affiliated operators.
The complementary range projection annihilates \(DK\), and equality of the traces of the initial and final projections in the polar decomposition gives full support on both sides.
The polar part \(u\) is then unitary, \(K=|D|^{-1}u^*\), and the negative logarithmic singular moment is finite since \(\log^-(s)\le s^{-2}\) for \(s>0\).

Passing to the opposite algebra exchanges the two squared moduli of \(B-\lambda\), whose spectral probabilities agree, including their zero masses.
Trace-preserving tensor amplification preserves the singular laws at all shifts and hence the Brown measure, also in each nonzero corner with its normalized trace.
For the projection \(P(A,E)\otimes1\), invariance and the two concentrated corner measures therefore identify the amplified Haagerup–Schultz projection by uniqueness.
The analogous projection on the second leg commutes with the first, so their meet is their product, whose trace is the product of their marginal masses.
I checked §2.4, Definition 4.1, Proposition 5.5, Definition 5.6 and Theorem 11.2 of Charlesworth, Dykema, Sukochev and Zanin in arXiv:1703.05695v3, pp. 8, 14, 21 and 49.
These statements identify the joint law by rectangle masses and permit its pushforward under \(f(z,w)=z-w\), which is entire on a neighborhood of the joint spectrum in the generated commutative Banach algebra. [Authors' edition](https://arxiv.org/pdf/1703.05695v3)

I checked Proposition 2.16 and Theorem 2.19 of Haagerup and Schultz in arXiv:math/0605251v1, pp. 17–19.
The former applies to bounded \(D\) with the verified finite negative logarithmic moment and in particular gives \(\nu_D(\{0\})=0\).
The latter applies with \(p=2\) to its possibly unbounded inverse in \(L^2\).
Together they bound the negative second Brown moment by \(\|K\|_2^2\), giving (1) under the product-law calculation.
The external inspection of both papers covers their theorem statements and applicability, with the original proofs outside its scope. [Authors' edition](https://arxiv.org/pdf/math/0605251v1)

If the two measures overlap, the minimum of their densities against their sum gives a nonzero dominated measure \(\gamma\).
The sum of squared masses in a disjoint planar grid is at least \(c r^2\gamma(\mathbb C)^2\) at each small scale \(r\).
Integrating this lower bound against \(2r^{-3}\,dr\) proves infinite self-energy, including when \(\gamma\) has atoms.
Domination contradicts (1), in particular when the two operators agree.
The map \(s\otimes t\mapsto [h\mapsto s\tau(th)]\) has rank-one vectors \(s,t^*\), so it extends onto the Hilbert--Schmidt space, sends \(1\otimes1\) to the vacuum projection and carries the two actions to the required compositions.

For a commuting graph-domain projection \(p\), the Leibniz terms involving approximants \(p_n\) use \(p_n\otimes1\) and \(1\otimes p_n\) alone, so Hilbert convergence suffices.
Closability on the commutators \([p_n,X]\) gives the asserted equation for \(\bar\delta p\).
Compression \(h\mapsto php\) commutes with both multiplications by \(X\) by \(pX=Xp\), without centrality.
The complementary mixed compressions are orthogonal, their unit right sides have opposite signs, and each inherits \(t(1-t)\) times its intrinsic squared norm.
Symmetry of the kernel \(|z-w|^{-2}\) therefore gives precisely \(2t(1-t)I\).
For a central projection in the generated \(C^*\)-algebra, the two spectral clusters of a sufficiently close selfadjoint core element give a smooth cutoff with that value.
Uniform \(C^1\) approximation on the containing interval controls the divided differences of the two commuting outer multipliers and yields the required graph convergence.
For actual ACSY, the Leibniz tests against two-sided core multiples of the vacuum put a dense algebraic tensor subspace into the adjoint domain and give closability.

In the cyclic matrix case \(YY^*=\operatorname{diag}(1,bb^*)\), so the gap at \(1\) gives the same cutoff approximation of \(e_{11}\).
Either stated hypothesis puts \(e_{11}\) in \(W^*(Y)\), and \(e_{11}Y=e_{12}\), \(e_{12}Y=e_{11}b\) and adjoints generate \(M_2(W^*(b))\).
Differentiating the approximants to \((2e_{11}-1)Y+Y(2e_{11}-1)=0\) gives the anticommutator equation on the full coarse space.
At fixed inner indices \(j=m=1\), left multiplication by \(Y\) sends the row pair \((x_1,x_2)\) to \((x_2,bx_1)\), and right multiplication by \(Y\) sends the column-index pair \((y_1,y_2)\) to \((y_2 b,y_1)\).
The \((1,1)\) and \((2,2)\) outer coefficients therefore give \(V+Ub=-2(1\otimes1)\) and \(bU+V=0\), with \(U,V\) in the intrinsic coarse space because coefficient extraction is bounded.
Their difference would solve the forbidden equal-operator equation with \(k=U/2\).
This applies for every indicated contraction and every permitted value of the derivation on \(Y^*\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0220_v1.md#statement) | Mixed energy estimate and singularity, identical-operator Hilbert--Schmidt obstruction, graph-domain corner estimate and cyclic matrix exclusions. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0220_v1.md#argument) | Affiliated inversion, tensor joint law and inverse moment, planar divergence, arbitrary commuting corners, graph approximation and both matrix coefficients. |
| [Whole-proof finding](#whole-proof-finding) | [Joint Brown-measure source interface](../../claims/Yin_C_F0220_v1.md#joint-brown-input) | Single-coordinate uniqueness in normalized corners, rectangle meet and measure extension, polynomial pushforward for the tensor pair. |
| [Whole-proof finding](#whole-proof-finding) | [Inverse Brown-measure source interface](../../claims/Yin_C_F0220_v1.md#inverse-brown-input) | Finite negative logarithmic singular moment, inverse pushforward and \(p=2\) bound for an affiliated inverse. |
| [Whole-proof finding](#whole-proof-finding) | [Planar energy argument](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Squared cell masses and layer integration for the finite common submeasure. |
| [Whole-proof finding](#whole-proof-finding) | [Closed derivation and spectral cutoff](../../claims/Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Adjoint-vacuum tests, central spectral separation and divided differences for selfadjoint core cutoffs. |
