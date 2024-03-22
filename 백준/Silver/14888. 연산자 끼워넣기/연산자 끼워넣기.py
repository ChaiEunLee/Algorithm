import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))

def DFS(add, sub, mul, div, num, idx):
    #print(add, sub, mul, div, num, idx)
    global max_val
    global min_val

    if idx == N:
        max_val = max(max_val, num)
        min_val = min(min_val, num)

    if add>0:
        DFS(add-1, sub, mul, div, num+number[idx], idx+1)
     
    if sub>0:
        DFS(add, sub-1, mul, div, num-number[idx], idx+1)

    if mul>0:
        DFS(add, sub, mul-1, div, num*number[idx], idx+1)

    if div>0:
        if number[idx] != 0:
            DFS(add, sub, mul, div-1, int(num/number[idx]), idx+1)
max_val =  -int(1e9)
min_val = int(1e9)
DFS(operator[0], operator[1], operator[2], operator[3], number[0] , 1)
print(max_val, min_val)