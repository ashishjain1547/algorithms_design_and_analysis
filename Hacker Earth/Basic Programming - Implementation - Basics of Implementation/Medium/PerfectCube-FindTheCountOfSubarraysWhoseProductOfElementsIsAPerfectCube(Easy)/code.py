from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# Note: The code below is following the "Sieve of Eratosthenes" algorithm for finding primes.
MAX_A = 100
is_prime = [True] * (MAX_A + 1)
primes = []
for i in range(2, MAX_A + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i, MAX_A + 1, i):
            is_prime[j] = False
            
#print(primes)


def cube_signature(x):
    sig = []
    for p in primes:
        #if p * p * p > x:
        #    break
        # Bug with the above two lines: when x=18, it returned ((2, 1), (9, 1))
        
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        if cnt % 3 != 0:
            sig.append((p, cnt % 3))
    if x > 1:
        sig.append((x, 1))
    
    return tuple(sig)

#print("For 14:")
#print(cube_signature(14))
#print("For 18:")
#print(cube_signature(18))


prefix = defaultdict(int)
prefix[()] = 1

current = defaultdict(int)
answer = 0

for x in A:
    sig = cube_signature(x)
    for p, cnt in sig:
        current[p] = (current[p] + cnt) % 3
        if current[p] == 0:
            del current[p]
    
    print("-----------------------------")
    key = tuple(sorted(current.items()))
    print(key)
    answer += prefix[key]
    print(answer)
    prefix[key] += 1
    print(prefix[key])
    print("-------------------------")
    
    
print(answer)


"""
FAILING THIS TEST CASE

N = 5
A = [18, 2, 3, 12, 6]
Expected output: 2

Why?

[2,3,12] = 72 = 2³×3² ❌

[3,12,6] = 216 = 6³ ✅

[18,2,3,12,6] = cube ✅
----------------------------------

🔹 6. Zero handling (critical edge case)
Case 11
N = 3
A = [0, 5, 7]


Any subarray containing 0 has product 0 = 0³

Subarrays:

[0]

[0,5]

[0,5,7]

✅ Expected output: 3

📌 If your code doesn’t handle zero separately, it will break.

🔹 7. Stress / randomized structure
Case 12
N = 6
A = [2, 4, 2, 4, 2, 4]


Expected output: 5

Multiple overlapping cube segments.

📌 Tests performance + correctness.


"""

