#https://ji-gwang.tistory.com/316
num = int(input())
info = []
max_w = 0
max_h = 0
max_widx = 0
max_hidx = 0
for i in range(6):
    inputval = list(map(int,input().split()))
    info.append(inputval)
    if inputval[0] ==1 or inputval[0] == 2: #width
        if max_w < inputval[1]:
            max_w = inputval[1]
            max_widx = i
    else:
        if max_h < inputval[1]:
            max_h = inputval[1]
            max_hidx = i
            
#긴변 2개와 거기에 인접한 변 출력
#index_list = [info[max_hidx-1], info[max_hidx+1], info[max_widx-1],info[max_widx+1]]
# 그 후 가장 긴 가로 및 세로와 인접한 변 2개와 가장긴 가로와 세로 총 4개를 새로운 리스트에 저장한다.
index_list = [info[max_hidx - 1], info[(max_hidx + 1) % 6], info[max_widx - 1],
              info[(max_widx + 1) % 6]]

#뺄 사각형의 넓이
product = 1
for line in info:
    if line not in index_list:
        product *= line[1]
        
result = (max_w*max_h - product)*num
print(result)