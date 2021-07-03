while True:
  h,w =  map(int, input().split())
  flag=1
  if h == w == 0:
    break
  for i in range(h):
    for j in range(w):
      if flag%2==1:
        print("#",end="")
      if flag%2==0:
        print(".",end="")
      flag += 1
    print("")
    flag = 1 if i%2==1 else 0
  print("")
# while True:
#   h,w =  map(int, input().split())
#   flag=1
#   if h == w == 0:
#     break
#   for i in range(h):
#     for j in range(w):
#       print(f"{i + j} ", end="")
#     print("")
#   print("")