#유클리드 호제법으로 구하기!
T = int(input())

for i in range(T):
    n,m = map(int, input().split())

    if n>=m:
        large = n
        small = m
    else:
        large = m
        small = n

    tmp = 1

    while True:
        if small == 0:
            break
        tmp = large #
        large = small #예전 small를 다음 단계에 large로 쓸거라서
        small = tmp%small #large%small로 나눠서 small로 덮어씌우는거니까
        #print(tmp, large, small)
    maxdiv = large
    print(int(n*m/maxdiv)) #n*m / 최대공약수 = 최소공배수