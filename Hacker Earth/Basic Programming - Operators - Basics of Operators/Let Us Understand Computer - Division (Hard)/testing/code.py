import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X = int(input())
    
    k = (math.isqrt(1 + 4*X) - 1) // 2
    print(X - k)
