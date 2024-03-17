N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 점수합산
def bfs(x, y, num):
    visited[x][y] = 1
    q.append([x,y])
    value = 0
    while q:
        x,y = q.pop(0)
        for nx, ny in (x+1,y), (x-1,y), (x, y-1), (x,y+1):
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == 0 and board[nx][ny] == num:
                    value += 1
                    visited[nx][ny] = 1
                    q.append([nx,ny])
    return value+1 #시작지점 포함해서

def changedice(dir):
    if dir == 0: #east
        change = [3,1,0,5,4,2]
    elif dir == 1: #south
        change = [1,5,2,3,0,4]
    elif dir == 2: #west
        change = [2,1,5,0,4,3]
    else: #north
        change = [4,0,2,3,5,1]
    return [dice[i] for i in change]


#-1해서 생각할거임
r,c = 0,0
# clock +1, anticlock -1 #동남서북 순서대로
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dice = [1,2,3,4,5,6]
dir = 0 #east로 시작
score = 0

for _ in range(K):
    # 벽에 도달하면 거꾸로 후진하게 방향 change
    if r+dx[dir]<0 or r+dx[dir]>=N or c+dy[dir]<0 or c+dy[dir]>=M:
        dir = (dir+2)%4

    # 1st move
    r += dx[dir]
    c += dy[dir]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = []
    C = bfs(r,c,board[r][c]) #board[r][c]랑 똑같은 숫자가 근처에 있는 개수
    ## 계산
    score += board[r][c] * C

    dice = changedice(dir)
    ## dice 회전
    if dice[5] > board[r][c]:
        dir = (dir+1)%4 # 시계방향
    elif dice[5] < board[r][c]:
        dir = (dir-1)%4
print(score)