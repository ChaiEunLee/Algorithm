#시간초과 -> 틀렸습니다 -> 정답!
M = int(input())
N = int(input())
primesum = 0
primemin = N

for n in range(M, N+1):
    count = 0
    if n > 1:
        for i in range(2, n):
            if n%i == 0: #n/i == n//i 에서 이렇게 바꾸니까 시간초과는 안 뜸!
                count += 1
                break
        if count == 0:
            primesum += n
            if primemin > n:
                primemin = n
            
if primesum == 0:
    print(-1)
else:
    print(primesum,primemin, sep = '\n')