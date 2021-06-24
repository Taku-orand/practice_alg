nums = list(map(int, input().split()))

for i in range(2, 0 , -1):
  j = 0
  while(j<i):
    if nums[j] > nums[j + 1]:
      nums[j], nums[j+1] = nums[j+1], nums[j]
    j += 1

print(nums[0],nums[1],nums[2])
  
