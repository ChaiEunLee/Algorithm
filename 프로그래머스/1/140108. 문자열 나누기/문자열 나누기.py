def solution(s):
    answer = 0
    xcnt = 1
    x = s[0]
    elsecnt = 0
    if len(s)>1:
        for i in range(1,len(s)):
            if s[i]==x:
                xcnt += 1
            else:
                elsecnt += 1

            if xcnt == elsecnt:
                answer += 1
                xcnt = 0
                elsecnt = 0
                if i<len(s)-1:
                    x = s[i+1]
            else: #xcnt != elsecnt
                # last element
                if i == len(s)-1:
                    answer += 1
    else:
        answer = 1
    return answer