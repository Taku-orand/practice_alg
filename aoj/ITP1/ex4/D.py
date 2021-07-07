n = int(input())
a = [int(x) for x in input().split()]
# a = list(map(int, input.split()))
maxNum = max(a)
minNum = min(a)
sumNum = sum(a)
print(f"{minNum} {maxNum} {sumNum}")