N = int(input())
s = set(map(int, input().split()))
count = 0
for i in s:
    if i <= 0:
        continue
    if -i in s:
        count += 1



print(count)
