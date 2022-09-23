N = int(input())

line = 0
max_num = 0

while N > max_num: #입력받은 숫자보다 커지기 전까지만. 입력받은 숫자가 몇번째 라인에 있는지 알려고
    line += 1
    max_num += line

#print("line", line, "max_num", max_num)
gap = max_num - N #그 줄에서 가장 큰수로부터 몇번째에 떨어져있는지 보려고

if line % 2 == 0: #짝수면. 분자는 늘어나고 분모는 줄어듦.
    numer = line - gap
    denom = 1 + gap
else: #홀수면 분자는 감소하고 분모는 늘어남.
    numer = 1 + gap
    denom = line - gap

print(str(numer)+"/"+str(denom))