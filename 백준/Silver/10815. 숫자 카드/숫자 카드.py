#1. 10815 - 숫자 카드
N = int(input())
have = set(map(int,input().split()))
M = int(input())
cards = list(map(int,input().split()))

for i in range(M):
    if cards[i] in have:
        print(1, end = ' ')
    else:
        print(0, end = ' ')