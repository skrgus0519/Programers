def solution(i, j, k):
    k = str(k)  
    count = 0
    for num in range(i, j + 1):  
        count += str(num).count(k)  
    return count
