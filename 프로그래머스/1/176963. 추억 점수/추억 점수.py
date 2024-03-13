def solution(name, yearning, photo):
    return [sum(yearning[name.index(person)] for person in p if person in name) for p in photo]