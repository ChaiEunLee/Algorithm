def solution(new_id):
    stand = '1234567890abcdefghijklmnopqrstuvwxyz-_.'
    new_id = new_id.lower()
    new_id2 = ""
    new_id = new_id.strip('.')

    for i in range(len(new_id)):
        if new_id[i] not in stand:
            continue
        elif new_id[i]=='.':
            if new_id2 and new_id2[-1]=='.':
                continue
        new_id2 += new_id[i]

    new_id2 = new_id2.strip('.')

    if not new_id2:
        new_id2 = 'a'

    if len(new_id2) >= 16:
        new_id2 = new_id2[:15]
    elif len(new_id2) < 3:
        while len(new_id2) < 3:
            new_id2 = new_id2 + new_id2[-1]

    new_id2 = new_id2.strip('.')
    return new_id2