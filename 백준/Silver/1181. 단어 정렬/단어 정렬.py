import sys

#N = int(input())
N = int(sys.stdin.readline())
wordlist = {}

for i in range(N):
    inputwordSize = 0
    inputword = input()
    inputwordSize = len(inputword)
    if inputword not in wordlist:
        wordlist[inputword] = inputwordSize

#https://codechacha.com/ko/python-sorting-dict/
sortdict = {}
sortdict = sorted(wordlist.items(), key = lambda x:(x[1],x[0]))

for i in range(len(wordlist)):
    print(sortdict[i][0])