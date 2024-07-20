# 일곱 난쟁이
# 2309

from itertools import combinations

lst = []
for _ in range(9):
    A = int(input())
    lst.append(A)

for i in combinations(lst, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break