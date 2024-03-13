import sys
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
visited = [False for _ in range(N)]
INF = 2147000000
res = INF



def dfs(L,idx):
    global res
    #print("L,idx: ", L, idx)
    if L == N//2: #if length == L//2
        A = 0
        B = 0
        # i,j 조합 잘 찾아서 계산
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        res = min(res, abs(A-B))
        return 
    # 0~N-1 돌면서 
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1) #dfs(Length, index), length +1씩 늘어나고, index는 (1,2,3), (1,3,4), (1,4,5), (1,4,6), (2,3,4), (2,4,5), ... 이런식으로 앞에서부터 누적으로 늘어남.
            visited[i] = False
dfs(0,0)
print(res)