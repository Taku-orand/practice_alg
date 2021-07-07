cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]
N = int(input())
for i in range(N):
  ch,rank = input().split()
  cards[pattern.index(ch)][int(rank)-1]=True
for i in range(4):
  for j in range(13):
    if cards[i][j] == False:
      print(pattern[i],j+1)