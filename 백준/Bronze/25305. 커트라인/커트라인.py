N, k = map(int, input().split())
score_list = []
score_list = list(map(int, input().split()))
print(sorted(score_list)[len(score_list)-k])