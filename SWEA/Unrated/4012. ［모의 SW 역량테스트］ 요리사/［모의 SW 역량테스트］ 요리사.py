#import sys
#sys.stdin = open("input.txt", "r")
from itertools import combinations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    food = []
    for _ in range(N):
        food.append(list(map(int,input().split())))
        
    foodlist = set([i for i in range(N)])
    mindiff = 20000*8*2
    for grp in combinations(range(N),N//2):
        A,B = 0,0
        for r,c in combinations(grp, 2):
	        A += food[r][c] + food[c][r]
        rest = foodlist.difference(grp)
        for r,c in combinations(rest,2):
	        B += food[r][c] + food[c][r]
        if abs(A-B) < mindiff:
            mindiff = abs(A-B)
    print('#{} {}'.format(test_case, mindiff))