def solution(s):
    answer = 0
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in words:
        if i in s:
            idx = str(words.index(i))
            s = s.replace(i, idx)
            
    return int(s)