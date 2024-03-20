
def solution(park, routes):
    parks = []
    obstacles = []
    for i in range(len(park)):
        parks.append(list(park[i]))
        if 'S' in list(park[i]):
            for j in range(len(parks[i])):
                if parks[i][j] == 'S':
                    x,y = i,j

    # 동남서북이라서 +1,
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for tmp in routes:
        route = list((tmp.split(' ')[0],int(tmp.split(' ')[1])))
        if route[0] == 'E':
            i = 0
        elif route[0] == 'S':
            i = 1
        elif route[0] == 'W':
            i = 2
        else:
            i = 3

        if 0<=x+dx[i]*route[1]<len(parks) and 0<=y+dy[i]*route[1]<len(parks[0]):
            nx,ny = x,y
            for _ in range(route[1]): #다 돌면서 
                nx = nx + dx[i]
                ny = ny + dy[i]
                if parks[nx][ny] == 'X':
                    nx, ny = x,y #원상복구
                    break
            x = nx
            y = ny
        #print(x,y)
    answer = [x,y]
    return answer