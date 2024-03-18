def solution(friends, gifts):
    from collections import defaultdict
    from itertools import combinations
    # give, receive, index = give-receive
    N = len(friends)
    record = [[0 for _ in range(N)] for _ in range(N)]
    index = defaultdict(int)
    for gift in gifts:
        A, B = gift.split(' ')
        index[A] += 1
        index[B] -= 1
        record[friends.index(A)][friends.index(B)] += 1 #row : give, col : receive
    #print(index, record)
    
    answer = [0]*N
    # Predict next month
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            #record[i][j] #give
            #record[j][i] #receive
            if record[i][j] == record[j][i]:
                if index[friends[i]] > index[friends[j]]:
                    answer[i] += 1
            elif record[i][j] > record[j][i]:
                answer[i] += 1
    #print(answer)
    return max(answer)