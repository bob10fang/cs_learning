class Window(object):
    def __init__(self, a1, a2, a3, a4, num):
        self.x1 = a1
        self.y1 = a2
        self.x2 = a3
        self.y2 = a4
        self.n = num

N, M = map(int, input().split())
windows = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    windows.append(Window(x1, y1, x2, y2, i + 1))

ans = []

for i in range(M):
    x, y = map(int, input().split())
    j = N - 1
    while j >= 0:
        if windows[j].x1 <= x <= windows[j].x2 and windows[j].y1 <= y <= windows[j].y2:
            ans.append(windows[j].n)
            if j < N - 1:
                temp = windows[j]
                windows[j] = windows[N - 1]
                windows[N - 1] = temp
            break
        j -= 1
    if j == -1:
        ans.append(-1)

for i in ans:
    if i == -1:
        print("IGNORED")
    else:
        print(i)
