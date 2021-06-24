w,h,x,y,r = map(int, input().split())

if (r+x <= w) and (r+y <= h) and (x>0) and (y>0):
  print("Yes")
else: print("No")