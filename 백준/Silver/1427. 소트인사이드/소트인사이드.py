strinput = input()
nlist=[]
for i in range(len(strinput)):
    nlist.append(int(strinput[i]))
    
nlist.sort()

for j in range(len(strinput)-1,-1,-1):
    print(nlist[j], end='')