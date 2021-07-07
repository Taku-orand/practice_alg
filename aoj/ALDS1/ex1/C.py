import math
def isPrime(n):
  if n == 2:
    return True
  if n < 2 or n % 2 == 0:
    return False
  i = 3
  while i <= int(math.sqrt(n)):
    if n % i == 0:
      return False
    i += 2
  return True

count=0
n = int(input())
for _ in range(n):
  x = int(input())
  if isPrime(x) == True:
    count+=1
print(count)