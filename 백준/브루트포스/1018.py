# 체스판 다시 칠하기
# 1018

M, N = map(int, input().split())
board = [input() for _ in range(M)]

min_repaints = float('inf')

for i in range(M - 7):
    for j in range(N - 7):
        repaints_with_B_start = 0
        repaints_with_W_start = 0
        for x in range(8):
            for y in range(8):
                current_color = board[i + x][j + y]
                expected_color_B_start = 'B' if (x + y) % 2 == 0 else 'W'
                expected_color_W_start = 'W' if (x + y) % 2 == 0 else 'B'
                if current_color != expected_color_B_start:
                    repaints_with_B_start += 1
                if current_color != expected_color_W_start:
                    repaints_with_W_start += 1
        min_repaints = min(min_repaints, repaints_with_B_start, repaints_with_W_start)

print(min_repaints)
