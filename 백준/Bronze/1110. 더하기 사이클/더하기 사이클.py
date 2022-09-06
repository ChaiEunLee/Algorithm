A = int(input())
new = A
i = 0

while True:
    N1 = new//10 #왜 A//10 하면 값이 오래 걸리고(거의 안나옴) new로 해야하는걸까??????
    N2 = new%10
    N3 = new//10 + new%10
#    N3 = (N1+N2)%10
    new = (N2*10) + (N3%10)
#    new = (N2*10) + N3
    i = i+1
    if (new==A):
        break    
print(i)