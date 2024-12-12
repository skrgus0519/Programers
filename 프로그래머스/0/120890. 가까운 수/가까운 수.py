def solution(array, n):
    answer = 0
    closer = float('inf')
    for i in array:
        temp = n-i
        if temp < 0:
            temp *= -1
        if closer > temp:
            closer = temp
            answer = i
        if closer == temp:
            if answer > i:
                answer = i
    return answer