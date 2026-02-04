N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

rowSum = [0] * N
colSum = [0] * M

for i in range(N):
    for j in range(M):
        rowSum[i] += A[i][j]
        colSum[j] += A[i][j]

best_score = -1
best_row = -1
best_col = -1

for i in range(N):
    for j in range(M):
        score = rowSum[i] + colSum[j] - 2 * A[i][j]

        # print("Score: ", score)
        # print(best_score, best_row, best_col)

        if score > best_score or (score == best_score and (i + 1 < best_row or (i + 1 == best_row and j + 1 < best_col))):
            best_score = score
            best_row = i + 1
            best_col = j + 1

print(best_row, best_col)