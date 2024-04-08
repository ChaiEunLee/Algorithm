N,M,K = map(int,input().split())
queue = []
for _ in range(M):
    row = list(map(int,input().split()))
    row[0] -= 1
    row[1] -= 1
    queue.append(row)

dirdict = {0:[-1,0],1:[-1,1],2:[0,1],3:[1,1],4:[1,0],5:[1,-1],6:[0,-1],7:[-1,-1]}

# r,c에 여러개 있는거 정보 저장 어떻게 하지?? 
# 각 칸마다 queue??
# index를 버리면 어떻게 풀지?
for _ in range(K):
    newqueue = []
    visited = [[0]*(N) for _ in range(N)]
    mass = [[0]*(N) for _ in range(N)]
    speed = [[0]*(N) for _ in range(N)]
    direction = [[0]*(N) for _ in range(N)]
    nextdirection = [[[0]*2 for _ in range(N)] for _ in range(N)]

    while queue:
        r,c,m,s,d = queue.pop()
        #print(r,c,m,s,d)
        nx = r+dirdict[d][0]*s
        ny = c+dirdict[d][1]*s
        nx = (nx)%N
        ny = (ny)%N
        #print('after: ', nx,ny)
        #print(r,c,m,s,d,nx,ny)
        visited[nx][ny] += 1
        mass[nx][ny] += m
        speed[nx][ny] += s
        direction[nx][ny] += d
        # 홀짝
        if d%2==1:
            nextdirection[nx][ny][0] += 1
        else:
            nextdirection[nx][ny][1] += 1
    #print('visited: ', visited)
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] > 0:
                if visited[i][j] == 1:
                    newqueue.append([i,j,mass[i][j], speed[i][j], direction[i][j]])
                else:
                    newmass = mass[i][j]//5
                    if newmass == 0:
                        continue
                    newspeed = speed[i][j]//visited[i][j]
                    #print("newmass, newspeed: ", newmass, newspeed)
                    if nextdirection[i][j][0] == 0 or nextdirection[i][j][1] == 0:
                        newdirection = 0
                    else:
                        newdirection = 1

                    for _ in range(4):
                        newqueue.append([i,j,newmass,newspeed,newdirection])
                        newdirection += 2
    queue = newqueue.copy()
    #print(newqueue)
answer = 0
while newqueue:
    r,c,m,s,d = newqueue.pop()
    answer += m
print(answer)