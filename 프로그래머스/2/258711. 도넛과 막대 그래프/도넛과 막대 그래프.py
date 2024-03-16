def solution(edges):
    input_count = [0 for _ in range(1000001)]
    output_count = [0 for _ in range(1000001)]

    create = -1
    stick, eight, donut = 0,0,0
    maxnode = -1

    for a,b in edges:
        maxnode = max(maxnode, a, b)
        output_count[a] += 1 #output이 있는 노드
        input_count[b] += 1 #input이 있는 노드

    for i in range(1,maxnode+1):
        if input_count[i] == 0 and output_count[i] >= 2:
            create = i
        elif input_count[i] >= 1 and output_count[i]==0:
            stick += 1
        elif input_count[i] >= 2 and output_count[i] == 2:
            eight += 1
    donut = output_count[create] - stick - eight
    #print(create, donut, stick, eight)
    return [create, donut, stick, eight]
