#最大公約数
def gcd(x,y):
  if x < y:
    x,y= y,x
  d = -1
  while y != 0:
    r = x % y
    x = y
    y = r
  return x

x,y = map(int, input().split())
print(gcd(x,y))