max_num = 0
for i in range(1,10):
    a = int(input())
    if a > max_num:
        max_num = a
        num = i
print(max_num, "\n"+str(num))