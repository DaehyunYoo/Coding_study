def solution(keymap, targets):
    answer = []
    
    for target in targets:    
        cnt = 0
        for i in target:
            flag = False
            min_val = 101
            
            for k in range(len(keymap)):
                if i in keymap[k]:
                    flag = True
                    min_val = min(min_val, keymap[k].index(i))
            if not flag:
                cnt = -1
                break
            cnt += min_val + 1
        
        answer.append(cnt)
                    
    return answer
