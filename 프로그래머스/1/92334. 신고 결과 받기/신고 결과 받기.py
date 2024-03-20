import collections
def solution(id_list, report, k):
    # 내가 신고한 계정이 정지되면 메일 발송
    # 한명이 여러번 신고해도 1번으로 카운트
    # k번이상 신고되면 정지
    # "신고자 신고당한"
    receive = [0]*len(id_list)
    answer = [0]*len(id_list)
    id_dict = {}
    for i, name in enumerate(id_list):
        id_dict[name] = i
    #print(id_dict)
    # key : receive, value : 신고자
    graph = collections.defaultdict(list)
    for tmp in report:
        user, recv = tmp.split(' ')
        if id_dict[user] not in graph[id_dict[recv]]:
            graph[id_dict[recv]].append(id_dict[user])
            receive[id_dict[recv]] += 1
    #print(graph, receive)
    for j in range(len(receive)):
        if receive[j] >= k:
            for user in graph[j]:
                answer[user] += 1
    return answer