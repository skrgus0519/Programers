def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        for sound in valid_sounds:
            if sound in word:
                word = word.replace(sound, " ", 1) 
        if word.strip() == "":
            count += 1

    return count
