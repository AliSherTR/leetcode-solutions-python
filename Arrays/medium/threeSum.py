from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        result = []
        nums.sort()  # Sorting to simplify the logic
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element
            
            j, k = i + 1, len(nums) - 1  # Two-pointer technique
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1  # Skip duplicates for the second element
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1  # Skip duplicates for the third element
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
        