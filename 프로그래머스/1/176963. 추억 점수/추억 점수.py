def solution(name, yearning, photo):
    # photo에 있는 사람
    answer = []
    name_dict = {}
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    
    for p in photo:
        memory = 0
        for person in p:
            if person in name_dict:
                memory += name_dict[person]
        answer.append(memory)
        
    return answer