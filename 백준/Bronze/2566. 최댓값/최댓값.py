#2. 최댓값
matrix = [[0]*9 for i in range(9)]
max_r = 0
max_c = 0
max_val = 0
for i in range(9):
    matrix[i] = list(map(int, input().split()))
    if max_val <= max(matrix[i]):
        max_val = max(matrix[i])
        max_c = matrix[i].index(max(matrix[i]))+1
        max_r = i+1
print(max_val)
print(max_r, max_c)