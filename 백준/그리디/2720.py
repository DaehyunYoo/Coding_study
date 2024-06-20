T = int(input())  # 케이스의 수를 입력 받습니다.
results = []  # 결과를 저장할 리스트를 초기화합니다.

for _ in range(T):
    exchange = int(input())  # 각 케이스별 교환할 금액을 입력 받습니다.
    
    Quarter, Dime, Nickel, Penny = 0, 0, 0, 0

    while exchange > 0:
        if exchange >= 25:  # 25 센트 이상 남았다면
            Quarter += exchange // 25
            exchange %= 25
        elif exchange >= 10:  # 10 센트 이상 25 센트 미만이 남았다면
            Dime += exchange // 10
            exchange %= 10
        elif exchange >= 5:  # 5 센트 이상 10 센트 미만이 남았다면
            Nickel += exchange // 5
            exchange %= 5
        else:  # 5 센트 미만이 남았다면
            Penny += exchange
            exchange = 0

    results.append(f"{Quarter} {Dime} {Nickel} {Penny}")

for result in results:
    print(result)
