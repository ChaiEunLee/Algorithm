#1. 행렬 덧셈
N, M = map(int, input().split())
matrix = [[0]*M for i in range(N)]
for i in range(N):
    matrix[i] = list(map(int, input().split()))
A = matrix

matrix = [[0]*M for i in range(N)]       
for i in range(N):
    matrix[i] = list(map(int, input().split()))
B = matrix

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end = ' ')
    print()