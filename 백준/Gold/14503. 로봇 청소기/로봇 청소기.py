import sys
input = sys.stdin.readline
N,M = map(int, input().split())
r,c,d = map(int,input().split())
clean = []
for i in range(N):
    clean.append(list(map(int, input().split())))
    

curri, currj = r,c #index는 0~N-1, 0~M-1
#0인 경우 북쪽,1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽
direction = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]} #반시계는 key-1

result = 1
clean[curri][currj] = -1 #이게 포인트!

while True:
    ifdirty = 0
    #print(curri, currj, clean[curri][currj], result)
    if clean[curri][currj] == 1 :
        print(result)
        break

    # 시작
    #result += 1
    if clean[curri][currj] == 0:
        clean[curri][currj] = -1 # 청소

    # Move
    # 직진이 아니라 일단 돌고 봄.
    for i in range(1,5): #반시계 : 북->서->남->동 : 0->3->2->1
        newi = curri+direction[(d-i)%4][0]
        newj = currj+direction[(d-i)%4][1]        
        if clean[newi][newj] == 0:
            if clean[newi][newj] != -1:
                curri,currj = newi,newj
                d = (d-i)%4
                ifdirty = 1
                result += 1
                break

    # 갈데가 없으면 다시 돌아온 그 처음 위치로 감.
    if ifdirty==0:
        # 후진
        curri = curri - direction[d][0]
        currj = currj - direction[d][1]
