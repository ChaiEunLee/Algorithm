def move(N, start, end):
    print(start,end)
    
def hanoi(N, start, end, via):
    if N == 1:
        move(1, start, end)
    else:
        hanoi(N-1, start, via, end)
        move(N, start, end)
        hanoi(N-1, via, end, start)
        
N = int(input())

print(2**(N)-1)
hanoi(N, 1,3,2)