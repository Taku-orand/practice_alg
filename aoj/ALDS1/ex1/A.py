#挿入ソート
def insertionSort(A,N):
  for i in range(N):
    v=A[i]
    j=i-1
    while j >= 0 and A[j] > v:
      A[j+1]=A[j]
      j -= 1
    A[j+1] = v
    printSort(A,N)

def printSort(A,N):
  for i in range(N-1):
    print(A[i],end=" ")
  print(A[N-1])

N = int(input())
A = [int(x) for x in input().split()]
insertionSort(A,N)