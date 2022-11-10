import sys

N = int(sys.stdin.readline())

numlist = []

for i in range(N):
    x = 0
    y = 0
    x,y = map(int, sys.stdin.readline().split())
    numlist.append([x,y])
    
numlist = sorted(numlist, key=lambda x :(x[1],x[0]))

for i in range(N):
    print(numlist[i][0], numlist[i][1])