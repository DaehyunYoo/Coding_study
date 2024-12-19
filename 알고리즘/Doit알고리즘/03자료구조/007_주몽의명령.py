# 주몽의 명령
# 백준 1940

N = int(input())
M = int(input())

materials = list(map(int, input().split()))

materials.sort()

start = 0
end = N - 1
count = 0

while start < end:
    if materials[start] + materials[end] == M:
        count += 1
        start += 1
        end -= 1
    elif materials[start] + materials[end] > M:
        end -= 1
    else:
        start += 1

print(count)