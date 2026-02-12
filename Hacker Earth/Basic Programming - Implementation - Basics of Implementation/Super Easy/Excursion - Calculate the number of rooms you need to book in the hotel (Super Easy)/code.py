import math

def solve(N, M, K):
    out = math.ceil(N / K) + math.ceil(M / K)
    return out

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    out = solve(N, M, K)
    print(out)