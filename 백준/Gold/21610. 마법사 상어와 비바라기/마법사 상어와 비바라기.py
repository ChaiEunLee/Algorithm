N,M = map(int,input().split())
A=[]
info=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(M):
    info.append(list(map(int,input().split())))
    

dirdict = {1:[0,-1], 2:[-1,-1], 3:[-1,0],4:[-1,1],5:[0,1],6:[1,1],7:[1,0],8:[1,-1]}
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

def ifdiagok(x,y):
    cnt = 0
    for nx,ny in [x+1,y+1],[x+1,y-1],[x-1,y-1],[x-1,y+1]:
        if 0<=nx<N and 0<=ny<N:
            if A[nx][ny]>0:
                cnt += 1
    return cnt

for i in range(M):
    #print(A)
    dir = info[i][0]
    step = info[i][1]
    water = []
    visited = [[0]*N for _ in range(N)]
    for x,y in cloud:
        # 1. 구름이 d 방향 s칸 이동
        nx,ny = (x+dirdict[dir][0]*step)%N, (y+dirdict[dir][1]*step)%N
        # 2. A[nx][ny] += 1 , 물이 증가한 nx,ny 정보 저장하기
        water.append([nx,ny]) 
        A[nx][ny] += 1 # 물의 양 1 증가
        visited[nx][ny] = 1

    # 3. 구름 사라짐
    cloud = [] # 구름 사라짐.
    
    # 4. 2에서 물이 증가한 nx,ny 각각 loop 돌면서 (queue)
    for x,y in water: # step2에서 물이 증가한 구름 하나씩 꺼내서 대각선 물 채우기
        # 대각선 방향 물 +=1 (가장자리는 X)
        A[x][y] += ifdiagok(x,y)

    # 5. 물이 2이상이면 구름이 생기고 물의 양이 2 줄어듦. 2에서 저장한 nx,ny면 가만히 있음. 
    two = [] # 2이상인거 저장
    for i in range(N):
        for j in range(N):
            if A[i][j]>=2 and visited[i][j] == 0:
                A[i][j] -= 2 
                cloud.append([i,j])

sum = 0
for i in range(N):
    for j in range(N):
        sum += A[i][j]
print(sum)