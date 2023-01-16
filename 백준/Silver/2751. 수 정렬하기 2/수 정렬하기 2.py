import sys
N = int(sys.stdin.readline())

numlist = []
for i in range(N):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()
for j in range(N):
    print(numlist[j])