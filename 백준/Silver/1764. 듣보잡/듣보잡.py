#5. 1764 - 듣보잡
N, M = map(int, input().split())

notheard = set()
notseen = set()

for _ in range(N):
    notheard.add(input())
for _ in range(M):
    notseen.add(input())
    
inter = notheard.intersection(notseen)
print(len(inter))
for word in sorted(inter):
    print(word)