S = input()
for x in range(97,123):
    if chr(x) in S:
        x_chr = chr(x)
        print(S.find(x_chr), end = ' ')
    else:
        print(-1, end =' ')