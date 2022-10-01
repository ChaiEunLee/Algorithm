#prime list 먼저 만들고
max_n = 10000
primeyn = [False, False] + [True]*(max_n-1)
primelist = []
for num in range(2, max_n):
    if primeyn[num]:
        primelist.append(num)
        for i in range(num, max_n+1, num):
            primeyn[i] = False
            
#골드바흐 추측 계산
T = int(input())
for i in range(T):
    n = int(input())
    for i in range (int(n/2),0,-1):
        if (i in primelist) and (n-i in primelist):
            print(i, n-i)
            break