N = int(input())
score = 0

if N < 100:
    score = N
else:
    score = 99
    for num in range(100, N+1):
        if (num%10 - (num//10)%10 == (num//10)%10 - num//100):
            score+=1
        else:
            score+=0
print(score)