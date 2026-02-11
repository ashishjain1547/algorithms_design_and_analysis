def minUpdates (N, A, K):
    # write your code here
    s = set()
    odd = 0
    even = 0

    for i in range(N):
        if A[i] not in s:
            s.add(A[i])
            if A[i] % 2 == 0:
                even += 1
            else:
                odd += 1
    if odd > N // 2 or even > N // 2:
        return -1

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = minUpdates(N, A, K)
    print (out_)