## Two Sum – Find two numbers in an array that add up to a target.

# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9

def sum(nums,target):
  n=len(nums)
  for i in range(n):
    for j in range(i+1,n):
      if nums[i]+nums[j]==target:
        return [i,j]
  return []
result=sum([2,7,11,10],12)
print(result) 
    
