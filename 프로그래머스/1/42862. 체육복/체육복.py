def solution(n, lost, reserve):
    # 바로 앞뒤에만 빌려줄 수 있음
    # return 학생 수 최대값
    answer_list = [1]*n
    
    for l in lost:
        answer_list[l-1] -= 1
        
    for r in reserve:
        answer_list[r-1] += 1

    for i in range(n):
        if answer_list[i] == 0:
            
            if i>0 and answer_list[i-1] == 2:
                answer_list[i] += 1
                answer_list[i-1] -= 1
                
            elif i<n-1 and answer_list[i+1]==2:
                answer_list[i] += 1
                answer_list[i+1] -= 1 
    answer = 0
    for j in answer_list:
        if j>0:
            answer += 1
    return answer