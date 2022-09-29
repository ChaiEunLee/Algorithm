max_n = 123456
primeyn = [False, False] + [True]*(2*max_n-1)
primelist = []
for num in range(2, 2*max_n+1): #2부터 시작하는거라서 2는 소수가 맞고, 2의 배수는 다 제거하고 3으로 돌아와서 하는거라서 이렇게 해도 잘 됨.
    if primeyn[num]:
        primelist.append(num)
        for i in range(2*num, 2*max_n+1, num):
            primeyn[i] = False

n = int(input())
while n != 0:
    print(len([prime for prime in primelist if (prime > n) and (prime <= 2*n)]))
    n = int(input())