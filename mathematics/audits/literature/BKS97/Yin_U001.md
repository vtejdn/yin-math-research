---
author: Yin
---

<a id="bks97-u001"></a>
# BKS97-U001: The Scalar q-Hermite Spectral Law

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected artifact: [arXiv:funct-an/9604010v1](https://arxiv.org/pdf/funct-an/9604010), dated 1996-04-30, 28 pages; the bibliography retains its 1997 journal identity. |
| source-locator | Locators: Definition 1.9 and Theorem 1.10(1), p. 7; Theorem 4.6(1), p. 20, with its explanation on p. 21. |
| inspection | Coverage: `Read`. |

- Record: 2026-09-09, the q-Gaussian mechanism agent; direct primary statement and applicability reading for [Yin_S_F0008](../../../strategies/Yin_S_F0008.md#s_f0008).
- Source identity: [BKS97 in the bibliography](../../../literature/readme.md).
  Inspected artifact: [arXiv:funct-an/9604010v1](https://arxiv.org/pdf/funct-an/9604010), dated 1996-04-30, 28 pages; the bibliography retains its 1997 journal identity.
  No local PDF retained; journal text not compared.
- Locators: Definition 1.9 and Theorem 1.10(1), p. 7; Theorem 4.6(1), p. 20, with its explanation on p. 21.
  These are both printed preprint and one-based PDF page numbers.
- Coverage: `Read`.
  The spectral-law and orthogonality statements are accepted under the [external-input rule](../../../../framework/rules/literature-audits.md#accepted-external-inputs); their original proofs have not been independently audited.

## Accepted Measure and Recurrence

For $-1<q<1$, put $a_q=2/\sqrt{1-q}$.
The variance-one q-Gaussian measure is supported on $[-a_q,a_q]$ and has density, with $x=a_q\cos\theta$,
\[
w_q(x)=\frac{\sqrt{1-q}}{\pi}\sin\theta
\prod_{k=1}^{\infty}(1-q^k)|1-q^ke^{2i\theta}|^2,
\qquad0\le\theta\le\pi.
\tag{1}
\]
The monic polynomials $H_m^{(q)}$ satisfy
\[
H_0^{(q)}=1,\quad H_1^{(q)}(x)=x,\qquad
xH_m^{(q)}=H_{m+1}^{(q)}+[m]_qH_{m-1}^{(q)},
\quad [m]_q=\frac{1-q^m}{1-q},
\tag{2}
\]
and $\int H_m^{(q)}H_n^{(q)}w_q\,dx=\delta_{mn}[m]_q!$.

Theorem 4.6(1) identifies the algebra of a scalar q-Gaussian with this spectral measure, scaled by the square root of its variance.
Hence a nonzero real linear combination $h=\sum_i v_iX_i$ of canonical q-Gaussians has this law scaled by $\|v\|$.
This scalar identification is the accepted interface; no transition-kernel or Markov-property assertion is needed.

## Applicability and Retained Proof Scope

[Yin_C_F0020 B](../../../claims/Yin_C_F0020_v1.md#yin_c_f0020) owns the further deductions from (1): uniform positive upper and lower bounds for the product at fixed q, comparison with a square-root endpoint density, exclusion of all reduced scalar L2 poles, and bounded scalar reconstruction.
Its bounded-dual construction additionally uses the previously accepted Hilbert-transform interface.
These are local arguments, not stronger statements attributed to BKS97.

Normalizing (2) by $\sqrt{[m]_q!}$ gives the degree-dependent orthonormal recurrence used for the scalar resolvent diagnostic in the same ledger note.
That diagnostic does not assert finite Hankel rank.

The source identifies the measure through q-Hermite orthogonality and the q-Fock spectral representation.
The original orthogonality-product proof and the foundational q-Fock construction are retained established inputs, not independently re-proved here.
The theorem statements, their normalizations and the one-variable specialization were directly checked.

## Limits and Verification Facts

The law here is the q-Gaussian law from q-commutation relations, not a similarly named distribution from Tsallis statistics.
The interval formula is restricted to $-1<q<1$; the endpoints $q=\pm1$ are excluded.
Statements about one real linear marginal do not determine the joint distribution's coefficient residual geometry or give a simultaneous bounded dual system at arbitrary q.

The source search was triggered by testing whether a marginal could retain Yin_C_F0016's integrable endpoint pole.
The exact arXiv version, product formula, recurrence and scaled spectral-law statement resolved that question.
Parsed source pages were inspected without retaining a PDF; no journal/preprint or systematic errata comparison was made.
No whole-paper proof audit, numerical experiment, formal verification or literature-priority assessment is claimed.

## Additional original definition reading

<a id="bks97-definition-recheck"></a>

This maintenance does not reopen the source or extend its original proof audit.

The coordinating agent reread the exact arXiv v1 dated 1996-04-30, its title and complete printed/PDF p. 7 on 2026-09-10, alongside the original U001.
Only Definition 1.9 and Theorem 1.10(1) normalization were checked; the accepted orthogonality, spectral-law and endpoint interfaces retain the original proof-inspection limits.
<a id="q-hermite"></a>
For -1<q<1, [n]_q!=(product from k=1 to n of [k]_q) has empty product one.
Thus the orthonormal family is H_n^(q)/sqrt([n]_q!), as used by C_F0020; the recurrence alone yields no finite-Hankel-rank assertion.
The source provides a current formulation/notation candidate, with no historical-priority investigation.
