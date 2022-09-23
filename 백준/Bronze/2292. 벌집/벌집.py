N = int(input())
num_pile = 1
cnt = 1

while N > num_pile:
    num_pile += 6 * cnt
    cnt += 1
print(cnt)