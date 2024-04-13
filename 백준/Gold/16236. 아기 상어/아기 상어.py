# NxN
# M fish
# 1 baby shark
# babysharksize = 2
# 상하좌우
# 자기보다 큰 물고기가 있으면 지나갈수 없음.
# 자기보다 작은 물고기만 먹을 수 있음
# 크기가 같으면 지나갈수 있지만 먹을 수 없음

N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if sea[i][j]==9:
            shark = [i,j]
            sea[i][j] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

INF = 1e9
sharksize = 2

def bfs():
    dist = [[-1] *N for _ in range(N)]
    x,y = shark
    q = [(x,y)]
    dist[x][y] = 0
    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1 and sea[nx][ny] <= sharksize:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1 and 1<=sea[i][j] and sea[i][j]<sharksize:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x,y = i,j
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist


# 더이상 먹을 수 있는 물고기가 없으면 끝
# 먹을 수 있는 가장 가까운 물고기 찾기 (상 -> 좌)
result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        shark = [value[0], value[1]]
        result += value[2]
        sea[shark[0]][shark[1]] = 0
        ate += 1
        if ate >= sharksize:
            sharksize += 1
            ate = 0