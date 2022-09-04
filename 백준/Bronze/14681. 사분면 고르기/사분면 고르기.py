x = int(input())
y = int(input())

# and 대신에 & 쓰면 답이 안 나옴. &는 비트 연산자라서 비트로 바꾸고 각 자리수마다 &로 계산함.
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")