def solution(balls, share):
    numerator = 1
    for i in range(share):
        numerator *= balls - i

    denominator = 1
    for i in range(1, share + 1):
        denominator *= i

    answer = numerator // denominator
    return answer