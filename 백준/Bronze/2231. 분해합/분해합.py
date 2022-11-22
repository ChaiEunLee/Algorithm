N = int(input())
result = 0

for i in range(1,N+1):
    numlist = list(map(int,str(i)))
    numSum = i + sum(numlist)
    if (numSum == N):
        result = i
        break
        
print(result)