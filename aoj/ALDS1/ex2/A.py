# def bubbleSort(A,N):
#   flag=1
#   count=0
#   while flag:
#     flag=0
#     for i in range(N-1,0,-1):
#       if A[i-1] > A[i]:
#         A[i],A[i-1]=A[i-1],A[i]
#         flag=1
#         count+=1
#   return count

def bubbleSort(A,N):
  count = 0
  for i  in range(0,N-1,1):
    for j in range(N-1,0,-1):
      if j < i:# for(j=N-1; j>i :j--)
        break
      if A[j-1] > A[j]:
        A[j],A[j-1]=A[j-1],A[j]
        print(A)
        count+=1
  return count

N=int(input())
A = list(map(int, input().split()))
count = bubbleSort(A,N)
for i in range(N-1):
  print(A[i],end=" ")
print(A[N-1])
print(count)