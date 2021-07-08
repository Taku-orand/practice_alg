def selectionSort(A,N):
  count = 0
  for i in range(0,N,1):
    minj=i
    for j in range(i,N,1):
      if A[minj] > A[j]:
        minj=j
    A[minj], A[i] = A[i], A[minj]
    if A[i] != A[minj]:
      count += 1
  return count

N = int(input())
A = list(map(int, input().split()))
count = selectionSort(A,N)
for i in range(0,N-1,1):
  print(A[i],end=" ")
print(A[N-1])
print(count)