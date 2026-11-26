"""Independent brute-force check for the one-descent derangement distribution."""
from collections import Counter
from fractions import Fraction
from itertools import permutations

def distribution(n):
    out=Counter()
    for p in permutations(range(1,n+1)):
        if sum(a>b for a,b in zip(p,p[1:]))==1 and all(j!=v for j,v in enumerate(p,1)):
            out[p[0]]+=1
    return out

if __name__=="__main__":
    for n in range(2,9):
        h=distribution(n)
        assert h=={**{j:2**(n-j-1) for j in range(2,n)},n:1},(n,h)
        assert Fraction(sum(v*k for v,k in h.items()),sum(h.values()))==3-Fraction(1,2**(n-2))
    print("One-descent derangements: exact full distributions agree for n=2..8.")
