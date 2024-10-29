import sys

T = int(sys.stdin.readline())

for i in range(T):
    A,B = map(int, input().split())
    print("Case #" + str(i+1) + ": " + str(A+B))