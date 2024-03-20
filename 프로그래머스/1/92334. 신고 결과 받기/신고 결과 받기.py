def solution(id_list, report, k):
    # 내가 신고한 계정이 정지되면 메일 발송
    # 한명이 여러번 신고해도 1번으로 카운트
    # k번이상 신고되면 정지
    # "신고자 신고당한"
    answer = [0]*len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split(' ')[1]] += 1
    for r in set(report):
        if reports[r.split(' ')[1]] >= k:
            answer[id_list.index(r.split(' ')[0])] += 1
    return answer