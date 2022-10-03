# 다른 접근
import sys
numlist = [0]*8001
N = int(sys.stdin.readline())
#0~8000
#-4000~4000
numbers = []
maxcnt = 1 #시간초과때문에 max(numlist대신 미리 maxcnt값 구하려고 지정)

for _ in range(N):
    i = int(sys.stdin.readline())
    numlist[i+4000] += 1
    numbers.append(i)
    if numlist[i+4000] > maxcnt:
        maxcnt = numlist[i+4000]

numbers.sort()     
#평균값
print(round(sum(numbers)/N))
#중앙값 (시간 초과 때문에 직접 계산)
print(numbers[int((N-1)/2)]) 
#최빈값
modelist = [i-4000 for i in range(len(numlist)) if numlist[i] == maxcnt]
if len(modelist) > 1:
    print(modelist[1])
else:
    print(modelist[0])
#범위
print(max(numbers)-min(numbers))