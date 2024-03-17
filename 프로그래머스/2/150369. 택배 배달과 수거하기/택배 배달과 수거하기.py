def solution(cap, n, deliveries, pickups):
    deliv = 0 #배달해야하는것, 음수면 추가로 배달할 수 있는것
    pick = 0 #픽업해야하는것, 음수면 추가로 픽업할 수 있는 공간
    answer = 0

    k = 0
    for i in range(n-1,-1,-1):
        #print("i : ", i)
        # 배달할거하고 픽업할거함
        deliv += deliveries[i]
        pick += pickups[i]
        #print(deliv, pick)
        # 캐파가 부족하면 물류창고감.
        while deliv>0 or pick>0: #물류 창고 가야하면
            deliv -= cap 
            pick -= cap
            #print("done:", deliv, pick)
            answer += (i+1) * 2
            #print("answer: ", answer)
    return answer