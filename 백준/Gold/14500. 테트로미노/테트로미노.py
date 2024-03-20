N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

visit = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

ans = 0
max_val = max(map(max, board)) #최대값 넣고 시작

def dfs(r,c, idx, total):
    global ans
    if ans >= total+max_val*(3-idx): #최대값이 이미 나오면 굳이 더 볼필요없이 다음 스텝으로 가려고 return
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc]==0:
                if idx==1: # ㅗ자 모양을 만들기 위해서 2번째 블록을 선택했을 때 다시 탐색하는 것.
                    visit[nr][nc] = 1
                    dfs(r,c,idx+1,total+board[nr][nc]) #
                    visit[nr][nc] = 0 #이게 포인트인듯!
                visit[nr][nc] = 1
                dfs(nr,nc,idx+1,total+board[nr][nc])
                visit[nr][nc] = 0 #이게 포인트인듯!

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r,c,0,board[r][c])
        visit[r][c] = 0 #이게 포인트인듯!

print(ans)