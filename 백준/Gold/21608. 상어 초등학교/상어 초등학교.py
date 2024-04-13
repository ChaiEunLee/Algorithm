# NxN
# 1. 좋아하는 학생이 많은 인접한 칸으로
# 2. 1이 여러개라면 인접한 칸 중 비어있는 칸이 가장 많은 칸으로
# 3. 2가 여러개라면 행의 번호가 작은 칸 -> 열의 번호가 작은 칸
def search_seat(student):
    maxlike = 0
    queue = []
    # 좋아하는 학생 수, 빈칸 수 탐색
    for i in range(1,N+1):
        for j in range(1,N+1):
            like, empty = 0,0
            # 빈자리 중에서
            if board[i][j]==0:
                # 좋아하는 학생 수, 빈 자리수 세기
                for d in range(4):
                    nx = i+dx[d]
                    ny = j+dy[d]
                    if 1<=nx<=N and 1<=ny<=N:
                        if board[nx][ny] in prefer[student]:
                            like += 1
                        if board[nx][ny]==0:
                            empty += 1
                if like > maxlike:
                    maxlike = like
                    queue = [[i,j,empty]]
                elif like == maxlike:
                    maxlike = like
                    queue.append([i, j, empty])
    return queue

N = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

prefer = {}
board = [[0]*(N+1) for _ in range(N+1)]
answer = 0
for i in range(N**2):
    tmp = list(map(int,input().split()))
    prefer[tmp[0]] = tmp[1:]
    student = tmp[0]
    queue = search_seat(student)
    maxempty = -1
    maxi,maxj = 0,0
    while queue:
        r,c,empty = queue.pop(0)
        if empty>maxempty:
            maxempty = empty
            maxi,maxj = r,c
    board[maxi][maxj] = student

# 다 구하고 만족도 구해야함.
answer = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        like = 0
        student = board[i][j]
        for d in range(4):
            nx = i+dx[d]
            ny = j+dy[d]
            if 1<=nx<=N and 1<=ny<=N:
                if board[nx][ny] in prefer[student]:
                    like += 1
        answer += int((10)**(like-1))
print(answer)