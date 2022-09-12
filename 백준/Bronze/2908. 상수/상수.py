num1, num2 = map(int, input().split())

newnum1 = num1%10 * 100 + (num1//10)%10 * 10 + num1//100
newnum2 = num2%10 * 100 + (num2//10)%10 * 10 + num2//100

if newnum1 > newnum2:
    print(newnum1)
elif newnum1 < newnum2:
    print(newnum2)