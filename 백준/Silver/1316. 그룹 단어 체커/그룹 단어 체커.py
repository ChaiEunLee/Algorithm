word_number = int(input())
grp_word_cnt = 0

for i in range(0, word_number):
    word = input()
    grp_word = []

    for i in range(len(word)):
        if (word[i] not in grp_word) or (word[i] == word[i-1]):
            grp_word.append(word[i])

        if len(grp_word) == len(word):
            grp_word_cnt += 1
print(grp_word_cnt)