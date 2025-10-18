N = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
i = 0
j = N - 1
while i < j:
  if a[i] + a[j] == 0:
    count += 1
    i += 1
    j -= 1
  elif a[i] + a[j] > 0:
    j -= 1
  else:
    i += 1

print(count)
