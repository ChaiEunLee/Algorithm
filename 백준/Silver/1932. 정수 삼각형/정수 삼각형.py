n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))
    
dp = []
for i in range(1,n+1):
    dp.append([0]*i)
dp[0] = tri[0]

for i in range(1,n):
    for j in range(i+1):
        #print(i,j,tri[i][j])
        right,left,mid = 0,0,0
        if j==0:
            right = dp[i-1][j]
        elif j==i:
            left = dp[i-1][j-1]
        else:
            mid = max(dp[i-1][j-1], dp[i-1][j])
        dp[i][j] = tri[i][j] + max(right, left, mid)
print(max(dp[n-1]))