sentence = input()
if sentence == ' ':
    print(0)
else:
    print(len(sentence.strip().split(' ')))