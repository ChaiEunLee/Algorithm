import math 
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    n = math.ceil(N/H)
    a = -(N - H*n)
    print(str(H-a)+str(n).zfill(2))