import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B,C = map(int, input().split())

result = 0
for a in A:
    a = a-B #총감독관
    result += 1 
    if a>0:
        result += a//C
        if a%C>0:
            result += 1
print(result)

