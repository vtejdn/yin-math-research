---
author: Yin
---
# Independent review of the layer reductions and finite coefficient certificate

On 2026-11-21 at 04:29 UTC a separately assigned reviewer inspected the complete fixed C_A0095_v2 statement and proof for Yin.
The reviewer had independently reviewed v1 and received the v2 claim without its proof-development discussions, author explanations or prior v2 findings.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0095_v2.md#statement) | All four tests, the minimum-support exclusions, arbitrary complex coefficients, and the fixed-group quantifiers. |
| [Whole finding](#whole-finding) | [Leading component](../../claims/Yin_C_A0095_v2.md#unitary-powers-and-the-leading-component) | Unitary conjugation, equality of kernels, and the highest homogeneous component. |
| [Whole finding](#whole-finding) | [Next degree and gap](../../claims/Yin_C_A0095_v2.md#the-next-degree-and-the-gap-condition) | Both unequal gaps, the equal-gap collision, deletion of the top layer under strict separation, and the free-group example. |
| [Whole finding](#whole-finding) | [Reciprocal extrema](../../claims/Yin_C_A0095_v2.md#reciprocal-extrema) | All homogeneous components used to reduce a solution to its middle layer. |
| [Whole finding](#whole-finding) | [Coefficient certificate](../../claims/Yin_C_A0095_v2.md#constructing-and-using-the-character-free-certificate) | Word collection, rational row-space membership, specialization with genuine conjugation, full-support requirement, and single-monomial obstruction. |
| [Whole finding](#whole-finding) | [Finite-group example](../../claims/Yin_C_A0095_v2.md#a-finite-group-diagnostic-with-no-real-characters) | Exact commutator coefficients in \(S_3\), the nonnormal solution, and failure of the specified certificate. |
| [Whole finding](#whole-finding) | [Earlier equivalence](../../claims/Yin_C_A0095_v1.md#statement) | Applicability of the scalar equivalence for each fixed torsion-free group. |
| [Whole finding](#whole-finding) | [Earlier extreme layers](../../claims/Yin_C_A0095_v1.md#testing-the-extreme-layers-of-one-element) | Starting highest-degree relation and two-layer deletion recovered in v2. |
| [Whole finding](#whole-finding) | [Coefficient families](../../claims/Yin_C_A0033_v1.md#statement) | Scope of the comparison with projective components and Newton polygons. |

## Whole finding

C_A0095_v2 proves all four tests at their stated scope.
Writing \(T(X)=uXu^{-1}\), right multiplication by \(u\) commutes with \(T\), giving \(\partial_u^k(X)=(T-I)^k(X)u^k\).
The spectral measure of \(T\) on any vector killed by \((T-I)^k\) is supported on \(\{1\}\), so that vector is fixed by \(T\).
This applies to every finite group-ring vector and yields the required commutation whenever a surviving power of \(\partial_{cu}\) vanishes.

At the next degree each changed factor costs at least \(\min(a,b)>0\), so exactly one of the four factors changes.
The leading component has already given \(\partial_P(Q^*)=0\).
Of the three possible unstarred replacements this kills both orders with an innermost \(\partial_P\), leaving \(\partial_P^2([R,Q^*])\).
The starred replacement contributes \(\partial_P^3(T^*)\).
At equal gaps both survive as possible contributions to one coefficient sum, even if \(R=T\), so commutation follows for the combined expression in (1).
In the strict gap test every unstarred replacement has degree at most \(2h+m-l<3h-m\).
Thus \(3h-\alpha\) isolates the three top factors and the adjoint of the single lower part \(D_\alpha\), simultaneously for all lower degrees.
Commutation with each part and its adjoint preserves both \(H\) and \(E\) after removing the top label, including the case \(m=l\).
In the free-group diagnostic the central \(v\) cancels from the commutators.
The reduced words \(u^{3-j}w^{-1}u^j\) for \(0\le j\le3\) are distinct, so their signed binomial coefficients give a nonzero component even though both initial degree tests vanish.

For reciprocal extrema the extreme monomials give zero commutators with one another's adjoints, and their individual self-commutators also vanish.
The remaining components of \(H_D\) in degrees \(h,0,-h\) are \(X,H_R,X^*\), respectively, with \(X=\partial_u(cR^*-\bar d R)\).
The degree \(3h\) equation kills \(X\) by the unitary kernel identity.
The degree \(2h\) equation then makes \(H_R\) commute with \(u\) and \(u^{-1}\).
Both orders of the opposite extremal factors therefore disappear from the degree-zero equation, leaving \(E_R=0\).
Since \(H_R=H_D\), a nonnormal witness loses two support labels and stays in the same group.
This deduction works for arbitrary nonzero \(c,d\), including \(|c|=|d|\).

In the certificate the four possible positions of the starred label have signed coefficients \(1,-3,3,-1\).
Each term is collected using both its group product and its commutative coefficient monomial.
This gives finitely many integer rows once the actual word equalities for the support are known.
An identity (16) specializes to a genuine adjoint by \(w_j=\bar c_j\), and division by \(c_r c_s\) is valid on the specified full support, including \(r=s\).
The same specialization preserves nonvanishing of a single nonzero monomial row.
Exact row reduction decides membership in the stated rational span, and failure leaves the full coefficient problem open.

For the \(S_3\) example, put \(L=ab-ba\) and \(t=aba=bab\).
The relations give \([a,L]=2(b-t)\), \([b,L]=2(t-a)\), \([a,t]=-L\), and \([b,t]=L\).
Consequently \(\partial_D^2(L)=4(c^2+d^2-cd)L\), and \(H_D=(c\bar d-d\bar c)L\) verifies (17).
With \(c=e^{\pi i/3}\) and \(d=1\) the quadratic vanishes and \(H_D\ne0\).
The symbolic rows of \(E\) span a single quadratic multiple of \(z_1w_2-z_2w_1\), and that quadratic is proportional to none of \(z_1^2,z_1z_2,z_2^2\).
Thus the certificate correctly fails on this support in a finite group with trivial real characters.

The earlier fixed-group equivalence and its two-layer specialization retain the scope documented in the [v1 review](Yin_R_A0131_v1.md#whole-finding).
The present review checked the [C33 statement](../../claims/Yin_C_A0033_v1.md#statement) for the comparison with projective component and Newton polygon tests.
Those results supply no premise for (7).
The two peeling arguments exclude the indicated forms of a minimum-support nonnormal solution in the same torsion-free group.
The [A0002 contract](../../tasks/Yin_T_A0002_v1.md#contract) remains open for unrestricted finite supports.
