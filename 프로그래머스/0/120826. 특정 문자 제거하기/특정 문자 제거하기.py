def solution(my_string, letter):
    answer = my_string.translate({ord(letter): None})
    return answer