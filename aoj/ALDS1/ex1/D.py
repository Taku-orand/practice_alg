#利益最大化
def maximum(A):
  minv = A[0]
  maxv = -999999999999999
  for i in range(1,len(A)):
    maxv = max(maxv,A[i]-minv)
    minv = min(minv,A[i])
  return maxv

N = int(input())
A = []
for _ in range(N):
  A.append(int(input()))
print(maximum(A))