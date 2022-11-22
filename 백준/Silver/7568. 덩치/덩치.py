N = int(input())
input_list = []

for i in range(N):
    input_list.append(list(map(int,input().split())))

for i in range(N):
    level = 0
    for j in range(N):
        if (input_list[i][0] < input_list[j][0]) and (input_list[i][1] < input_list[j][1]):
            level += 1
    print(level+1,end=' ')