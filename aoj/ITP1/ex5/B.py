while True:
  h,w =  map(int, input().split())
  if h == w == 0:
    break
  for i in range(h):
    for j in range(w):
      if i==0 or i==h-1:
        print("#", end="")
        continue
      if j == 0 or j == w-1:
        print("#", end="")
        continue
      print(".", end="")
    print("")
  print("")