def solution(order):   
    answer = 0
    order = list(str(order))
    for i in order:
        if i in "369":
            answer += 1
    return answer