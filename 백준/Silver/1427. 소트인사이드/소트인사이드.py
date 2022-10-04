number = input()
numlist = [0]*10
for i in range(len(number)):
    new = int(number[i])
    for j in range(len(numlist)):
        if numlist[j] <= new: #내림차순
            #한칸씩 뒤로 밀기 
            numlist[j+1:len(numlist)] = numlist[j:len(numlist)-1]#j~len(numlist)-1
            numlist[j] = new
#            print(j, numlist, new)
            break
for i in range(len(number)):
    print(str(numlist[i]),end='')