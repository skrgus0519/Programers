def solution(age):
    answer = ''
    alpha = 'abcdefghij'
    
    answer = ''.join(alpha[int(digit)] for digit in str(age))
    
    return answer