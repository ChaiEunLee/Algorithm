from itertools import combinations
import sys

#N, M = map(int,input().split())
#cards = list(map(int, input().split()))
totalsum = 0
N, M = map(int,sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

cardcomb = list(combinations(cards, 3))
for i in range(len(cardcomb)):
    combSum = 0
    combSum = sum(cardcomb[i])
    if (totalsum < combSum) and (combSum <= M):
        totalsum = sum(cardcomb[i])
    if (totalsum == M):
        break
        
print(totalsum)