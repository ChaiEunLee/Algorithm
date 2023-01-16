N = int(input())
paper = [[0]*100 for i in range(100)]

for i in range(N):
    x,y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            paper[x+j][y+k] = 1
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]
        
print(total)