T = int(input())
for i in range(T):
    num, input_chr = input().split()
    for j in range(len(input_chr)):
        print(input_chr[j]*int(num), end='')
    print()