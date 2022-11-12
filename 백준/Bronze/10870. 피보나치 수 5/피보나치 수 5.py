#2. 피보나치 수 5
def Fibonnaci(n:int)->int:
    if n==0 or n==1:
        return n
    else:
        return Fibonnaci(n-1) + Fibonnaci(n-2)
    
N = int(input())
print(Fibonnaci(N))