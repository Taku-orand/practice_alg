while True:
  n,x = map(int, input().split())
  if n == x == 0:
    break
  count = 0
  for i in range(1,n+1):
    # print(i)
    for j in range(1,n+1):
      for k in range(1,n+1):
        if i < j < k:
          if (i + j + k) == x:
            count += 1
  print(count)