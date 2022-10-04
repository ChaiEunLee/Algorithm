#list로 심플하게 풀기

import sys
#sys.stdin.readline()

N = int(sys.stdin.readline())
#N = int(input())

cordlist = []

for i in range(N):
#    x,y = map(int, input().split())
    x,y = map(int, sys.stdin.readline().split())
    cordlist.append([x,y])
    
cordlist.sort()

for i in range(N):
    print(cordlist[i][0], cordlist[i][1])