def solution(my_string, num1, num2):
    str_list = list(my_string)
     # num1과 num2의 문자를 교환
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    
    # 리스트를 다시 문자열로 변환하여 반환
    return ''.join(str_list)