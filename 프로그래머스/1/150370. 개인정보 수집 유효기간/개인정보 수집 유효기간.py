def solution(today, terms, privacies):
    # terms : 약관종류' '유효기간 # alphabet, 월 개수
    # privacies : 날짜' '종류
    # 날짜 : .으로 구분
    # today 기준 파기해야할 약관 list로 return
    termdict = {}
    for term in terms:
        contract, due = term.split(' ')
        termdict[contract] = int(due)
    yearnow, monthnow, daynow = today.split('.')
    
    result = []
    for i, priv in enumerate(privacies):
        date, contract = priv.split(' ')
        year, month, day = list(map(int,date.split('.')))

        month += termdict[contract]

        if day == 1:
            day = 28
            month -= 1
        else:
            day -= 1
        
        if month >= 12:
            if month%12 == 0:
                year += month//12-1
                month = 12
            else:
                year += month//12
                month %= 12
        
        if int(yearnow) > year:
            result.append(i+1)
        elif int(yearnow) == year and int(monthnow) > month:
            result.append(i+1)
        elif int(yearnow) == year and int(monthnow) == month and int(daynow) > day:
            result.append(i+1)
        #print(i, yearnow, monthnow, daynow, year, month, day, result)
    return result