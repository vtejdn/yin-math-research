---
author: Yin
---
# Mixed-word weighted-liberation kernels in the actual Haar/Poisson model

## Question and scope

This computation supports the adversarial development in [D_F0004](../../../drafts/Yin_D_F0004.md).
For the realized C_F0057 free U,V model, it computes finite Laurent kernels for unitary mixed words using exact polynomial-in-r free moments.
Angular scans are numerical diagnostics for a proposed universal lower bound normalized by the actual square-root-vacuum measure sigma_r squared times absolute(z-v) squared.
The reduction and source scope remain in D_F0004; no finite random matrix model replaces the realized tracial law.

## Files

- [main.py](main.py) computes exact coefficient polynomials by recursive centered-word expansion with freeness and the known Haar/Poisson moments.
- `../../outputs/Yin_J_F0009/results.json` is the historical output location for the exact coefficients, finite controls and numerical diagnostics; no payload is retained here.
- [D_F0004](../../../drafts/Yin_D_F0004.md) owns the actual-law reduction, independent hand computations and analytic bounds.
  The program is development evidence, not independent mathematical review.

## Reproduction

From the repository root, using the Python standard library:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0009/main.py
```

Output resolves to `mathematics/computations/outputs/Yin_J_F0009/results.json`, independently of the caller's directory.
It is atomically published after completing the selected checks and scans.
The program checks 20 exact coefficient identities for (U^a V)^n at a=-2,-1,0,1,2 and n=1,2,3,4, then records six named short mixed words.
Diagnostics use r=1/4,1/2,sqrt(3/4),0.95 and theta=pi*j/2048 for j=1,…,2048, with ordinary double precision and no random input.
Coefficients before the scan are integer polynomials in r; no interval error guarantee is claimed.
A fresh clone can lack output; reading the program does not execute it.

## Results and limits

All 20 known-formula comparisons passed and the six-word scan completed.
The largest observed normalized negative ratio was approximately 0.2343714237 for (U squared V) to the fourth power at r=1/4 and theta=pi.
No sampled ratio exceeded one; this establishes no uniform inequality.
The (UV)^3 ratio near 0.0009765616 agrees with the exact 1/1024 value proved in D_F0004 at r=sqrt(3/4), cos(theta)=-5/6.
That draft separately checks the ordinary commutator kernel by a six-term derivative/conditional-expectation calculation.
These controls test signs, phase and normalization, without supplying a full independent program review.

Exact arithmetic certifies only generated finite coefficient polynomials subject to the stated analytic recurrence.
Floating scans are diagnostics, not certified inequality or counterexample proofs.
All-degree bounds for two explicit word families are separately proved in D_F0004.
This scan establishes no result for arbitrary mixed words, analytic functional-calculus unitaries or nonbounded kernels, and creates no Claim or Task-completion assessment.

## Normal coordinate-change diagnostic

[normal_change.py](normal_change.py) tests the actual correlated normal family X=U+lambda U squared, Y=U*V from [D_F0006](../../../drafts/Yin_D_F0006.md#selfadjoint-tests-and-the-correlated-unitary-obstruction).
The reference U,V law is the same free Haar/Poisson law.
For real absolute(lambda) below one half, the divided-difference inverse has a projectively convergent Neumann series; the diagnostic retains its terms through degree N.
It computes the resulting actual finite-insertion adjoint T_N and vacuum xi_N, not an exact coordinate derivation for X at finite N.
Its six selfadjoint tests are w+w* for w=U^-2 V^2, UVU*V*, U*V^2, U^-2 V, U^2 V^2, and V.

The score function f=-w_r'/w_r gives h=1+i f and the actual normalized reference vacuum xi=h(V)U.
Integration by parts gives tau(h V^n)=(1-n)r^absolute(n) and tau(h* V^n)=(1+n)r^absolute(n).
For k=absolute(n) and s=r squared, the remaining moment is
\[
 \tau(f^2V^n)=r^k\left[-\frac{k(k-1)}2
       +\frac{(k+1)s}{1-s}+\frac{s+s^2}{(1-s)^2}\right].
\]
To obtain it, use tau(f squared V^n)=tau(f' V^n)-n squared r^k and sum the two geometric tails in f'=sum over positive j of j r^j(V^j+V^-j).
All other needed V moments contain at most two factors h or h* and follow by expansion.
The program uses exact Fraction arithmetic and centered alternating-word recursion; no finite-matrix approximation of the tracial law is used.
Its controls check tau(h*h), the vacuum pairing tau(h*V^-1)=0, and the exact unitary mixed-test defect -r squared from the [fixed hand proof](../../../ledger/Yin_L_F0055_v1.md#sharp-fixed-vacuum-and-degree-growth-failures).
The extended controls also compare the exact all-degree formulas at n=1,2,3,4,5, including the scalar-shifted strictly positive tests.

Run from the repository root with Python standard-library arithmetic:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0009/normal_change.py --N 8 --lam 3/10
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0009/normal_change.py --N 12 --lam 3/10
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0009/normal_change.py --N 8 --lam 3/10 --r 9/10
```

All three commands were executed successfully.
The exact rational matrix for twice Re<T_N(a squared),xi_N> minus norm(T_Na) in L2 squared was positive definite on the specified six-dimensional real test span in all three runs.
The original output files recorded its entries and positive LDL pivots:
`../../outputs/Yin_J_F0009/normal-change-r1-2-l3-10-N8.json`,
`../../outputs/Yin_J_F0009/normal-change-r1-2-l3-10-N12.json`, and `../../outputs/Yin_J_F0009/normal-change-r9-10-l3-10-N8.json`.
They are regenerable parameter-specific outputs, not a full-operator positivity certificate.
Printed ratios use floating conversion only for display; the matrix and LDL signs use exact arithmetic.
No least-eigenvalue margin was combined with the infinite-series tail, and no arbitrary-input or unrestricted-normal inequality is established.

The commands below were also run, with all 17 exact checks passing at each parameter:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0009/normal_change.py --controls-only
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0009/normal_change.py --controls-only --r 9/10
```

These controls support the retained hand calculation at their finite scope; the proof for all n is the [fixed geometric-sum argument](../../../ledger/Yin_L_F0055_v1.md#sharp-fixed-vacuum-and-degree-growth-failures).
