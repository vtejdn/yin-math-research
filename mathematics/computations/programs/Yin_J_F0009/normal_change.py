"""Actual free Haar/Poisson moments for a normal coordinate change.

Development diagnostic for D_F0006. Fractions are exact; N is a finite
Neumann truncation, not the full normal-coordinate derivation.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
import json
import argparse

R=Q(1,2)
# Blocks: (algebra, exponent, h-power, h-star-power).
# U is Haar; h(V)=1+i*f_r(V), where the Poisson score f_r is real.
def norm(w):
    out=[]
    for t in w:
        t=tuple(t)
        if t[1:]==(0,0,0): continue
        if out and out[-1][0]==t[0]:
            s=out.pop(); t=(t[0],s[1]+t[1],s[2]+t[2],s[3]+t[3])
        if t[1:]!=(0,0,0): out.append(t)
    return tuple(out)
def cat(*w): return norm(sum((tuple(t) for t in w),()))
def U(n=1): return norm(((0,n,0,0),))
def V(n=1): return norm(((1,n,0,0),))
H=((1,0,1,0),)
def star(w): return tuple((l,-n,q,p) for l,n,p,q in reversed(w))
def canonical(w):
    w=norm(w)
    while len(w)>1 and w[0][0]==w[-1][0]:
        w=norm((w[-1],w[0])+w[1:-1])
    return min(w[j:]+w[:j] for j in range(len(w))) if w else ()
@lru_cache(None)
def mu(n,p,q):
    assert p+q<=2
    k=abs(n); m=R**k
    if p+q==0:return m
    if (p,q)==(1,0):return (1-n)*m
    if (p,q)==(0,1):return (1+n)*m
    s=R*R
    f2=m*(-Q(k*(k-1),2)+(k+1)*s/(1-s)+(s+s*s)/(1-s)**2)
    if (p,q)==(1,1):return m+f2
    return (1+(-2*n if p==2 else 2*n))*m-f2
def tr(w):return tr0(canonical(w))
@lru_cache(None)
def tr0(w):
    if not w:return Q(1)
    if sum(n for l,n,p,q in w if l==0):return Q(0)
    if len(w)==1:
        l,n,p,q=w[0]
        return mu(n,p,q) if l==1 else Q(n==0)
    positions=[j for j,t in enumerate(w) if t[0]==1]
    out=Q(0)
    for size in range(1,len(positions)+1):
        for removed in combinations(positions,size):
            coefficient=Q(1)
            for j in removed:coefficient*=mu(*w[j][1:])
            if coefficient:
                out+=(1 if size%2 else -1)*coefficient*tr(tuple(t for j,t in enumerate(w) if j not in removed))
    return out
def p_add(out,w,c):
    w=norm(w); out[w]=out.get(w,Q(0))+c
    if not out[w]:del out[w]
def p_mul(a,b):
    out={}
    for w,c in a.items():
        for z,d in b.items():p_add(out,cat(w,z),c*d)
    return out
def p_inner(a,b):
    return sum(c*d*tr(cat(star(w),z)) for w,c in a.items() for z,d in b.items())
def block(l,n):
    if l==0:
        if n>0:return [(1,U(k),U(n-1-k)) for k in range(n)]
        return [(-1,U(-k-1),U(n+k)) for k in range(-n)]
    if n>0:return [(1,V(k),cat(U(-1),V(n-k))) for k in range(n)]
    return [(-1,V(-k-1),cat(U(-1),V(n+k+1))) for k in range(-n)]
def deriv(w):
    assert all(p==q==0 for l,n,p,q in w)
    return [(s,cat(w[:j],a),cat(b,w[j+1:])) for j,(l,n,p,q) in enumerate(w) for s,a,b in block(l,n)]
@lru_cache(None)
def e0(w):
    out={}
    for s,a,b in deriv(w):p_add(out,a,s*tr(b))
    return out
@lru_cache(None)
def eps_e(w):
    # epsilon=-I_(U tensor U) delta, hence E_epsilon(p)=-(E_delta(pU)-p)U.
    out={cat(w,U()):Q(1)}
    for v,c in e0(cat(w,U())).items():p_add(out,cat(v,U()),-c)
    return out
def T(a,lam,N):
    out={}
    for n in range(N+1):
        for k in range(n+1):
            ell=n-k; coefficient=(-lam)**n*comb(n,k)
            for w,c in a.items():
                p_add(out,cat(w,U(-k),H,U(1-ell)),coefficient*c)
                for z,d in eps_e(cat(w,U(-k))).items():
                    p_add(out,cat(z,U(-ell)),-coefficient*c*d)
                if ell:p_add(out,cat(w,U(1-n)),-coefficient*c)
    return out
def serialize(q):return str(q)
def unitary_controls():
    xi=T({():Q(1)},Q(0),0)
    xi2=1+2*R*R/(1-R*R)**2
    assert tr(cat(H,star(H)))==xi2
    assert tr(cat(star(H),V(-1)))==0
    count=2
    for n in range(1,6):
        w=cat(U(-n),V(n));a={w:Q(1),star(w):Q(1)}
        geometric=sum(R**(2*j) for j in range(1,n))
        ta=T(a,Q(0),0)
        assert p_inner(ta,ta)==2*xi2+geometric
        assert p_inner(T(p_mul(a,a),Q(0),0),xi)==2*xi2
        b=dict(a);p_add(b,(),Q(3));tb=T(b,Q(0),0)
        assert p_inner(T(p_mul(b,b),Q(0),0),xi)-p_inner(tb,tb)==-geometric
        count+=3
    return count
def main():
    global R
    parser=argparse.ArgumentParser()
    parser.add_argument('--r',default='1/2')
    parser.add_argument('--lam',default='1/5')
    parser.add_argument('--N',type=int,default=5)
    parser.add_argument('--controls-only',action='store_true')
    args=parser.parse_args();R=Q(args.r);lam=Q(args.lam);N=args.N
    assert 0<R<1 and abs(lam)<Q(1,2) and N>=0
    controls=unitary_controls()
    if args.controls_only:
        print(json.dumps({'r':str(R),'unitary_degrees':[1,2,3,4,5],'exact_controls':controls}))
        return
    candidates={
      'Uminus2V2':cat(U(-2),V(2)),
      'commutator':cat(U(),V(),U(-1),V(-1)),
      'UminusV2':cat(U(-1),V(2)),
      'Uminus2V':cat(U(-2),V()),
      'Uplus2V2':cat(U(2),V(2)),
      'V':V(),
    }
    xi=T({():Q(1)},lam,N)
    results=[]
    basis=[]; images=[]
    for name,w in candidates.items():
        a={w:Q(1),star(w):Q(1)}
        ta=T(a,lam,N);tb=T(p_mul(a,a),lam,N)
        basis.append(a);images.append(ta)
        lhs=p_inner(ta,ta); pairing=p_inner(tb,xi)
        results.append({'test':name,'norm2':str(lhs),'pairing':str(pairing),
                        'ratio':float(lhs/pairing) if pairing else None,
                        'factor_two_difference':str(2*pairing-lhs),
                        'vector_terms':len(ta)})
    # Exact quadratic form on the real span of the six selfadjoint tests.
    matrix=[]
    for i,a in enumerate(basis):
        row=[]
        for j,b in enumerate(basis):
            ab=p_mul(a,b)
            for w,c in p_mul(b,a).items():p_add(ab,w,c)
            row.append(p_inner(T(ab,lam,N),xi)-p_inner(images[i],images[j]))
        matrix.append(row)
    assert matrix==[list(t) for t in zip(*matrix)]
    schur=[row[:] for row in matrix];pivots=[];ldl_status='positive definite'
    for k in range(len(schur)):
        pivot=schur[k][k];pivots.append(pivot)
        if pivot<=0:
            ldl_status='nonpositive pivot; requires further analysis';break
        for i in range(k+1,len(schur)):
            for j in range(k+1,len(schur)):
                schur[i][j]-=schur[i][k]*schur[k][j]/pivot
    result={'r':str(R),'lambda':str(lam),'N':N,'exact_controls':controls,
            'scope':'finite Neumann approximation only; no tail-certified inequality conclusion',
            'results':results,'factor_two_matrix':[[str(v) for v in row] for row in matrix],
            'exact_ldl_status':ldl_status,'exact_ldl_pivots':[str(p) for p in pivots]}
    program=Path(__file__).resolve().parent
    repo=next(p for p in program.parents if (p/'repository/config.json').is_file())
    folder=repo/'mathematics/computations/outputs'/program.name;folder.mkdir(parents=True,exist_ok=True)
    destination=folder/f'normal-change-r{str(R).replace("/","-")}-l{str(lam).replace("/","-")}-N{N}.json'
    temporary=destination.with_suffix('.partial')
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(destination)
    print(json.dumps({'r':str(R),'lambda':str(lam),'N':N,'exact_controls':controls,
                      'exact_ldl_status':ldl_status,
                      'results':[{'test':r['test'],'ratio':r['ratio'],'terms':r['vector_terms']} for r in results]},indent=2))
if __name__=='__main__':main()

