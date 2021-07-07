presidence = [[[0 for _ in range(10)]  for _ in range(3)] for _ in range(4)]
N = int(input())
for _ in range(N):
  b,f,r,v = map(int, input().split())
  presidence[b-1][f-1][r-1] += v

for i in range(4):
  for j in range(3):
    for k in range(10):
      print(f" {presidence[i][j][k]}", end="")
    print()
  if i != 3:
    print("####################")
