def solve(n):
    found = False
    while not found:
        s = sum(map(int, str(n)))
        if s % 4 == 0:
            found = True
            return n
        n += 1

T = int(input())

for _ in range(T):
    n = int(input())
    out_ = solve(n)
    print (out_)