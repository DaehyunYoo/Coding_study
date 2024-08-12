n, t = map(int, input().split())

line_top = list(map(int, input().split()))
line_bot = list(map(int, input().split()))

for _ in range(t):
    temp_top_last = line_top[-1]
    
    for i in range(n-1, 0, -1):
        line_top[i] = line_top[i-1]
        
    line_top[0] = line_bot[-1]
    
    for j in range(n-1, 0, -1):
        line_bot[j] = line_bot[j-1]
    line_bot[0] = temp_top_last

print(*line_top)
print(*line_bot)