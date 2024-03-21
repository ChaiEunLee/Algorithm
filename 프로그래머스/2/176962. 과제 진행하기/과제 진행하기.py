def solution(plans):
    # sort in timeline
    plans = sorted(plans, key=lambda plans:(plans[1]))

    # dict로 index 만들고
    start = []
    name = []
    left = []
    for plan in plans:
        h,m = list(map(int, plan[1].split(':')))
        start.append(h*60+m)
        name.append(plan[0])
        left.append(int(plan[2]))

    # start homework
    stack = []
    end = []
    result = []
    #print(start)

    for i in range(len(start)):
        #print(end, start,left)
        end.append(start[i]+left[i])
        if i==len(name)-1:    # last homework는 무리없이 완료
            result.append(name[i])
            break
        if end[i]>start[i+1]:
            stack.append([i , left[i] - (start[i+1]-start[i])])
        else:
            result.append(name[i])
            # 남은 시간 과제하기
            interval = (start[i+1]-end[i])
            while interval != 0 and stack:
                i,curleft = stack.pop()
                if interval>=curleft:
                    interval -= curleft
                    result.append(name[i])
                else:
                    curleft -= interval
                    stack.append([i,curleft])
                    interval = 0

    # 남은 과제들 하나씩 꺼내기
    while stack:
        i,left = stack.pop()
        result.append(name[i])

    return result