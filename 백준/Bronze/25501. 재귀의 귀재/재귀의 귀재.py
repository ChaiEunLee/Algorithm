#3. 25501-재귀의 귀재
def recursion(s, l, r):
    global number
    number += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
    
    
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())
for i in range(N):
    number = 0
    S = input()
    print(isPalindrome(S),number)