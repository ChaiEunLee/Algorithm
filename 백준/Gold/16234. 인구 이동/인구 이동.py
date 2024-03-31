import sys
sys.setrecursionlimit(100000)

N,L,R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))


def DFS(x,y):
    global newval
    global newcnt
    for dir in range(4):
        if 0<=x+dx[dir]<N and 0<=y+dy[dir]<N:
            nx = x+dx[dir]
            ny = y+dy[dir]
            if not visited[nx][ny]:
                if L <= abs(A[x][y]-A[nx][ny]) <= R:
                    visited[nx][ny] = True
                    newval += A[nx][ny]
                    newcnt += 1
                    stack.append([nx,ny])
                    DFS(nx,ny)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
step = -1
region = 0
while region < N*N:
    region = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                #region += 1
                stack = [[i,j]]
                newval = A[i][j]
                newcnt = 1
                visited[i][j] = True
                DFS(i,j)
            if newcnt == 1:
                region += 1
            if region == N*N:
                break
            #print(stack, newval, newcnt)
            while stack:
                x,y = stack.pop()
                A[x][y] = int(newval/newcnt)
    step += 1

print(step)

# for i, j in N 
# if not visited 
# start DFS ()

#IN DFS ()
# 상하좌우 방문해서 값비교
# 연합이 될만하다면 방문 처리
# DFS에 추가 # 추가할 때 넣을 값을 위해 value, cnt 기억
# DFS에 들어간 곳을 다 기억해놔야하는데... x,y 기억? stack으로 기억. 

# OUT of DFS
# 아 아니지 visited로 했으니까 괜찮겠다. 고르고 바꾸고 새로운 DFS 시작하는 방식으로.
# 마지막에 값 추가할 때 stack을 하나 만들어놓고 거기다가 넣으면 될듯. 
 
