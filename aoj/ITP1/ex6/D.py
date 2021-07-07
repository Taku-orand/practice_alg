n,m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
b = [0 for _ in range(m)]
c = [0 for _ in range(n)]
for i in range(n):
  a[i]= list(map(int,input().split()))
for i in range(m):
  b[i] = int(input())

for i in range(n):
  for j in  range(m):
    c[i] += int(a[i][j])*b[j]

for num in c:
  print(num)