while True:
  x,y = map(int, input().split())
  if x == 0 and y == 0:
    break
  if x > y:
    x,y = y,x
  print("%d %d" %(x,y))