end_list = []
for i in range(10000000):
    if str(666) in str(i):
        end_list.append(i)
        if len(end_list) == 10000:
            break
N = int(input())
print(end_list[N-1])