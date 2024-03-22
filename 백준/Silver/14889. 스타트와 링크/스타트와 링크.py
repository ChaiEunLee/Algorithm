from itertools import combinations
N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

import math
all = set(range(N))
done = 0
minval = 100*10

for tmp in combinations(range(N),N//2):
    cnt = math.comb(N,N//2)//2+1
    if done==cnt:
        break
    done += 1
    first = set(tmp)  
    second = all-first
    #print(first, second, done)
    firstscore = 0
    secondscore = 0
    for elem in combinations(first,2):
        firstscore += S[elem[0]][elem[1]]
        firstscore += S[elem[1]][elem[0]]
    for elem in combinations(second,2):
        secondscore += S[elem[0]][elem[1]]
        secondscore += S[elem[1]][elem[0]]
    if abs(firstscore-secondscore) < minval:
        minval = abs(firstscore-secondscore)
    #print(firstscore, secondscore, minval)
print(minval)