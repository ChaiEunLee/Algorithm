a = int(input())
for k in range(a):
    score = input()
    num = 0
    sum_score = 0
    for i in range(0, len(score)):
        if score[i]=="O":
            num += 1
        else:
            num = 0
#        print(score[i],num)
        sum_score += num
    print(sum_score)