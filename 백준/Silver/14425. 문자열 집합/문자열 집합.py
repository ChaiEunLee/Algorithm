#2. 14425 - 문자열 집합
N,M = list(map(int, input().split()))
S_list = []
for i in range(N):
    S_list.append(input())
    
count = 0
S_set = set(S_list)
for j in range(M):
    inputword = input()
    if inputword in S_set:
        count += 1
    
print(count)