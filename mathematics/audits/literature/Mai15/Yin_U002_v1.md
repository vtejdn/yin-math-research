---
author: Yin
---

# Mai15: Real coassociative derivations and the norm estimates

## Mai15-U002

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Tobias Mai, *Regularity of distributions of Wigner integrals*, [retained arXiv:1512.07593v2](../../../literature/pdf/Mai15--arxiv-v2.pdf), 44 pages; artifact account (private lookup: `../../../literature/registry.md#mai15-source-artifact`). |
| source-locator | Definition 4.8, Theorem 4.9, Lemmas 4.10 and 4.11, Corollaries 4.12 and 4.13, and the regular-conjugate-variable observation, printed/PDF pp.26-31. Supporting adjoint identities are in [Mai15-U001 v2](Yin_U001_v2.md#mai15-u001). |
| inspection | 2026-10-16, AI source reader for Yin: every proof in this scope was read in full, its algebraic and Hilbert space steps checked, and all six original PDF pages visually inspected. The assessment is audited within the corrected scope described below, with standard Hilbert space and tracial inequalities retained as external inputs. This is source reading and self-review, not an independently commissioned project proof review or formal verification. |

### Exact hypotheses and conclusions

Let $(M,\tau)$ be finite tracial with faithful normal tracial state, let $H=L^2(M,\tau)$, and let $\mathcal A\subset M$ be a weakly dense unital $*$-subalgebra.
The outer derivation $\delta:\mathcal A\to H\bar\otimes H$ must satisfy all three conditions
\[
 \delta(a^*)=\delta(a)^\dagger,\qquad
 \delta(\mathcal A)\subseteq\mathcal A\odot\mathcal A,\qquad
 (\delta\otimes\mathrm{id})\delta=(\mathrm{id}\otimes\delta)\delta.
\]
Here $(a\otimes b)^\dagger=b^*\otimes a^*$, and $\odot$ denotes algebraic tensor product.
The second condition is part of the source's Definition 4.8, not a consequence of taking values in the completed Hilbert space tensor product.
Assume in addition that $1\otimes1$ belongs to the actual Hilbert space adjoint domain and put $\xi=\delta^*(1\otimes1)\in H$.
Reality gives $\xi=\xi^*$ in $L^2$; it does not make $\xi$ bounded.

Theorem 4.9 gives, for every $x\in\mathcal A$, including non-selfadjoint $x$,
\[
 \|\delta^*(x\otimes1)\|_2,\ \|\delta^*(1\otimes x)\|_2
 \leq\|\xi\|_2\|x\|,
 \qquad
 \|(\mathrm{id}\otimes\tau)\delta(x)\|_2,
 \|(\tau\otimes\mathrm{id})\delta(x)\|_2
 \leq2\|\xi\|_2\|x\|.
\tag{1}
\]
Under these same hypotheses, Corollary 4.12 gives
\[
 \|\delta^*(x_1\otimes x_2)\|_2
 \leq3\|\xi\|_2\|x_1\|\|x_2\|,
\tag{2}
\]
and bounds each of $(\mathrm{id}\otimes\tau)(\delta(x_1)\cdot x_2)$ and $(\tau\otimes\mathrm{id})(x_1\cdot\delta(x_2))$ by $4\|\xi\|_2\|x_1\|\|x_2\|$ in $L^2$.
The displayed statement of Corollary 4.12 omits the vacuum-adjoint hypothesis even though its formulas use $\xi$ and its proof invokes Theorem 4.9.
This unit adopts the corollary with that hypothesis restored.

### Why coassociativity and reality enter the proof

Set $y=(\mathrm{id}\otimes\tau)\delta(x)$ and $T(x)=\delta^*(x\otimes1)=x\xi-y$.
Lemma 4.10 uses the algebraic range to ensure $y\in\mathcal A$, so that the second derivative is actually defined.
It then uses coassociativity to obtain
\[
 (\mathrm{id}\otimes\tau)\delta(y)
  =(\mathrm{id}\otimes\langle\,\cdot\,,\xi\rangle)\delta(x).
\tag{3}
\]
The pairing is linear in its first variable.
Equation (3) follows by applying $\mathrm{id}\otimes\tau\otimes\tau$ to the two iterated derivatives and using $(\tau\otimes\tau)\delta(a)=\langle a,\xi\rangle$ on $\mathcal A$.
No second derivative is defined by this calculation for an arbitrary completed-tensor-valued derivation.

The proof on pp.28-29 combines (3), the actual adjoint formula, and reality to obtain
\[
 \|T(x)\|_2^2=\langle T(x^*x),\xi\rangle.
\tag{4}
\]
In detail, reality first gives $y^*=(\tau\otimes\mathrm{id})\delta(x^*)$.
Integration by parts with $y\otimes1$ and (3) produces
\[
 \|y\|_2^2
 =2\operatorname{Re}\langle1\otimes\xi x^*,\delta(x^*)\rangle
   -\langle\delta(x^*x),1\otimes\xi\rangle.
\]
Expanding $\|x\xi-y\|_2^2$ cancels the cross terms and leaves
\[
 \|T(x)\|_2^2
 =\|x\xi\|_2^2-\langle\delta(x^*x),1\otimes\xi\rangle.
\]
The remaining pairing is real because the other terms are real.
Reality of $\delta$, selfadjointness of $x^*x$, and $\xi=\xi^*$ identify it with $\langle\delta(x^*x),\xi\otimes1\rangle$, proving (4).
The selfadjoint element in this argument is $x^*x$; the tested $x$ is arbitrary.
All products of $\xi$ used here have bounded coefficients, so $L^2$ membership suffices throughout.

### Power iteration and the constants

Cauchy-Schwarz in (4) gives
\[
 \|T(x)\|_2^2\leq\|\xi\|_2\|T(x^*x)\|_2.
\tag{5}
\]
Independently, the Leibniz rule yields
\[
 \|T(x^m)\|_2
 \leq\|x\|^m\|\xi\|_2
       +m\|x\|^{m-1}\|\delta(x)\|_2.
\tag{6}
\]
Thus $\limsup_m\|T(x^m)\|_2^{1/m}\leq\|x\|$.
This calculation only uses powers of $x$, so the reference to Remark 4.2 does not require $x=x^*$: the needed polynomial chain rule is the ordinary Leibniz expansion for a single word.

Lemma 4.11 iterates (5) along $z_n=(x^*x)^{2^n}$, obtaining
\[
 \|T(x^*x)\|_2
 \leq C^{1-2^{-n}}\|T((x^*x)^{2^n})\|_2^{2^{-n}},
 \qquad C=\|\xi\|_2.
\]
Taking the limit using (6), and then using (5) once more, gives $\|T(x)\|_2\leq C\|x\|$.
If $C=0$, equation (4) directly gives $T=0$, so the lemma's stated $C>0$ convention causes no gap.
The second one-sided adjoint bound follows from $\delta^*(u^\dagger)=\delta^*(u)^*$.
Subtracting $T(x)$ from $x\xi$ in the adjoint formula gives the factor $2$ in (1).
Writing
\[
 \delta^*(x_1\otimes x_2)
 =\delta^*(x_1\otimes1)x_2
  -x_1(\tau\otimes\mathrm{id})\delta(x_2)
\]
gives the factor $3$ in (2).
Applying the product rule to $\delta(x_1x_2)$ and using (1) twice gives the factor $4$.

### The regular-conjugate-variable observation

Corollary 4.13 restates (4).
The paragraph following it assumes the stronger actual conditions
\[
 \xi\in\operatorname{Dom}\overline\delta\cap M,
 \qquad \overline\delta(\xi)\in M\bar\otimes M.
\]
The bars in this passage are visible in the original PDF and must not be lost in text extraction.
Adjoint duality then changes (4) into $\langle x^*x\otimes1,\overline\delta(\xi)\rangle$ and gives
\[
 \|\delta^*(x\otimes1)\|_2
 \leq\|\overline\delta(\xi)\|^{1/2}\|x\|_2,
 \qquad
 \|(\mathrm{id}\otimes\tau)\delta(x)\|_2
 \leq\bigl(\|\xi\|+\|\overline\delta(\xi)\|^{1/2}\bigr)\|x\|_2.
\]
Here the norm of $\overline\delta(\xi)$ is the von Neumann algebra norm; the underlying Hilbert space pairing is controlled by the positive functional associated to $x^*x\otimes1$.
The analogous opposite-side estimates follow by reality.
These genuinely require additional regularity of $\xi$ and are not consequences of $\xi\in L^2$ alone.

### Source corrections and exact reuse boundary

Lemma 4.11 and its use at the start of the proof of Theorem 4.9 write $T:\mathcal A\to M$.
The available hypotheses only give $T:\mathcal A\to L^2(M,\tau)$, already at $T(1)=\xi$.
The proof of Lemma 4.11 uses only the stated $L^2$ inequalities, so replacing this codomain by $L^2(M,\tau)$ repairs the application without changing any constant or conclusion.
Its last use of the hypothesis on p.28 is labeled (ii), but the displayed inequality uses (i).
The malformed sentence in Lemma 4.10 saying only that $\mathcal A\odot\mathcal A$ holds is read as $\delta(\mathcal A)\subseteq\mathcal A\odot\mathcal A$, exactly as Definition 4.8 requires.
These corrections are local and the corrected proof above closes; they are not evidence against Theorem 4.9.

The proof inspected here is internally complete after these corrections and does not rely on an MSW estimate.
Its attribution to Dabrowski is historical source attribution, not an unchecked mathematical dependency of the displayed derivation.
For selfadjoint generators with ordinary free difference quotients, the word formulas verify reality, the algebraic range, and coassociativity; (1) therefore applies to arbitrary complex polynomials, with precisely the constants stated above.

For an arbitrary derivation satisfying only the actual vacuum-adjoint condition, neither (3) nor (4) has been established by this source.
Normality of a chosen generating tuple does not replace either required identity.
Forming real and imaginary parts of a derivation does not, by itself, provide its algebraic range or the mixed iterated-derivative identities needed for coassociativity.
The estimates are on $\mathcal A$ with the operator norm on the right; the theorem neither constructs a dual system nor states that $M\Omega$ lies in the domains of a dual operator and its adjoint.
Such a domain extension requires its own closed-graph argument with the actual operators and signs.
No extension to a nonzero coassociativity defect is asserted in this source unit.
