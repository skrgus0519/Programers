def solution(spell, dic):
    answer = 2
    for d in dic:
        check = []
        for s in spell:
            if s in d:
                check.append(True)
        if len(check) == len(spell):
            print(check, d)
            answer = 1
            
    return answer