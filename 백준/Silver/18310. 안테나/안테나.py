N = int(input())
house = list(map(int, input().split()))

housesort = sorted(house)

if len(housesort)%2 == 0:
    mid = int(len(housesort)/2)-1
else:
    mid = int(len(housesort)/2)

print(housesort[mid])