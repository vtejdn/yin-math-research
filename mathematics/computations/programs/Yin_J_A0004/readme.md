---
author: Yin
---
# All subrectangles of the Mian–Siddique witness

The [verifier](verify.py) uses only Python 3.10 or later and its standard library.
From this directory run the following command with assertions enabled.

~~~text
python -B verify.py
~~~

It checks the exact row and column sets against the three retained certificates and prints their sizes, the bucket counts and the outcome of the cancellation tests.
It writes no files and needs no downloaded input.
The lists in the program are the 32 and 28 words in the order of [Mian and Siddique, arXiv v1, Appendix A, p. 10](../../../literature/pdf/MS26b--arxiv-v1.pdf#page=10).
Lowercase letters denote generators, uppercase letters their inverses and the initial word on each side is the identity.
The two relators and finite images come from Sections 2.2 and 3.2, pp. 3–4 of the same edition.
The chain quotient, support enumeration and three-pair certificates are the present calculation.
The program builds the required necessary product equalities from the group presentation and checks the two input maps on the relators.
It does not rely on the authors' ball enumeration or require a Lean environment.
The [proof and source scope](../../../claims/Yin_C_A0105_v1.md#statement) give the implication for every field.
