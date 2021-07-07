x,y,z = map(int, input().split())
num = 0
for i in range(x, y+1):
  if z % i == 0:
    num += 1
print(num)