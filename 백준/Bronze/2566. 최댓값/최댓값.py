matrix = [[0]*9 for i in range(9)]

for i in range(9):
    matrix[i] = list(map(int, input().split()))
    
maxval = 0
indexi = 0
indexj = 0
for i in range(9):
    for j in range(9):
        if (matrix[i][j] > maxval):
            maxval = matrix[i][j]
            indexi=i
            indexj=j
            
print(maxval)
print(indexi+1, indexj+1)