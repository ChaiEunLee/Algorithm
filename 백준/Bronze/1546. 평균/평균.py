num = int(input())
score = list(map(int, input().split()))
new_score=[]
for i in range(num):
    new_score.append(score[i]/max(score) * 100)
print(sum(new_score)/num)