N,L = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

def if_can_line(line):
    bri = [False for _ in range(N)]
    for i in range(1,N):
        if abs(line[i-1]-line[i])>1:
            return False
        else:
            # 왼쪽이 더 클 때
            if (line[i-1]-line[i])==1: 
                for j in range(L):
                    if i+j >= N:
                        return False
                    # 평평해야 다리 놓을 수 있음
                    if line[i] != line[i+j]:
                        return False
                    # 이미 다리가 있으면 안 됨.
                    if bri[i+j] == True:
                        return False 
                    if bri[i+j] == False:
                        bri[i+j] = True
            #오른쪽이 더 클 때
            elif (line[i-1]-line[i])==-1:
                for j in range(L):
                    if i-1-j < 0:
                        return False
                    #평평해야함
                    if line[i-1] != line[i-1-j]:
                        return False
                    # 이미 다리가 있으면 안 됨.
                    if bri[i-1-j]==True:
                        return False
                    if bri[i-j-1]==False:
                        bri[i-j-1] = True
    return True
answer = 0
for i in range(N):
    if if_can_line(board[i]):
        answer += 1

for j in range(N):
    road = [board[i][j] for i in range(N)]
    if if_can_line(road):
        answer += 1
    
print(answer)