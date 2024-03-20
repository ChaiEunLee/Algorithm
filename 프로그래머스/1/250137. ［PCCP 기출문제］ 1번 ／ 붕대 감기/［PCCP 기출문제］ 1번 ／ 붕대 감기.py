def solution(bandage, health, attacks):
    answer = health
    i = 0
    time = 0
    tstep = 0
    while True:
        if answer <= 0 :
            return -1
        if time == attacks[i][0]:
            answer -= attacks[i][1]
            tstep = 0
            if time == attacks[len(attacks)-1][0]:
                if answer <= 0:
                    return -1
                else:
                    return answer
            i += 1
        else:
            tstep += 1
            #print(tstep)
            answer += bandage[1]
            if tstep == bandage[0]:
                answer += bandage[2]
                tstep = 0
            answer = min(health, answer)
        time += 1
        #print(time, tstep, answer)
    return answer