"""Exact finite checks for Miy26-U007 and Miy26-U008; standard library only.

Direct truncated geometric-series multiplication is independent of the six-state
recurrence. Gaussian rational arithmetic avoids floating-point tolerances.
Current reproduction from the repository root:
  .venv/Scripts/python.exe mathematics/computations/programs/Yin_J_F0007/main.py
On POSIX use .venv/bin/python for the same command.
No third-party dependencies are required; this instruction records no new run.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import random


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "r", F(self.r))
        object.__setattr__(self, "i", F(self.i))

    @staticmethod
    def get(z):
        return z if isinstance(z, G) else G(z)

    def __add__(self, z):
        z = G.get(z)
        return G(self.r + z.r, self.i + z.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, z):
        return self + (-G.get(z))

    def __rsub__(self, z):
        return G.get(z) + (-self)

    def __mul__(self, z):
        z = G.get(z)
        return G(self.r*z.r-self.i*z.i, self.r*z.i+self.i*z.r)

    __rmul__ = __mul__

    def __truediv__(self, z):
        z = G.get(z)
        t = z.r*z.r + z.i*z.i
        if not t:
            raise ZeroDivisionError
        p = self*z.conj()
        return G(p.r/t, p.i/t)

    def __rtruediv__(self, z):
        return G.get(z)/self

    def __bool__(self):
        return bool(self.r or self.i)

    def conj(self):
        return G(self.r, -self.i)

    def norm2(self):
        return G(self.r*self.r+self.i*self.i)

    def __str__(self):
        return str(self.r) if not self.i else f"({self.r}+{self.i}i)"


def dot(u, v):
    return sum((a*b for a, b in zip(u, v)), G())


def mv(a, v):
    return [dot(row, v) for row in a]


def mat(a):
    return [[G.get(x) for x in row] for row in a]


def det(a):
    a = [row[:] for row in a]
    answer = G(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return G()
        if j != k:
            a[j], a[k] = a[k], a[j]
            answer = -answer
        p = a[j][j]
        answer = answer*p
        for k in range(j+1, len(a)):
            t = a[k][j]/p
            for l in range(j+1, len(a)):
                a[k][l] = a[k][l]-t*a[j][l]
            a[k][j] = G()
    return answer


def solve(a, b):
    a = [row[:] + [v] for row, v in zip(a, b)]
    n = len(b)
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[j], a[k] = a[k], a[j]
        p = a[j][j]
        a[j] = [v/p for v in a[j]]
        for k in range(n):
            if k != j:
                t = a[k][j]
                a[k] = [v-t*w for v, w in zip(a[k], a[j])]
    return [row[-1] for row in a]


def shifted(a, x):
    return [[G(x if i == j else 0)-a[i][j]
             for j in range(len(a))] for i in range(len(a))]


def qmatrix(a, b, lam):
    a = [[v/lam for v in row] for row in a]
    b = [v/lam for v in b]
    s = sum((v.norm2() for row in a for v in row), G())
    beta = sum((v.norm2() for v in b), G())
    q = [[G() for _ in range(6)] for _ in range(6)]
    q[0][:2] = [beta, s]
    q[1][0] = G(1)
    for j in range(2):
        q[0][2+j] = sum((b[i].conj()*a[i][j] for i in range(2)), G())
        q[0][4+j] = q[0][2+j].conj()
        q[2+j][0], q[4+j][0] = b[j].conj(), b[j]
        for i in range(2):
            q[2+j][4+i], q[4+j][2+i] = a[j][i].conj(), a[j][i]
    return q, a, b, s, beta


def geometric_coefficients(a, b, lam, max_length):
    """Coefficients of lam^-1 sum_{k=0}^N (f/lam)^k, clipped by word length."""
    polynomial = {(i,): b[i]/lam for i in range(2)}
    polynomial.update({(i,j): a[i][j]/lam for i in range(2) for j in range(2)})
    power, total = {(): G(1)}, {(): G(1)/lam}
    for _ in range(max_length):
        nxt = {}
        for u, c in power.items():
            for v, d in polynomial.items():
                if c and d and len(u)+len(v) <= max_length:
                    nxt[u+v] = nxt.get(u+v, G()) + c*d
        power = nxt
        for w, c in power.items():
            total[w] = total.get(w, G()) + c/lam
    return total


def state(c, n):
    x = sum((c.get(w, G()).norm2() for w in product(range(2), repeat=n)), G())
    xp = sum((c.get(w, G()).norm2() for w in product(range(2), repeat=n+1)), G())
    h = [sum((c.get(w, G())*c.get((j,)+w, G()).conj()
              for w in product(range(2), repeat=n)), G()) for j in range(2)]
    return [xp, x] + h + [v.conj() for v in h]


def main():
    rng = random.Random(260319528)
    cases = [
        (mat([[0,0],[0,0]]), [G(),G()], G(1)),
        (mat([[0,0],[0,0]]), [G(1),G(0,1)], G(2,1)),
        (mat([[4,0],[0,0]]), [G(),G()], G(1)),
        (mat([[-2,0],[0,1]]), [G(3),G()], G(1)),
        (mat([[-2,0],[0,0]]), [G(3),G()], G(1)),
        (mat([[F(1,2),F(1,2)],[F(1,2),F(1,2)]]), [G(F(1,2)),G(F(1,2))], G(2,1)),
        (mat([[0,1],[1,0]]), [G(1),G(1)], G(2,-1)),
        (mat([[1,0],[1,-1]]), [G(1),G(0,1)], G(2,1)),
        (mat([[G(0,F(1,2)),1],[2,1]]), [G(),G()], G(2)),
        (mat([[0,1],[-1,0]]), [G(1),G(0,1)], G(1,1)),
        (mat([[0,1],[0,0]]), [G(1),G(1)], G(1,-1)),
        (mat([[1,2],[0,3]]), [G(1),G(-1)], G(3,1)),
    ]
    for _ in range(36):
        a = [[G(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in range(2)] for _ in range(2)]
        b = [G(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in range(2)]
        cases.append((a,b,G(rng.randrange(1,4),rng.randrange(-2,3))))
    counts = dict(state_components=0, coefficient_equations=0, determinants=0,
                  schur_complements=0, boundary_examples=0)
    for a,b,lam in cases:
        q, al, bl, s, beta = qmatrix(a,b,lam)
        c = geometric_coefficients(a,b,lam,7)
        z = [G(1)/lam.norm2()] + [G()]*5
        for n in range(7):
            z = mv(q,z)
            expected = state(c,n)
            for actual, wanted in zip(z,expected):
                assert actual == wanted, (a,b,lam,n,actual,wanted)
                counts["state_components"] += 1
        for n in range(1,8):
            for w in product(range(2),repeat=n):
                lhs = lam*c.get(w,G())
                rhs = b[w[0]]*c.get(w[1:],G())
                if n >= 2:
                    rhs += a[w[0]][w[1]]*c.get(w[2:],G())
                assert lhs == rhs
                counts["coefficient_equations"] += 1
        assert det(q) == -s*det(al).norm2()
        counts["determinants"] += 1
        h = [[q[i+2][j+2] for j in range(4)] for i in range(4)]
        row = bl + [z.conj() for z in bl]
        col = [z.conj() for z in bl] + bl
        for x in (7,11):
            block = shifted(h,x)
            if not det(block):
                continue
            d = G(x*x)+beta*x-s-dot(row,solve(block,col))*x*x
            assert det(shifted(q,x)) == det(block)*d
            counts["schur_complements"] += 1
    # A rank-one endpoint with a dominant eigenvalue unseen by some left vectors
    # still has a left eigenvector pairing nontrivially with e_1.
    q,_,_,_,_ = qmatrix(mat([[-2,0],[0,0]]),[G(3),G()],G(1))
    left = [G(1),G(2),G(F(-3,2)),G(),G(F(-3,2)),G()]
    assert [dot(left,list(col)) for col in zip(*q)] == [2*z for z in left]
    counts["boundary_examples"] += 1
    # The printed symmetric Schur formula is missing ||b_1||^2=9.
    q,_,_,_,_ = qmatrix(mat([[-2,0],[0,1]]),[G(3),G()],G(1))
    h = [[q[i+2][j+2] for j in range(4)] for i in range(4)]
    actual = det(shifted(q,3))/det(shifted(h,3))
    corrected, printed = G(F(-7,5)), G(F(17,5))
    assert actual == corrected and actual != printed
    counts["boundary_examples"] += 1
    # The invariant cyclic subspace, not all eigenvalues of an arbitrary matrix,
    # determines whether a specified orbit decays.
    hidden = mat([[0,0],[0,2]])
    assert mv(hidden,[G(1),G()]) == [G(),G()]
    assert det(shifted(hidden,2)) == G()
    counts["boundary_examples"] += 1
    print("Arithmetic: exact Gaussian rationals; seed=260319528; cases=48; max_word_length=7")
    for name,count in counts.items():
        print(f"{name}: {count} passed")
    print("Missing-factor witness: A=diag(-2,1), b=(3,0), lambda=1, x=3")
    print("Schur value: actual=corrected=-7/5; printed=17/5")
    print("All stated finite checks passed; no general convergence or random-matrix claim is certified.")


if __name__ == "__main__":
    main()
