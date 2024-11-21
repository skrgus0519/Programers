def solution(numbers):
    answer = 0
    list = []
    
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            list.append(numbers[i] * numbers[j])
    answer = max(list)
    return answer