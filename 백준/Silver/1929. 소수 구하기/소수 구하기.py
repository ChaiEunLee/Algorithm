M, N = map(int, input().split())
primeyn = [False, False] + [True] * (2*N-1)
primelist = []

for num in range(2, N+1):
    if primeyn[num]:
        primelist.append(num)
        for i in range(2*num, N+1, num):
            primeyn[i] = False
for prime in primelist:
    if prime >= M:
        print(prime)