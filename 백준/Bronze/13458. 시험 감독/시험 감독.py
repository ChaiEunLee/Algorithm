N = int(input())
A = list(map(int, input().split()))
B,C = map(int, input().split())
answer = len(A)
for num in A:
    # 총 감독관
    num -= B
    # 부 감독관
    if num > 0:
        answer += (num//C)+1
        if num%C == 0:
            answer -= 1

print(answer)