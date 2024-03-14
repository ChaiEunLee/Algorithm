import sys
input = sys.stdin.readline
N = int(input())
board = [[0]*N for _ in range(N)]
direction = []
r,c,dir = 0,0,0
dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
d = 0
min = 0
queue = [[0,0]]

for _ in range(int(input())):
    i,j = map(int, input().split())
    board[i-1][j-1] = 1

for _ in range(int(input())):
    X,C = map(str, input().split())
    direction.append([int(X),C])
    

while True:
    min += 1
    r += dirs[dir][0]
    c += dirs[dir][1]
    if [r,c] in queue:
        break
    if r<0 or r>=N or c<0 or c>=N:
        #print(r,c)
        break
    
    if board[r][c] == 1:
        board[r][c] = 0
    else:
        queue.pop(0)
        #board[startr][startc] = 0
    #board[r][c] = 0
    queue.append([r,c])

    if d<len(direction) and direction[d][0] == min:
        if direction[d][1] == 'L':
            dir = (dir+1)%4
        else:
            dir = (dir+3)%4
        d+=1
print(min)