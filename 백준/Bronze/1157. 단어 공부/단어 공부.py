word = input()
worddict = {}
for letter in word:
    if letter.upper() in worddict:
        worddict[letter.upper()] += 1
    else:
        worddict[letter.upper()] = 1


modeword = []
for key,value in worddict.items():
    if value == max(worddict.values()):
        modeword.append(key.upper())

if len(modeword) > 1:
    print('?')
else:
    print(modeword[0])