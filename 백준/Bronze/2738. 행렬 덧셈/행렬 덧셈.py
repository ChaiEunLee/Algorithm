N,M = map(int,input().split())

alist = [[0]*M for i in range(N)]
for i in range(N):
    alist[i] = list(map(int, input().split()))
    
A = alist

blist = [[0]*M for i in range(N)]
for j in range(N):
    blist[j] = list(map(int, input().split()))
B = blist

for n in range(N):
    for m in range(M):
            print(alist[n][m]+blist[n][m], end=' ')
    print()