#3.색종이
#흰색 도화지 100*100
#검은색 색종이 각각 10*10
#입력값 : 왼쪽 변/하단 변과 색종이의 거리 100-L, 100-R

N = int(input())
total = 0
paper = [[0]*100 for i in range(100)]

#검은색이 닿으면 1로 변경. 이미 1이면 넘어감.
for n in range(N):
    L,R = map(int, input().split())
    for i in range(L,L+10): #0~L-1
        for j in range(R, R+10): #0~R-1
            if paper[i][j] == 0:
                paper[i][j] = 1
                
for i in range(100):
    total += sum(paper[i])
print(total)