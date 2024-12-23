def solution(keyinput, board):  
    moves = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0]
    }
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    position = [0, 0]

    for key in keyinput:
        dx, dy = moves[key]
        
        new_x = position[0] + dx
        new_y = position[1] + dy
        
        position[0] = max(-max_x, min(max_x, new_x))
        position[1] = max(-max_y, min(max_y, new_y))
    
    return position
