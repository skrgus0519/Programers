def solution(quiz):
    result = []
    for q in quiz:
        parts = q.split()
        X = int(parts[0])
        operator = parts[1]
        Y = int(parts[2])
        Z = int(parts[4])

        if operator == '+':
            calc = X + Y
        elif operator == '-':
            calc = X - Y

        if calc == Z:
            result.append("O")
        else:
            result.append("X")

    return result
