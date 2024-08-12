n = int(input())
lst = []
for _ in range(n):
    a = int(input())
    lst.append(a)

s1, e1 = map(int, input().split())

s2, e2 = map(int, input().split())

temp = []
for i in range(n):
    if not (s1-1 <= i <= e1-1):  # s1-1부터 e1-1까지의 인덱스가 아닌 경우만 추가
        temp.append(lst[i])

result = []
for j in range(len(temp)):
    if not (s2-1 <= j <= e2-1):  # s2-1부터 e2-1까지의 인덱스가 아닌 경우만 추가
        result.append(temp[j])

print(len(result))
for k in result:
    print(k)