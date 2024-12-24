def solution(dots):
    x_code = [dot[0] for dot in dots]
    y_code = [dot[1] for dot in dots]

    width = max(x_code) - min(x_code)
    height = max(y_code) - min(y_code)
    
    return width * height
