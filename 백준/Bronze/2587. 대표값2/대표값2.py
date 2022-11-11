numlist = []
for _ in range(5):
    numlist.append(int(input()))
#   numlist.append(int(sys.stdin.readline()))

numlist.sort()
print(int(sum(numlist)/len(numlist)))
print(numlist[2])