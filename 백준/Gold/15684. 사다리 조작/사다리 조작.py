def is_complete(i):
    x, y = 0, i
    while x < height:
        if y - 1 >= 0 and ladders[x][y - 1]:
            y = y - 1
        elif y < line_cnt - 1 and ladders[x][y]:
            y = y + 1
        x += 1
    if y != i:
        return False
    return True


def backtracking(x, y, depth):
    global answer
    # 탈출 전에 지금 조건에서 사다리여부 체크
    if depth >= answer:  # 정답이 될 가능성 없음
        return

    non_correct = 0
    for i in range(line_cnt):
        if not is_complete(i):
            non_correct += 1
    if non_correct > ((answer - 1 - depth) * 2):
        # 하나의 사다리는 2개의 결과를 바꿀 수 있다.
        # 지금이 유망하려면 정답보다 적은 개수로 사다리를 완성시켜야 하는데
        # 안맞는 사다리가 (정답-1)*2개 보다 많다면 가지치기
        return
    elif non_correct == 0:
        answer = min(answer, depth)
        return

    # 탈출 조건
    if depth >= 3:
        return

    for i in range(x, height):
        for j in range(line_cnt - 1):
            if i == x and j <= y:  # 이번 x 줄인데 j가 지금보다 작거나 같은 경우
                continue
            if (j - 1 >= 0 and ladders[i][j - 1]) or (j + 1 < line_cnt - 1 and ladders[i][j + 1]) or ladders[i][j]:
                # 양쪽에 사다리가 하나라도 있을 경우 -> 인접할 수 없다.
                continue
            ladders[i][j] = 1
            backtracking(i, j, depth + 1)
            ladders[i][j] = 0


answer = 4

line_cnt, hor_cnt, height = map(int, input().split())
ladders = [[0 for _ in range(line_cnt - 1)] for _ in range(height)]

for hor in range(hor_cnt):
    a, b = map(lambda x: int(x) - 1, input().split())
    ladders[a][b] = 1

backtracking(0, -1, 0)

if answer == 4:
    print(-1)
else:
    print(answer)