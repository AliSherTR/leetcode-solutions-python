###################################################### BRUTE FORCE APPROACH ###########################################################
class Solution: 
    def twoSum(self, nums: list[int] , target: int) -> list[int]:
        for i in range (len(nums) -1):
            for j in range (len (nums) -1):
                if(nums[i] + nums[j] == target):
                    return [i, j]

s = Solution();
print(s.twoSum([1 ,3, 5, 7] , 8))



######################################################## OPTIMIZED SOLUTION ############################################################## 
def twoSum(nums: list[int] , target: int):
    num_to_index = {}

    for i , num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:  
                return [num_to_index[complement], i]  
    
        num_to_index[num] = i  

print(twoSum([1 ,3, 5, 7] , 8))