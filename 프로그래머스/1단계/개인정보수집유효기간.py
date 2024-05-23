def solution(today, terms, privacies):
    answer = []
    date, tp = [], []
    
    for i in privacies:
        a, b = i.split(' ')
        date.append(a)
        tp.append(b)
    
    for i in range(len(date)):
        date[i] = date[i].replace('.', '')
    
    terms_dict = {}
    for i in terms:
        term_type, duration = i.split(' ')
        terms_dict[term_type] = int(duration)
    
    for i in range(len(date)):
        term_type = tp[i]
        if term_type in terms_dict:
            now = date[i]
            new_month = int(now[4:6]) + terms_dict[term_type]
            new_year = int(now[:4])
            while new_month > 12:
                new_year += 1
                new_month -= 12
            new_date = f"{new_year:04d}{new_month:02d}{now[6:]}"
            if new_date <= today.replace('.', ''):
                answer.append(i + 1)
    
    return answer
