#7. 11478 - 서로 다른 부분 문자열의 개수
word = input()

wordset = set()

for n in range(len(word)):
    for i in range(len(word)-n):
        wordset.add(word[i:i+n+1])
print(len(wordset))