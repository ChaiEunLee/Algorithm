a,b,c = map(int, input().split())
while(a!=0 or b!=0 or c!=0):
    if c**(2) == a**(2)+b**(2):
        print('right')
    elif a**(2) == c**(2)+b**(2):
        print('right')
    elif b**(2)==a**(2)+c**(2):
        print('right')
    else:
        print('wrong')
    a,b,c = map(int, input().split())