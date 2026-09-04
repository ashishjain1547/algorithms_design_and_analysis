import math

def solve(a, b):
    l = math.lcm(a, b)
    return (l//a, l//b)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    out_ = solve(a, b)
    print(out_[0], out_[1])
