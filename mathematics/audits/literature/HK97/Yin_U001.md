---
author: Yin
---

# HK97: assembly surjectivity for countable amenable groups

<a id="hk97-u001"></a>
## Source and inspection

The inspected source is the [complete publisher TeX original](readme.md#publisher-source).
On 2026-11-12, Section 1 was read through Theorem 1.2 and Corollary 1.3, including the preceding definitions of the two assembly maps and the countable discrete group convention.
The source declares the labels through its theorem environments named `theorem1` and `theorem2`.
The proof outline in the remaining sections and its external inputs were not audited.

<a id="amenable-assembly"></a>
## Exact usable statement

For every countable amenable discrete group \(G\), the reduced Baum–Connes assembly map
\[
\mu_{\mathrm{red}}:K_*^G(\underline EG)\longrightarrow K_*(C_r^*(G))
\]
is an isomorphism; in particular its degree-zero map is surjective.
This is the countable amenable conclusion explicitly stated in Corollary 1.3, following the isomorphism statement of Theorem 1.2.
The source uses \(\mathcal EG\) for the universal proper space denoted \(\underline EG\) here.
For torsion-free \(G\), the source identifies it with the universal free space and identifies the assembly domain with the corresponding compactly supported \(K\)-homology of \(BG\).

The corollary follows in the source from the theorem for groups admitting metrically proper affine isometric actions on a possibly infinite-dimensional real inner-product space and the cited fact that countable amenable groups admit such actions.
That mechanism and the declared hypotheses were checked at statement level; the construction of the action and the proof of the assembly theorem are accepted published inputs, not independently verified here.
No statement for an arbitrary nonamenable group or an arbitrary affiliated rational closure is inferred.

The separately inspected [BCM04 assembly-trace interface](../BCM04/Yin_U001.md#assembly-trace) explains the scalar projection consequence for torsion-free countable amenable groups.
It supplies no finite-support kernel projection or group-ring domain theorem.
