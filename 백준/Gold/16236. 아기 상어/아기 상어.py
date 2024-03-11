from collections import deque
# 엄마 상어에게 도움을 요청하지 않고 잡아먹을 수 있는 시간
# 크기가 같은 물고기는 지나가기만 가능
# 작아야 먹기 가능, 크면 못지나감
# 자기만큼 먹어야 1증가
# 9: 아기상어의 위치, 크기는 2
# 가장 가까운 물고리, 
# 위, 왼쪽 우선순위

import sys
input = sys.stdin.readline
N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))

INF = 1e9

now_size = 2
now_x, now_y = 0,0

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            now_x, now_y = i,j
            sea[now_x][now_y] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    # 값이 -1이면 도달불가하다는 의미
    dist = [[-1]*N for _ in range(N)]
    # 시작 위치는 도달가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1 and sea[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
        #print(dist, queue)
    return dist

def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1 and 1<=sea[i][j] and sea[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist

result = 0
ate = 0

while True:
    value = find(bfs()) # 먹을 수 있는 물고기의 위치 찾기
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        sea[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0