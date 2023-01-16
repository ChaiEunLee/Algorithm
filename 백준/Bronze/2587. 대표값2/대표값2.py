numlist = []
for i in range(5):
    numlist.append(int(input()))
    
numlist.sort()
print(int(sum(numlist)/len(numlist)))
print(numlist[2])