x = 1
num_list = []

def d(x):
    s = str(x)
    num = x
    for i in s:
        num += int(i)
    return num


while x <= 10000:
    try:
        num_list.append(d(x))
        x+=1
    except:
        break
        
for i in range(1, 10001):
    if i not in num_list:
        print(i)