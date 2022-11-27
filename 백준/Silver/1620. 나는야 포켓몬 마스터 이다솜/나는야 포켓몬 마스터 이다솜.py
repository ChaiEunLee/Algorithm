#3. 1620 - 나는야 포켓몬 마스터 이다솜
import sys
N, M = map(int, sys.stdin.readline().split())
poket = {}

for i in range(N):
    poket[i+1] = sys.stdin.readline().strip()
    
poket_reverse = dict(map(reversed,poket.items()))

for j in range(M):
    quiz = sys.stdin.readline().strip()
    if quiz in poket_reverse.keys():
        print(poket_reverse[quiz])
    elif int(quiz) in poket.keys():
        print(poket[int(quiz)])