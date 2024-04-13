# https://yeon-code.tistory.com/82
# ㅍ아ㅣ썬 
# 15684. 사다리 조작
N,M,H = map(int,input().split())

# 1개, 2개, 3개의 사다리를 추가로 놓고
# 정답을 도출해보기
# 2<=N<=10, 1<=H<=30, 0<=M<=(N-1)*H
# 30*10 300C1 + 300C2 + 300C3 정도 되겠네 괜춘한듯??
#N,M,H = 2, 1, 3
board = [[False]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    board[a-1][b-1] = True

def check():
    wrong = 0
    for start in range(N):
        now = start
        for j in range(H):
            if board[j][now]: #now~now+1을 잇는 선
                now += 1
            elif now>0 and board[j][now-1]: #now-1~now를 잇는 선
                now -= 1
        if now!= start:
            wrong += 1
    return wrong
def dfs(cnt, x, y):
    global ans
    wrong = check()
    if wrong > ((ans - 1 - cnt) * 2):
        return
    elif wrong == 0:
        ans = min(ans,cnt)
        return
    elif cnt==3 or ans <= cnt:
        return
    for i in range(x,H):
        # 지금 탐색하고 있는 행이면
        if i==x:
            now = y #지금 탐색하고 있는 열부터
        # 새로운 행으로 넘어가면
        else:
            now = 0 #0열부터 탐색
        for j in range(now, N-1):
            if not board[i][j] and not board[i][j+1]:
                if j>0 and board[i][j-1]:
                    continue
                board[i][j] = True
                dfs(cnt+1, i, j+2)
                board[i][j] = False

ans = 4
dfs(0,0,0)
print(ans if ans < 4 else -1)
