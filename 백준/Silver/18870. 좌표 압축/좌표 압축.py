#찾을 때 dict로 time complexity 낮추기
import sys

#N = int(input())
N = int(sys.stdin.readline())

numlist = []
#numlist = list(map(int,input().split()))
numlist = list(map(int,sys.stdin.readline().split()))

numsort = sorted(list(set(numlist)))
numdict = {}

for i in range(len(numsort)):
    numdict[numsort[i]] = i
for i in numlist:
    print(numdict[i], end = ' ')