M, N = map(int, input().split())

chess_list = []
for m in range(M):
    chess_list.append(list(input()))

result_min = []
for i in range(M-7):
    for j in range(N-7):
        result = 0
        result2 = 0
        for r in range(i,i+8):
            for c in range(j,j+8):
                if (r+c)%2 == 0:
                    if chess_list[r][c] != 'W':
                        result += 1
                    if chess_list[r][c] != 'B':
                        result2 += 1
                else:
                    if chess_list[r][c] != 'B':
                        result += 1
                    if chess_list[r][c] != 'W':
                        result2 += 1
        result_min.append(min(result, result2))
print(min(result_min))