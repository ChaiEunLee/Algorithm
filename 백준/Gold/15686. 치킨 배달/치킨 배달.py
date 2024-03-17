N,M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

# combination?? time complexity가..
# 각 home , chicken 거리 계산?? 남은 chicken 집별로 최소 거리 합산?
chicken = []
home = []
result = 999999
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i,j))
        elif board[i][j] == 1:
            home.append((i,j))
#print(chicken)
#print(home)

from itertools import combinations
for comb in combinations(chicken,M):
    #print(comb)
    city_len = 0
    for h in home:
        minchicken = 999
        for j in range(M):
            #print(h, comb)
            cur_len = abs(h[0]-comb[j][0]) + abs(h[1]-comb[j][1])
            minchicken = min(minchicken, cur_len)
        city_len += minchicken
    result = min(result,city_len)

print(result)