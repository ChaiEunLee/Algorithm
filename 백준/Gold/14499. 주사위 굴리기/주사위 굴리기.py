N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# move 
# east 1, west 2, north 3, south 4
move = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0,0,0,0,0,0] # dice[0]: up, dice[5]: bottom
# dice = [up, north, east, west, south, bottom]
# east : [4,2,1,6,5,3]
# west : [3,2,6,1,5,4]
# north : [5,1,3,4,6,2]
# south : [2,6,3,4,1,5]
def changedice(dir, dice):
    if dir == 1: #east
        dice = [dice[j] for j in [3,1,0,5,4,2]]
    elif dir == 2: #west
        dice = [dice[j] for j in [2,1,5,0,4,3]]
    elif dir == 3: #north
        dice = [dice[j] for j in [4,0,2,3,5,1]]
    else:
        dice = [dice[j] for j in [1,5,2,3,0,4]]
    return dice

for i in move:
    # move x,y
    if 0<=x+dx[i-1]<N and 0<= y+dy[i-1] < M:
        x += dx[i-1]
        y += dy[i-1]
        # change dice number 
        dice = changedice(i, dice)
        # change dice bottom, map value 
        if board[x][y]==0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])