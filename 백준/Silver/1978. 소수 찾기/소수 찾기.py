N = int(input())
numlist= list(map(int, input().split()) )
primecnt = 0
for num in numlist:
    count = 0
    for i in range(1, num+1):
        if num/i == num//i:
            count += 1
        else:
            count += 0
    if count == 2:
        primecnt += 1
print(primecnt)