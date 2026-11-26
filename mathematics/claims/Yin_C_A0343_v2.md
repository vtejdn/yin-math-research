---
author: Yin
---

# Uniform gaps below half when the five index-four characters all have rank at most two

## Statement

Consider the [marked noncyclic order-twenty quotient](Yin_C_A0333_v1.md#statement) of torsion-free two-generated groups with scalar regular injectivity.
For a complex two-square rectangle of noninteger nullity write \(\delta\) for this nullity with unnormalized coordinate trace.
Use its four-square signed commutator \(R_N\) on the common index-four sign subgroup.
Assume all five characters coming from the marking give \(R_N\) numerical rank at most two.

For each fixed marked group there is \(\epsilon_H>0\), independent of the four coefficient matrices, such that \(\delta\le1/2-\epsilon_H\).
For sofic marked groups there is a single \(\epsilon>0\), independent of the group and of the coefficients.
No numerical value for this last constant is asserted.
For every fixed normalized prototype parameter \(d\) there is also a gap independent of all the groups in the statement, without assuming soficity.
For real admissible \(d\) an explicit coefficient-dependent word cutoff giving this last gap is described below.

## The determinant reduction above two fifths

It suffices to consider \(\delta>2/5\); the [order-twenty degree bound](Yin_C_A0311_v1.md#statement) gives \(\delta\le1/2\).
For the two genuine order-ten characters with mixed weights \((1,2),(2,-1)\), use the degree-three matrix deformations of the [two-end calculation](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case).
The ten roots contribute \(10\delta>4\) to a degree budget of six.
The two extreme coefficients cannot both be singular, since each would contribute at least one more.
Put a full endpoint first by reversal if necessary, obtaining the six-dimensional companion with group-ring entries.
The interpolation polynomial of the ten roots together with zero cannot annihilate this companion: if it did, the square-free interpolation projection at any of the ten roots would give a nonzero group-ring column in an eigenspace of dimension \(\delta<1\).
The nonzero remainder has rank at least one by scalar injectivity, so the total dimension at those eleven points is at most five.
Singularity of the other endpoint would require at least \(10\delta+1>5\), a contradiction.
The two weights therefore make all four corners invertible even under this relaxed nullity threshold.

The numerical commutator formula in the [character-rank calculation](Yin_C_A0336_v1.md#character-ranks-and-zero-orders-on-the-grid) does not use the value \(1/2\).
The bound of one zero matrix on the grid also applies: a second would triangularize the numerical coefficient span and force full regular rank.
Hence the [five-square enumeration](Yin_C_A0336_v1.md#the-coefficient-lines) forces the same twenty determinant lines under the present character-rank assumption.
Use the indicated orientation, sign and phase twist to obtain the normalized prototype.
Its three numerator coefficients are independent by the constant point test for a noninteger kernel.
The [Clifford pencil budget](Yin_C_A0342_v1.md#statement) gives at most one parameter in each fixed ordered marking with nullity greater than \(1/4\), and that parameter is real.
There are only two orientations and finitely many grid twists, and no such parameter actually attains \(1/2\) by the [scattering argument](Yin_C_A0343_v1.md#statement).
This proves the fixed-group gap.

## A word cutoff for each fixed real parameter

Fix a real admissible \(d\), one normalized sign, and one numerical representative of its transfer.
The Clifford calculation ensures that this representative has the same kernel dimension as every other with these data, for every one of the marked groups.
For nonreal \(d\) the bound \(1/4\) already applies.
For a group with \(0<\delta\le1/2\), the [two-step trace identities](Yin_C_A0343_v1.md#which-group-words-can-contribute-to-the-trace) hold unchanged.
Indeed indicability would force integer regular rank, and the existence of a normalized cyclic power also forces integer rank by the same denominator elimination, independently of the value of \(\delta\).

For \(2<d<5/2\) take the constant basis making \(U=g^{-1}M(h)\) unitary and put \(T=U^2\).
Then \(T\) has normalized regular trace zero by absence of two-step returns, and its atom at one has mass at least \(\delta\) by the two signed kernels.
For \(d<1/2\) take \(T=W^2\) in the centered [positive-sign scattering basis](Yin_C_A0343_v1.md#positive-sign-scattering).
For \(1/2<d<2\) or \(d>5/2\) take \(T=V\) in the centered [negative-sign construction](Yin_C_A0343_v1.md#negative-sign-scattering).
The centering uses only the numerical coefficients and Haar measure on one circle.
The same trace computations and graph identifications give a unitary \(T\) of normalized trace zero and mass at least \(\delta\) at one in both cases.

Let \(\mu\) be its spectral measure with the normalized two-coordinate trace and \(D=T^2-I\).
In the associated \(L^2\) norm,
\[
   \|D\|_2^2=\int_{\mathbb T}|z-1|^2|z+1|^2\,d\mu(z)
       \le4\left(\int_{\mathbb T}|z+1|^2\,d\mu(z)-4\mu(\{1\})\right)
       \le8(1-2\delta).
\]
At some marked character \(\chi\), the numerical matrix \(D(\chi)\) has a nonzero entry.
For the two scattering cases this is precisely the numerical character contradiction in their respective proofs, using both signs of \(x\) in the negative-sign case.
In the definite case \(U(\chi)^4=B(y)^2/x^4\) times the identity, which differs from one at some character by the nonzero remainder of \(p(y)^2-y^8 q(y)^2\) modulo \(y^{10}-1\).
Fix such an entry with absolute value \(\eta>0\).

Construct that entry as a fixed absolutely summable convolution on the free group on the two displayed letters, by inserting the Laurent series of the cyclic rational functions.
Let \(l\) be such that its total absolute coefficient mass outside the free word ball of radius \(l\) is at most \(\eta/2\), and let \(b_l\) be the size of that free ball.
The quotient map to \(H\) cannot increase the absolute mass outside the ball there.
Inside its ball, the sum of the absolute coefficients of the chosen matrix entry is at most \(\sqrt{2 b_l}\,\|D\|_2\) by Cauchy--Schwarz and the matrix trace normalization.
Since \(\chi\) is unitary one obtains
\[
                 \delta\le \tfrac12-\frac{\eta^2}{128 b_l}.
\]
For any fixed centered numerical representative the cutoff can be found from the exponentially summable Laurent tails of the finitely many rational functions in \(T\) and its square.
This proof gives a uniform bound across the actual marked groups at the fixed parameter.

## Finitely many sofic parameters above two fifths

For a sofic \(H\) the [coefficient embedding theorem](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf) (Corollary 1.7) preserves the rank of the group-ring Clifford pencil at every complex embedding.
If \(d\) is transcendental, embeddings fixing \(\overline{\mathbb Q}\) give arbitrarily many different parameters of the same nullity.
The finite-sum budget forces this nullity to be zero.
For an algebraic \(d\), all conjugates have the same nullity by the two prototype signs and the independent sign character.
Therefore \([\mathbb Q(d):\mathbb Q]\,\delta\le1/2\).
In particular \(d=a/b\) is rational in lowest terms whenever \(\delta>1/4\).

For \(\delta>2/5\) the [integral minor proof](Yin_C_A0340_v2.md#an-integral-minor-and-its-mahler-measure) applies to this rational input with only the multiplicity changed.
At \(d_0=2\) the size of its nonzero minor divided by the number of sites tends to eight, while the nullity per site at \(d\) tends to \(4\delta\) by the same algebraic-integer singular-value bound.
The multiplicity per site used in Gauss's lemma is thus at least \(4\delta-o(1)\) for each of the two conjugate minors.
The coefficient norm remains at most sixty, giving
\[
                         \max(|a|,b)\le60^{\,2/\delta}<60^5 .
\]
All parameters with \(\delta>2/5\) therefore lie in a single finite set independent of the group.
Take the minimum of the preceding fixed-parameter gaps for the admissible rationals in that set and the two normalized signs, together with \(1/10\) for the complementary nullity range.
This positive number supplies the uniform sofic gap in the statement.
