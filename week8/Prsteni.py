import sys
input = sys.stdin.readline
from fractions import Fraction
import math



n:int = int(input())
rings: list[int] = list(map(int, input().split()))

for i in range(1, len(rings)):
    ring = rings[i]
    # print(Fraction(rings[0]/ring))
    gcd = math.gcd(rings[0], ring)
    a = Fraction(rings[0]/gcd)
    b = Fraction(ring/gcd)
    print(str(a)+"/"+str(b))