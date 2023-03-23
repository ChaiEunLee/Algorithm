n = int(input())
m = int(input())

INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
        
# 출발지, 도착지 같을 때 0으로 초기화 하는거 잊지말기!
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end=' ')
    print()