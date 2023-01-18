#7. 1004 - 어린 왕자
num = int(input())
for _ in range(num):
    x1,y1,x2,y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx,cy,r = map(int,input().split())        
        d1 = ((cx-x1)**2 + (cy-y1)**2)**(1/2)
        d2 = ((cx-x2)**2 + (cy-y2)**2)**(1/2)
        
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
        #둘다 같은 원 안에 있으면 0번이니까 세지 않음
            cnt += 1
        
    print(cnt)