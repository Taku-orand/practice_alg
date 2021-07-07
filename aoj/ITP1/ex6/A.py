#リスト型で用意されている sort メソッドを使うことで、値を昇順に並び替えることができます。
#リストオブジェクト.sort()
#また、リスト型で用意されている reverse メソッドを使うことで、要素の順番を逆に並び替えることができます。
#リストオブジェクト.reverse()

N = int(input())
a = [int(x) for x in input().split()]
for i in range(N-1,0,-1):
  print(a[i], end=" ")
print(a[0])