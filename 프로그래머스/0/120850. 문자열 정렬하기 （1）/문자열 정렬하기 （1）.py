def solution(my_string):
    answer = []
    str_list = list(my_string)
    for i in str_list:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
            
    return answer