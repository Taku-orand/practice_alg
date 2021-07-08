#挿入ソート
def insertionSort(A,N,g):
  global cnt
  for i in range(g,N):
    v=A[i]
    j=i-g
    while j >= 0 and A[j] > v:
      A[j+g]=A[j]
      j -= g
      cnt+=1
    A[j+g] = v
#シェルソート
def shellSort(A,N):
  h=1
  g = []
  while h<=N:
    g.append(h)
    h = h*3 + 1
  g.reverse()
  for i in range(len(g)):
    insertionSort(A,N,g[i])
  return g

cnt = 0
N = int(input())
A = [int(input()) for _ in range(N)]
g = shellSort(A,N)
print(len(g))
for i in range(len(g)-1):
  print(g[i],end=" ")
print(g[len(g)-1])
print(cnt)
for i in range(N):
  print(A[i])