n, t = map(int, input().split())

top_left = list(map(int, input().split()))
top_right = list(map(int, input().split()))
bot = list(map(int, input().split()))

for _ in range(t):
    temp_top_left_last = top_left[-1]
    temp_top_right_last = top_right[-1]
    temp_bot_last = bot[-1]
    
    for i in range(n-1, 0, -1):
        top_left[i] = top_left[i-1]
    
    for j in range(n-1, 0, -1):
        top_right[j] = top_right[j-1]
    top_right[0] = temp_top_left_last
    
    for k in range(n-1, 0, -1):
        bot[k] = bot[k-1]
    bot[0] = temp_top_right_last
    
    top_left[0] = temp_bot_last

print(*top_left)
print(*top_right)
print(*bot)