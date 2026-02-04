N, K = map(int, input().split())

digits = list(map(int, str(N)))

stack = []

for digit in digits:
    while K > 0 and stack and stack[-1] < digit:
        stack.pop()
        K -= 1
    stack.append(digit)

# If there are still K digits to remove, remove from the end
while K > 0:
    stack.pop()
    K -= 1

print(''.join(map(str, stack)))