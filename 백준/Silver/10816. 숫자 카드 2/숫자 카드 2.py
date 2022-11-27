#4. 10816 - 숫자카드2
N = input()
have = list(map(int, input().split()))
M = input()
ifhave = list(map(int, input().split()))

myDict = {}
for i in have:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1
        
for j in ifhave:
    if j in myDict:
        print(myDict[j], end=' ')
    else:
        print(0, end = ' ')