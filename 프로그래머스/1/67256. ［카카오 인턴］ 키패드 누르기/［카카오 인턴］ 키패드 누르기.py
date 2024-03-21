def solution(numbers, hand):
    # 147 왼손, 369 오른손, 2580 가까운 손, 오른손잡이/왼손잡이
    # 왼손 *, 오른손 #에서 시작
    l = [3,0]
    r = [3,2]
    # distance 계산해서 하기
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            l = [n//3,0]
        elif n in [3,6,9]:
            answer += 'R'
            r = [n//3-1,2]
        elif n in [2,5,8,0]:
            if n==0:
                cur = [3,1]
            else:
                cur = [n//3,1]
            #print(n,l,r,cur)
            if abs(l[0]-cur[0]) +abs(l[1]-cur[1]) < abs(r[0]-cur[0]) +abs(r[1]-cur[1]):
                answer += 'L'
                l = cur
            elif abs(l[0]-cur[0]) +abs(l[1]-cur[1]) > abs(r[0]-cur[0]) +abs(r[1]-cur[1]):
                answer += 'R'
                r = cur
            else:
                if hand[0]=='l':
                    answer += 'L'
                    l = cur  
                else:
                    answer += 'R'
                    r = cur
    #print(answer)
    return answer