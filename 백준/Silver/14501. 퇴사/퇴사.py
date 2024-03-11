# dp
import sys
input = sys.stdin.readline
N = int(input())
plan = []
for _ in range(N):
    plan.append(list(map(int, input().split())))
    
# 최대값을 누적하는 방식
dp = [0 for _ in range(N+1)]

for i in range(N): #0~N-1까지 돌면서 1일 후에 벌면 1~N이 되게
    day = plan[i][0]
    price = plan[i][1]

    for j in range(i+day,N+1): #정산일자 ~ 끝까지 누적
        if dp[j] < dp[i]+price:
            dp[j] = dp[i]+price
print(dp[-1])